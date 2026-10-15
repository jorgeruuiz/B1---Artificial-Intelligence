"""Helper functions for the Innovation Lab workshop notebooks.

The notebooks keep the steps that matter for the workshop: the configuration,
the training call, explainability and compression. This module holds the
boilerplate around them:

- Data: preprocessing statistics, transforms, datasets, loaders, image display
- Training: training loop, evaluation, saving and loading the model
- Results: learning curves and confusion matrix
- XAI: sampling test images and plotting explanations
- Compression: size, sparsity, latency, quantization helpers
- MANOLO: exporting the dataset in MANOLO's tensor format

Every function takes its settings as arguments, so the module never reads the
notebook's variables.
"""

from __future__ import annotations

import copy
import io
import json
import random
import time
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import torch
from pytorch_grad_cam.utils.image import show_cam_on_image
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision.models import quantization as qmodels
from torchvision.transforms import v2

from architecture import build_model

# =============================================================================
# Data
# =============================================================================


def _image_steps(image_size: int, grayscale: bool) -> list:
    """Decode to a uint8 tensor, optionally reduce to one channel, resize."""
    steps = [v2.ToImage()]
    if grayscale:
        steps.append(v2.Grayscale(num_output_channels=1))
    steps.append(v2.Resize((image_size, image_size), antialias=True))
    return steps


def compute_mean_std(
    train_dir: str | Path, image_size: int, grayscale: bool, max_images: int = 2000, seed: int = 42
) -> tuple[list[float], list[float]]:
    """Per-channel mean and standard deviation of the training images, in [0, 1] units.

    Uses the training split only (at most ``max_images`` random images), so nothing from the
    validation or test images leaks into the preprocessing.
    """
    transform = v2.Compose([*_image_steps(image_size, grayscale), v2.ToDtype(torch.float32, scale=True)])
    dataset = datasets.ImageFolder(train_dir, transform=transform)
    indices = random.Random(seed).sample(range(len(dataset)), min(max_images, len(dataset)))
    total, total_squared, pixels = 0.0, 0.0, 0
    for index in indices:
        image = dataset[index][0].double()
        total = total + image.sum(dim=(1, 2))
        total_squared = total_squared + (image**2).sum(dim=(1, 2))
        pixels += image.shape[1] * image.shape[2]
    mean = total / pixels
    std = (total_squared / pixels - mean**2).sqrt()
    return [round(float(value), 4) for value in mean], [round(float(value), 4) for value in std]


def build_transforms(
    image_size: int, mean: list[float], std: list[float], grayscale: bool, augment: bool = False
) -> v2.Compose:
    """Decode, optional grayscale, resize, optional horizontal flip, scale to [0, 1], normalise."""
    steps = _image_steps(image_size, grayscale)
    if augment:
        steps.append(v2.RandomHorizontalFlip())
    steps += [v2.ToDtype(torch.float32, scale=True), v2.Normalize(mean, std)]
    return v2.Compose(steps)


def make_datasets(
    dataset_dir: str | Path,
    image_size: int,
    mean: list[float],
    std: list[float],
    grayscale: bool,
    augment: bool = False,
) -> dict[str, datasets.ImageFolder]:
    """ImageFolder datasets for the train, val and test splits. Augmentation applies to train only."""
    folders = {"train": "train", "val": "val", "test": "test"}
    dsets = {}
    for split, folder in folders.items():
        transform = build_transforms(image_size, mean, std, grayscale, augment=augment and split == "train")
        dsets[split] = datasets.ImageFolder(Path(dataset_dir) / folder, transform=transform)
    classes = dsets["train"].classes
    for split, dataset in dsets.items():
        if dataset.classes != classes:
            raise ValueError(f"'{split}' has the classes {dataset.classes}, 'train' has {classes}")
    return dsets


