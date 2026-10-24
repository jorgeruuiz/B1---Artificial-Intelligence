# Source coverage

References throughout the notes count PDF pages from 1, including title slides. Repeated reveal slides and image-only illustrations are consolidated into explanations of their underlying concept, rather than repeated as separate sections.

| Supplied deck | Pages | Coverage |
| --- | ---: | --- |
| 0. Presentation | 15 | Course scope in README; administrative details are not repeated as study theory. |
| 0.1. Math background | 11 | Topic 0: probability, random variables, Gaussian identities, information theory, MLE and Lagrange regularization. |
| 1.1. Fundamentals | 45 | Topic 1: learning settings, inductive bias, data, methodology, splits and k-NN. Applications illustrate the concepts. |
| 1.2. Shallow Learning | 85 | Topic 1: regression, regularization, optimization, robust fitting, metrics, classification, PCA, clustering, SVM, kernels, CART and ensembles. Neural-network previews lead into Topic 3. |
| 1.3. Bayesian Learning | 58 | Topic 1: uncertainty, Gaussian regression posterior/predictive, basis functions, GPs, kernels, ARD, marginal likelihood, Cholesky, and introductory extensions. |
| 2.1. Introduction to Reinforcement Learning | 16 | Topic 2: interaction, reward, gridworld, policy, model, value, planning and partial-observation introduction. |
| 2.2. Markov decision processes | 26 | Topic 2: Markov states, returns, values, Bellman expectation/optimality and dynamic programming. |
| 2.3. Q-learning | 48 | Topic 2: model-based/model-free, incremental MC, TD, exploration, regret, SARSA/Q-learning, features, worked Pacman calculation and deadly triad. |
| 2.4. Policy Search | 19 | Topic 2: policy objectives, trajectory likelihood, gradients, softmax policy, REINFORCE, actor–critic and optimization alternatives. |
| 3.1. Introduction to Deep Learning | 41 | Topic 3: definitions, applications, data and representation-learning pipeline. |
| 3.2. Shallow NN | 51 | Topic 3: ReLU construction, shapes/counts, approximation theorem, activation regions and terminology. |
| 3.3. Deep Learning Fundamentals | 44 | Topic 3: deep composition, capacity, scores, losses, SGD, momentum, Adam and hyperparameters. References aligned to the current deck. |
| 3.4. Deep Learning Fundamentals II | 53 | Topic 3: scalar/matrix backprop, autograd, initialization, normalization, explicit/implicit regularization, dropout, augmentation and double descent. |
| 4.1. CNNs | 111 | Topic 4: convolution, sizes/counts, receptive fields, pooling/upsampling, architectures, expanded residual blocks/normalization, transfer learning, diagnostics, task extensions and exercises. |
| 5.1. Sequence Models | 34 | Topic 5, section 5.1: RNNs, shapes/counts, BPTT, clipping/truncation, LSTM/GRU, variants, TCNs, seq2seq, teacher forcing and attention. |
| 5.1. Extra Material | 7 | Topic 5, section 5.1: gate equations, sizes/counts, parameters versus states, and the actual p. 7 tiny-LSTM update. |
| 5.2. Transformers | 43 | Topic 5, section 5.2: Q/K/V, arithmetic/shapes/counts, positions, tokenization/embeddings, blocks, normalization, families/masks/cross-attention, efficiency, ViT and the p. 42 A/B exercise. |
| 5.3. Foundation models | 28 | Topic 5, section 5.3: broad pretraining/adaptation, supervision stages, MoE/storage, language families, CLIP, DINOv2, SAM, generation pipelines and limitations. |
| 5.4. Unsupervised learning | 38 | Topic 5, section 5.4: supervision distinctions, PCA/t-SNE, clustering/LDA, proxy tasks, contrastive learning, BYOL, SuperPoint and semi-supervised extensions. |
| 5.5. Generative Models | 26 | Topic 5, section 5.5: generative/discriminative distinctions, AE/VAE, reconstruction/KL, GAN objectives, collapse, CycleGAN, diffusion, conditioning and course hierarchy. |
| X.1 / X.2 (initially supplied) | 41 / 51 | Extracted text identical to 3.1 / 3.2; no separate content. |

## Clarifications made in context

- Gaussian conditioning uses subtraction in conditional covariance; Gaussian mixtures need not be Gaussian; linear combinations must include covariance terms where relevant.
- Natural-log information is measured in nats; realized posterior-versus-prior KL is distinct from a particular entropy reduction; their expected relation is mutual information.
- MLE unbiasedness and asymptotic statements need conditions and correct scaling.
- Ridge loss scaling, logistic uniqueness/separation, PCA matrix orientation, F-beta weighting, and multiclass versus one-vs-rest accuracy are made explicit.
- RL rewards are indexed consistently after actions. Terminal continuation is zero, but the entering reward remains. Q-learning does not need a sampled successor action; convergence conditions and the deadly triad are qualified.
- Approximate Q-learning differentiates only the current prediction (semi-gradient); the slide Pacman weights are calculated before rounding.
- Neural-network approximation results are existence results; activation regions live in input space. Backpropagation is separated from optimization. Dropout and batch-normalization training/inference distinctions are explained.
- Convolution output-size calculations include floor and dilation; the 240-by-240 exercise gives distinct answers for stated padding assumptions. Historical model examples are kept as slide examples.
- Residual identity arguments require compatible shapes and activations. BN trainable parameters are separated from running statistics; evaluation mode differs from disabling gradients.
- RNN/LSTM counts state bias conventions and distinguish shared parameters from computed states. The tiny LSTM uses the teacher's rounded nonlinearities and identifies its output scores as logits.
- Attention matrix conventions are explicit. The unscaled p. 11 example and divide-by-three p. 42 shortcut are distinguished from scaled-softmax attention. The A/B comparison states the row-vector convention and toy semantic-axis assumption.
- Causal masking prevents future-token leakage but does not remove exposure bias. Encoders can still mask padding. Layer norm does not use BN's cross-sample running statistics.
- Foundation models are distinguished from architectures. CLIP similarities are not calibrated probabilities; CLIP alone does not decode images. Transfer learning and reward optimization do not guarantee universal performance or factual correctness.
- PCA preserves variance under a linear squared-error criterion, not an arbitrary percentage of meaning or accuracy. t-SNE emphasizes local relationships; standard t-SNE has no simple reusable fitted linear map. LDA means Latent Dirichlet Allocation here.
- Self-supervision has targets and losses. BYOL uses no explicit negatives; pseudo-labels are uncertain predictions.
- Deterministic autoencoders can decode arbitrary latent vectors, but may decode them poorly. VAE variance versus standard deviation is explicit. GAN collapse concerns diversity; discriminator uncertainty alone does not prove success.
- Diffusion training can directly construct noisy inputs at sampled timesteps; generation usually iterates a reverse process. Text encoding, denoising and image decoding are distinct components.

## Completion and printing

The explanatory notes cover every teaching deck currently supplied in `Lecture Slides`, through 5.5. Administrative, demonstration and bibliography slides are identified or consolidated rather than copied as theory. The earlier mathematical-background volume remains available; its exclusion from the practice-question bank is unchanged.

The notes are grouped into one PDF per main course topic, 0–5. All material from 5.1–5.5, including the LSTM extra deck, is contained in Topic 5 with a unified contents list and continuous pagination. Expanded CNN material is part of Topic 4. Superseded separate chapter files are archived rather than listed as primary volumes. Page references in Topics 3 and 4 were aligned to current slide versions.

No lab solutions or teacher files were edited. The lab references connect the supplied theory to the named practical tasks.
