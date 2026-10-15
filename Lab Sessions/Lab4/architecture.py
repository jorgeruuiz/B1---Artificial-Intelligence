"""ResNet-18 architecture for the Innovation Lab workshop.

MANOLO contract (same as demo/ceadar/demo_assets/architecture.py): the file
exposes ``build_model(**model_kwargs)`` (aliased as ``Model``) and the trained
weights are a ``state_dict`` that loads into ``build_model(**model_kwargs)``.

Register the model with the ``model_kwargs`` saved in the training report,
``{"num_classes": N, "in_channels": C}``.
"""

import torch.nn as nn
from torchvision import models


def build_model(num_classes: int = 2, in_channels: int = 3, **kwargs) -> nn.Module:
    """Randomly initialised torchvision ResNet-18 for ``in_channels`` inputs and ``num_classes`` outputs.

    With ``in_channels != 3`` (e.g. 1 for grayscale images) the first convolution is rebuilt for that
    number of channels. Extra keyword arguments are accepted and ignored, as in the CeADAR demo.
    """
    model = models.resnet18(weights=None, num_classes=num_classes)
    if in_channels != 3:
        model.conv1 = nn.Conv2d(in_channels, 64, kernel_size=7, stride=2, padding=3, bias=False)
        nn.init.kaiming_normal_(model.conv1.weight, mode="fan_out", nonlinearity="relu")
    return model


Model = build_model