def describe(dsets: dict[str, datasets.ImageFolder]) -> None:
    """Print the number of images per class in each split."""
    for split, dataset in dsets.items():
        counts = np.bincount(dataset.targets, minlength=len(dataset.classes))
        per_class = ", ".join(f"{name}: {count}" for name, count in zip(dataset.classes, counts))
        print(f"{split:5s} {len(dataset):6d} images | {per_class}")


def make_loaders(
    dsets: dict[str, datasets.ImageFolder], batch_size: int, num_workers: int = 4, pin_memory: bool = False
) -> dict[str, DataLoader]:
    """One DataLoader per split. Only the training loader shuffles."""
    return {
        split: DataLoader(
            dataset,
            batch_size=batch_size,
            shuffle=split == "train",
            num_workers=num_workers,
            pin_memory=pin_memory,
            persistent_workers=num_workers > 0,
        )
        for split, dataset in dsets.items()
    }


def to_display(image: torch.Tensor, mean: list[float], std: list[float]) -> np.ndarray:
    """Undo the normalisation of one (C, H, W) image and return an (H, W, 3) array in [0, 1]."""
    image = image.detach().cpu().float()
    image = image * torch.tensor(std).view(-1, 1, 1) + torch.tensor(mean).view(-1, 1, 1)
    if image.shape[0] == 1:
        image = image.repeat(3, 1, 1)
    return image.clamp(0, 1).permute(1, 2, 0).numpy()


def show_samples(dataset: datasets.ImageFolder, mean: list[float], std: list[float], n: int = 8, seed: int = 42) -> None:
    """Plot ``n`` random images of a dataset, as the model receives them."""
    indices = random.Random(seed).sample(range(len(dataset)), n)
    fig, axes = plt.subplots(1, n, figsize=(2 * n, 2.4))
    for ax, index in zip(axes, indices):
        image, label = dataset[index]
        ax.imshow(to_display(image, mean, std))
        ax.set_title(dataset.classes[label], fontsize=9)
        ax.axis("off")
    plt.show()


# =============================================================================
# Training and evaluation
# =============================================================================


def _autocast(device: torch.device, use_amp: bool):
    """bfloat16 mixed precision on the GPU when requested, plain float32 otherwise."""
    return torch.autocast(device.type, dtype=torch.bfloat16, enabled=use_amp and device.type == "cuda")


def train_one_epoch(
    model: nn.Module, loader: DataLoader, optimizer: torch.optim.Optimizer, device: torch.device, use_amp: bool = False
) -> tuple[float, float]:
    """Train for one epoch with cross-entropy and return the mean loss and the accuracy."""
    model.train()
    criterion = nn.CrossEntropyLoss()
    total_loss, correct, seen = 0.0, 0, 0
    for images, labels in loader:
        images = images.to(device, non_blocking=True)
        labels = labels.to(device, non_blocking=True)
        optimizer.zero_grad(set_to_none=True)
        with _autocast(device, use_amp):
            logits = model(images)
            loss = criterion(logits, labels)
        loss.backward()
        optimizer.step()
        total_loss += loss.item() * labels.size(0)
        correct += (logits.argmax(dim=1) == labels).sum().item()
        seen += labels.size(0)
    return total_loss / seen, correct / seen


@torch.no_grad()
def predict(
    model: nn.Module, loader: DataLoader, device: torch.device, use_amp: bool = False
) -> tuple[torch.Tensor, torch.Tensor]:
    """Logits and labels of every sample of ``loader``, in loader order, on the CPU."""
    model.eval()
    all_logits, all_labels = [], []
    for images, labels in loader:
        with _autocast(device, use_amp):
            logits = model(images.to(device, non_blocking=True))
        all_logits.append(logits.float().cpu())
        all_labels.append(labels)
    return torch.cat(all_logits), torch.cat(all_labels)


def evaluate(model: nn.Module, loader: DataLoader, device: torch.device, use_amp: bool = False) -> dict:
    """Mean loss, accuracy, per-class recall and confusion matrix (rows: true class, columns: prediction)."""
    logits, labels = predict(model, loader, device, use_amp)
    num_classes = logits.shape[1]
    predictions = logits.argmax(dim=1)
    confusion = torch.bincount(labels * num_classes + predictions, minlength=num_classes**2)
    confusion = confusion.view(num_classes, num_classes)
    recall = confusion.diag() / confusion.sum(dim=1).clamp(min=1)
    return {
        "loss": float(nn.functional.cross_entropy(logits, labels)),
        "accuracy": float((predictions == labels).float().mean()),
        "per_class_recall": [round(float(value), 4) for value in recall],
        "confusion": confusion.tolist(),
    }


def fit(
    model: nn.Module,
    loaders: dict[str, DataLoader],
    epochs: int,
    lr: float,
    device: torch.device,
    weight_decay: float = 1e-4,
    use_amp: bool = False,
    log_prefix: str = "",
) -> tuple[list[dict], int]:
    """Train with AdamW and a cosine learning-rate schedule, keeping the best validation epoch.

    The model ends with the weights of the epoch that had the best validation accuracy. Returns the
    per-epoch history and that epoch. Used for the initial training and to fine-tune pruned models.
    """
    model.to(device)
    optimizer = torch.optim.AdamW(model.parameters(), lr=lr, weight_decay=weight_decay)
    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=epochs)
    history, best_epoch, best_accuracy, best_state = [], 0, -1.0, None
    for epoch in range(1, epochs + 1):
        start = time.perf_counter()
        train_loss, train_accuracy = train_one_epoch(model, loaders["train"], optimizer, device, use_amp)
        val = evaluate(model, loaders["val"], device, use_amp)
        scheduler.step()
        history.append(
            {
                "epoch": epoch,
                "train_loss": train_loss,
                "train_accuracy": train_accuracy,
                "val_loss": val["loss"],
                "val_accuracy": val["accuracy"],
            }
        )
        print(
            f"{log_prefix}epoch {epoch:2d}/{epochs} | train loss {train_loss:.4f} acc {train_accuracy:.4f} "
            f"| val loss {val['loss']:.4f} acc {val['accuracy']:.4f} | {time.perf_counter() - start:.0f}s"
        )
        if val["accuracy"] > best_accuracy:
            best_epoch, best_accuracy = epoch, val["accuracy"]
            best_state = copy.deepcopy(model.state_dict())
    model.load_state_dict(best_state)
    print(f"{log_prefix}best epoch {best_epoch} (val acc {best_accuracy:.4f})")
    return history, best_epoch


def save_report(report: dict, output_dir: str | Path) -> Path:
    """Write ``report.json`` (configuration, preprocessing, metrics) to ``output_dir``."""
    path = Path(output_dir) / "report.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    return path


def save_model(model: nn.Module, report: dict, output_dir: str | Path) -> Path:
    """Write the weights (``model.pt``, a state_dict) and ``report.json`` to ``output_dir``."""
    path = Path(output_dir) / "model.pt"
    path.parent.mkdir(parents=True, exist_ok=True)
    torch.save({key: value.detach().cpu() for key, value in model.state_dict().items()}, path)
    save_report(report, output_dir)
    return path


def load_model(output_dir: str | Path, device: torch.device) -> tuple[nn.Module, dict]:
    """Rebuild the saved model the way MANOLO does: ``build_model(**model_kwargs)`` + strict state_dict load."""
    report = json.loads((Path(output_dir) / "report.json").read_text(encoding="utf-8"))
    model = build_model(**report["model_kwargs"])
    model.load_state_dict(torch.load(Path(output_dir) / "model.pt", map_location="cpu", weights_only=True))
    return model.to(device).eval(), report


# =============================================================================
# Results
# =============================================================================


def plot_history(history: list[dict], best_epoch: int | None = None) -> None:
    """Loss and accuracy per epoch, for the training and validation splits."""
    epochs = [row["epoch"] for row in history]
    fig, axes = plt.subplots(1, 2, figsize=(11, 3.5))
    for ax, metric in zip(axes, ("loss", "accuracy")):
        ax.plot(epochs, [row[f"train_{metric}"] for row in history], label="train")
        ax.plot(epochs, [row[f"val_{metric}"] for row in history], label="val")
        if best_epoch:
            ax.axvline(best_epoch, color="grey", linestyle=":", label="best epoch")
        ax.set(xlabel="epoch", ylabel=metric)
        ax.legend()
    plt.tight_layout()
    plt.show()


def plot_confusion(confusion: list[list[int]], classes: list[str], title: str = "Confusion matrix") -> None:
    """Confusion matrix with counts; rows are the true classes, columns the predictions."""
    matrix = np.asarray(confusion)
    size = 1.0 * len(classes) + 2.5
    fig, ax = plt.subplots(figsize=(size, size))
    ax.imshow(matrix, cmap="Blues")
    ax.set_xticks(range(len(classes)), classes, rotation=45, ha="right")
    ax.set_yticks(range(len(classes)), classes)
    ax.set(xlabel="predicted", ylabel="true", title=title)
    for row in range(matrix.shape[0]):
        for col in range(matrix.shape[1]):
            color = "white" if matrix[row, col] > matrix.max() / 2 else "black"
            ax.text(col, row, matrix[row, col], ha="center", va="center", color=color)
    plt.tight_layout()
    plt.show()


# =============================================================================
# XAI
# =============================================================================


def sample_per_class(dataset: datasets.ImageFolder, per_class: int, seed: int = 42) -> list[int]:
    """Indices of ``per_class`` random images of each class, grouped by class."""
    rng = random.Random(seed)
    indices = []
    for label in range(len(dataset.classes)):
        candidates = [index for index, target in enumerate(dataset.targets) if target == label]
        indices += rng.sample(candidates, min(per_class, len(candidates)))
    return indices


def plot_explanations(
    images: torch.Tensor,
    heatmaps: np.ndarray,
    labels: list[int],
    probabilities: torch.Tensor,
    classes: list[str],
    mean: list[float],
    std: list[float],
    title: str = "",
) -> None:
    """Images on the top row, heatmaps overlaid below; the prediction is green if correct, red if wrong."""
    count = len(images)
    fig, axes = plt.subplots(2, count, figsize=(2 * count, 4.6), squeeze=False)
    for col in range(count):
        picture = to_display(images[col], mean, std)
        predicted = int(probabilities[col].argmax())
        axes[0, col].imshow(picture)
        axes[0, col].set_title(f"true: {classes[labels[col]]}", fontsize=8)
        axes[1, col].imshow(show_cam_on_image(picture, heatmaps[col], use_rgb=True))
        axes[1, col].set_title(
            f"pred: {classes[predicted]} ({float(probabilities[col][predicted]):.2f})",
            fontsize=8,
            color="green" if predicted == labels[col] else "red",
        )
        for ax in axes[:, col]:
            ax.axis("off")
    fig.suptitle(title)
    plt.tight_layout()
    plt.show()


# =============================================================================
# Compression
# =============================================================================


def state_dict_size_mb(model: nn.Module) -> float:
    """Size of the serialised state_dict, i.e. of the saved ``.pt`` file, in MB."""
    buffer = io.BytesIO()
    torch.save(model.state_dict(), buffer)
    return buffer.getbuffer().nbytes / 1e6


def prunable_weights(model: nn.Module) -> list[tuple[nn.Module, str]]:
    """``(module, "weight")`` for every convolution and linear layer: the input of the pruning functions."""
    return [(module, "weight") for module in model.modules() if isinstance(module, (nn.Conv2d, nn.Linear))]


def weight_sparsity(model: nn.Module) -> float:
    """Fraction of convolution and linear weights that are exactly zero."""
    weights = [getattr(module, name) for module, name in prunable_weights(model)]
    return sum(int((weight == 0).sum()) for weight in weights) / sum(weight.numel() for weight in weights)


@torch.no_grad()
def cpu_latency_ms(model: nn.Module, example: torch.Tensor, runs: int = 10) -> float:
    """Mean CPU time of one forward pass over the ``example`` batch, in milliseconds."""
    on_gpu = any(parameter.is_cuda for parameter in model.parameters())
    model = (copy.deepcopy(model).cpu() if on_gpu else model).eval()
    example = example.cpu()
    model(example)  # warm-up
    start = time.perf_counter()
    for _ in range(runs):
        model(example)
    return (time.perf_counter() - start) * 1000 / runs


def quantization_engine() -> str:
    """First int8 backend this torch build supports (x86 and fbgemm on Linux, onednn on Windows)."""
    supported = torch.backends.quantized.supported_engines
    for engine in ("x86", "fbgemm", "onednn", "qnnpack"):
        if engine in supported:
            return engine
    raise RuntimeError(f"This torch build has no int8 engine: {supported}")


def quantizable_copy(model: nn.Module) -> nn.Module:
    """Float CPU copy of the ResNet-18 of ``architecture.py`` as torchvision's quantizable variant.

    Same layers plus QuantStub/DeQuantStub and quantization-friendly residual additions, so the trained
    weights load unchanged. The first convolution is rebuilt for models with ``in_channels != 3``.
    """
    quantizable = qmodels.resnet18(weights=None, quantize=False, num_classes=model.fc.out_features)
    if model.conv1.in_channels != 3:
        quantizable.conv1 = nn.Conv2d(model.conv1.in_channels, 64, kernel_size=7, stride=2, padding=3, bias=False)
    quantizable.load_state_dict(model.state_dict())
    return quantizable.eval()


@torch.no_grad()
def calibrate(model: nn.Module, loader: DataLoader, num_batches: int) -> None:
    """Run ``num_batches`` batches through a prepared model (on the CPU) so its observers record value ranges."""
    model.eval()
    for batch, (images, _) in enumerate(loader):
        if batch == num_batches:
            break
        model(images.cpu())


# =============================================================================
# MANOLO
# =============================================================================


def _balanced_subset(targets: list[int], size: int | None, seed: int) -> list[int]:
    """Class-balanced random indices (as balanced as the data allows), shuffled so batches mix classes."""
    rng = random.Random(seed)
    if size is None or size >= len(targets):
        indices = list(range(len(targets)))
        rng.shuffle(indices)
        return indices
    by_class: dict[int, list[int]] = {}
    for index, target in enumerate(targets):
        by_class.setdefault(target, []).append(index)
    chosen: list[int] = []
    for members in by_class.values():
        chosen += rng.sample(members, min(size // len(by_class), len(members)))
    taken = set(chosen)
    remaining = [index for index in range(len(targets)) if index not in taken]
    chosen += rng.sample(remaining, size - len(chosen))
    rng.shuffle(chosen)
    return chosen


def export_tensor_dataset(
    train_dataset: datasets.ImageFolder,
    test_dataset: datasets.ImageFolder,
    path: str | Path,
    max_train: int | None = None,
    max_test: int | None = None,
    seed: int = 42,
) -> dict[str, int]:
    """Save MANOLO's tensor-dict dataset: ``{"train": {"images", "labels"}, "test": {"images", "labels"}}``.

    Images are stored exactly as the model receives them (resized, normalised float32), so pass datasets
    built without augmentation. Each split is a class-balanced random subset of at most ``max_*`` images.
    """
    tensors, counts = {}, {}
    for split, dataset, limit in (("train", train_dataset, max_train), ("test", test_dataset, max_test)):
        indices = _balanced_subset(dataset.targets, limit, seed)
        images = torch.stack([dataset[index][0] for index in indices]).float().contiguous()
        labels = torch.tensor([dataset.targets[index] for index in indices], dtype=torch.long)
        tensors[split] = {"images": images, "labels": labels}
        counts[split] = len(indices)
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    torch.save(tensors, path)
    return counts
