# Artificial Intelligence — exam slide index
**PDF page numbers start at 1 and include title pages.** They may differ from printed slide numbers, especially in 1.2 and 1.3. This index points to the original slide PDFs, not the study-note PDFs.
Grouped by main topic 1–5, with exact slide-deck titles beneath each topic. 5.1E means the separate LSTM extra-material PDF. The Lab 4 briefing appears as a supplement.
## Quick lookup

| Find | Slide PDF and pages |
| --- | --- |
| Training / validation / test; cross-validation | [1.1: 31-32, 41](../Lecture%20Slides/1.1.%20Fundamentals.pdf#page=31); [1.2: 21-25](../Lecture%20Slides/1.2.%20Shallow%20Learning.pdf#page=21) |
| Regression errors; classification metrics / confusion matrix | [1.2: 40, 60-67](../Lecture%20Slides/1.2.%20Shallow%20Learning.pdf#page=40) |
| Bayesian posterior / prediction; Gaussian-process equations | [1.3: 13-14, 51-52](../Lecture%20Slides/1.3.%20Bayesian%20Learning.pdf#page=13) |
| Discounted returns and Bellman equations | [2.2: 8-19](../Lecture%20Slides/2.2.%20Markov%20decision%20processes.pdf#page=8) |
| MC / TD update; SARSA versus Q-learning | [2.3: 23-24, 29, 35-38](../Lecture%20Slides/2.3.%20Q-learning.pdf#page=23) |
| Dense-network dimensions and parameter counts | [3.2: 39-42](../Lecture%20Slides/3.2.%20Shallow%20NN.pdf#page=39); [3.3: 8-10](../Lecture%20Slides/3.3.%20Deep%20Learning%20Fundamentals.pdf#page=8) |
| Hinge / softmax loss; backpropagation exercise | [3.3: 23-26](../Lecture%20Slides/3.3.%20Deep%20Learning%20Fundamentals.pdf#page=23); [3.4: 8-17](../Lecture%20Slides/3.4.%20Deep%20Learning%20Fundamentals%20II.pdf#page=8) |
| Convolution output size, parameters and receptive field | [4.1: 17, 20-23, 30, 106](../Lecture%20Slides/4.1.%20CNNs.pdf#page=17) |
| Residuals; BN count and train/eval; normalization variants | [4.1: 52-59, 62](../Lecture%20Slides/4.1.%20CNNs.pdf#page=52) |
| LSTM dimensions, parameter counts and one-step update | [5.1E: 5-7](../Lecture%20Slides/5.1.%20Extra%20Material.pdf#page=5) |
| Attention calculation, shapes and classroom A/B exercise | [5.2: 11-13, 42](../Lecture%20Slides/5.2.%20Transformers.pdf#page=11) |
| Causal mask, cross-attention, KV cache and image patches | [5.2: 31-40](../Lecture%20Slides/5.2.%20Transformers.pdf#page=31) |
| PCA / t-SNE; k-means / topic mixtures | [5.4: 9-22](../Lecture%20Slides/5.4.%20Unsupervised%20learning.pdf#page=9) |
| Pretraining / SFT / RL; CLIP, DINOv2 and SAM | [5.3: 14, 19-22](../Lecture%20Slides/5.3.%20Foundation%20models.pdf#page=14) |
| AE / VAE / GAN / diffusion: meanings and comparisons | [5.5: 7-13, 17-22](../Lecture%20Slides/5.5.%20Generative%20Models.pdf#page=7) |

## 1. Learning fundamentals, shallow and Bayesian learning

### 1.1. Fundamentals.pdf

| Concept / method / exercise | PDF pages |
| --- | --- |
| Machine learning, models, assumptions, inductive bias; No Free Lunch | [4-6](../Lecture%20Slides/1.1.%20Fundamentals.pdf#page=4) |
| Supervised learning; regression versus classification | [10-14](../Lecture%20Slides/1.1.%20Fundamentals.pdf#page=10) |
| Unsupervised learning; dimensionality reduction and clustering | [15-17](../Lecture%20Slides/1.1.%20Fundamentals.pdf#page=15) |
| Reinforcement learning and combinations of learning strategies | [18-23](../Lecture%20Slides/1.1.%20Fundamentals.pdf#page=18) |
| Abstraction, partial information; correlation versus causation | [24-26](../Lecture%20Slides/1.1.%20Fundamentals.pdf#page=24) |
| Data quality, sampling bias, Big Data limitations, feature choice | [27-30](../Lecture%20Slides/1.1.%20Fundamentals.pdf#page=27) |
| Training, validation and test sets; model selection and evaluation | [31-32, 41](../Lecture%20Slides/1.1.%20Fundamentals.pdf#page=31) |
| k-nearest neighbours (k-NN): prediction, distance and choice of k | [33-34, 36](../Lecture%20Slides/1.1.%20Fundamentals.pdf#page=33) |
| k-NN examples: dataset size, splits, digits and image difficulty | [37-39](../Lecture%20Slides/1.1.%20Fundamentals.pdf#page=37) |
| ML workflow: frame problem, explore data, compare and tune models | [40-44](../Lecture%20Slides/1.1.%20Fundamentals.pdf#page=40) |

### 1.2. Shallow Learning.pdf

| Concept / method / exercise | PDF pages |
| --- | --- |
| Linear regression, Gaussian noise, likelihood and least squares | [4-8](../Lecture%20Slides/1.2.%20Shallow%20Learning.pdf#page=4) |
| Negative log-likelihood; gradient descent and stochastic updates | [9, 26-31](../Lecture%20Slides/1.2.%20Shallow%20Learning.pdf#page=9) |
| Basis-function expansion; polynomial regression | [11-12](../Lecture%20Slides/1.2.%20Shallow%20Learning.pdf#page=11) |
| Overfitting, bias-variance trade-off and model complexity | [13-15](../Lecture%20Slides/1.2.%20Shallow%20Learning.pdf#page=13) |
| Ridge / L2 regularization; Gaussian prior and MAP interpretation | [16-18](../Lecture%20Slides/1.2.%20Shallow%20Learning.pdf#page=16) |
| Lasso / L1 regularization; sparsity and coefficients set to zero | [19-20](../Lecture%20Slides/1.2.%20Shallow%20Learning.pdf#page=19) |
| Hyperparameters, validation splits and cross-validation | [21-25](../Lecture%20Slides/1.2.%20Shallow%20Learning.pdf#page=21) |
| Learning rate; batch GD versus SGD; mini-batches and momentum | [27-32](../Lecture%20Slides/1.2.%20Shallow%20Learning.pdf#page=27) |
| Other optimization algorithms: overview | [33](../Lecture%20Slides/1.2.%20Shallow%20Learning.pdf#page=33) |
| Outliers; robust regression, L1/Laplace, Huber and RANSAC | [34-39](../Lecture%20Slides/1.2.%20Shallow%20Learning.pdf#page=34) |
| Regression metrics: MAE, MSE, RMSE, median error and R-squared | [40](../Lecture%20Slides/1.2.%20Shallow%20Learning.pdf#page=40) |
| Bayesian ridge and ARD: regression comparison | [42](../Lecture%20Slides/1.2.%20Shallow%20Learning.pdf#page=42) |
| Feature scaling / standardization and its importance | [43](../Lecture%20Slides/1.2.%20Shallow%20Learning.pdf#page=43) |
| Linear classification, decision boundary, perceptron and sigmoid | [45-48](../Lecture%20Slides/1.2.%20Shallow%20Learning.pdf#page=45) |
| Logistic regression: Bernoulli likelihood, cross-entropy and training | [49-53](../Lecture%20Slides/1.2.%20Shallow%20Learning.pdf#page=49) |
| Multiclass / multinomial logistic regression and softmax | [54-56](../Lecture%20Slides/1.2.%20Shallow%20Learning.pdf#page=54) |
| MLP preview; hidden layers and nonlinear activations | [57-59](../Lecture%20Slides/1.2.%20Shallow%20Learning.pdf#page=57) |
| True/false positives and negatives; TP, TN, FP, FN | [60](../Lecture%20Slides/1.2.%20Shallow%20Learning.pdf#page=60) |
| Accuracy, precision and recall: definitions and interpretation | [61-62](../Lecture%20Slides/1.2.%20Shallow%20Learning.pdf#page=61) |
| Classification threshold; precision-recall trade-off and PR curve | [63-64](../Lecture%20Slides/1.2.%20Shallow%20Learning.pdf#page=63) |
| F1 / F-beta; confusion-matrix orientation | [65](../Lecture%20Slides/1.2.%20Shallow%20Learning.pdf#page=65) |
| Read a multiclass confusion matrix; per-class and aggregate metrics | [66-67](../Lecture%20Slides/1.2.%20Shallow%20Learning.pdf#page=66) |
| PCA; dimensionality reduction and its effect on a classifier | [68-70](../Lecture%20Slides/1.2.%20Shallow%20Learning.pdf#page=68) |
| K-means clustering | [71](../Lecture%20Slides/1.2.%20Shallow%20Learning.pdf#page=71) |
| SVM: separating hyperplanes, maximum margin and support vectors | [72-75](../Lecture%20Slides/1.2.%20Shallow%20Learning.pdf#page=72) |
| Soft-margin / non-separable SVM | [76](../Lecture%20Slides/1.2.%20Shallow%20Learning.pdf#page=76) |
| SVM optimization: Lagrange formulation | [77](../Lecture%20Slides/1.2.%20Shallow%20Learning.pdf#page=77) |
| Nonlinear feature maps and the kernel trick | [78-79](../Lecture%20Slides/1.2.%20Shallow%20Learning.pdf#page=78) |
| Classification and regression trees (CART) | [81](../Lecture%20Slides/1.2.%20Shallow%20Learning.pdf#page=81) |
| Ensembles; bootstrap sampling, bagging and random forests | [82-83](../Lecture%20Slides/1.2.%20Shallow%20Learning.pdf#page=82) |
| Boosting; AdaBoost and gradient boosting | [84](../Lecture%20Slides/1.2.%20Shallow%20Learning.pdf#page=84) |

### 1.3. Bayesian Learning.pdf

| Concept / method / exercise | PDF pages |
| --- | --- |
| Bayesian reasoning; prior, likelihood, posterior and Bayes rule | [4-6](../Lecture%20Slides/1.3.%20Bayesian%20Learning.pdf#page=4) |
| Bayesian prediction versus ML/MAP point estimates | [7-8](../Lecture%20Slides/1.3.%20Bayesian%20Learning.pdf#page=7) |
| Bayesian linear regression; Gaussian prior, likelihood and posterior | [9-13](../Lecture%20Slides/1.3.%20Bayesian%20Learning.pdf#page=9) |
| Multivariate Gaussians; covariance, marginals and conditioning | [10-12](../Lecture%20Slides/1.3.%20Bayesian%20Learning.pdf#page=10) |
| Posterior predictive distribution; prediction uncertainty | [14](../Lecture%20Slides/1.3.%20Bayesian%20Learning.pdf#page=14) |
| Regression in feature space; weight-space versus function-space views | [15-20](../Lecture%20Slides/1.3.%20Bayesian%20Learning.pdf#page=15) |
| Polynomial, Fourier, bell, Heaviside and exponential basis functions | [21-27](../Lecture%20Slides/1.3.%20Bayesian%20Learning.pdf#page=21) |
| Learned/many features; kernel trick and transition to Gaussian processes | [28-30](../Lecture%20Slides/1.3.%20Bayesian%20Learning.pdf#page=28) |
| GP definition, joint distributions, correlation and conditioning | [31-35](../Lecture%20Slides/1.3.%20Bayesian%20Learning.pdf#page=31) |
| Nonparametric models; training data versus fixed parameter vectors | [36](../Lecture%20Slides/1.3.%20Bayesian%20Learning.pdf#page=36) |
| Kernel families: squared exponential, Matern, linear, periodic, neural | [37-43](../Lecture%20Slides/1.3.%20Bayesian%20Learning.pdf#page=37) |
| Combining kernels; linear plus periodic structure | [44-45](../Lecture%20Slides/1.3.%20Bayesian%20Learning.pdf#page=44) |
| Kernel hyperparameters: lengthscale, signal variance and noise | [46-47](../Lecture%20Slides/1.3.%20Bayesian%20Learning.pdf#page=46) |
| Automatic Relevance Determination (ARD); per-dimension lengthscales | [48](../Lecture%20Slides/1.3.%20Bayesian%20Learning.pdf#page=48) |
| Hyperparameter learning; marginal likelihood and complexity/fit trade-off | [49-50](../Lecture%20Slides/1.3.%20Bayesian%20Learning.pdf#page=49) |
| GP predictive mean and variance; regression summary equations | [51](../Lecture%20Slides/1.3.%20Bayesian%20Learning.pdf#page=51) |
| Cholesky-based GP computation | [52](../Lecture%20Slides/1.3.%20Bayesian%20Learning.pdf#page=52) |
| Nonzero means, hierarchical Bayes, non-Gaussian likelihoods and GP extensions | [53-56](../Lecture%20Slides/1.3.%20Bayesian%20Learning.pdf#page=53) |

## 2. Reinforcement learning

### 2.1. Introduction to Reinforcement Learning.pdf

| Concept / method / exercise | PDF pages |
| --- | --- |
| What RL is; agent interaction versus supervised/unsupervised learning | [2-3](../Lecture%20Slides/2.1.%20Introduction%20to%20Reinforcement%20Learning.pdf#page=2) |
| Rewards, costs and the reward hypothesis | [5-6](../Lecture%20Slides/2.1.%20Introduction%20to%20Reinforcement%20Learning.pdf#page=5) |
| Agent-environment loop; deterministic/stochastic gridworld | [7-9](../Lecture%20Slides/2.1.%20Introduction%20to%20Reinforcement%20Learning.pdf#page=7) |
| Partial observation and generalized decision-process introduction | [10](../Lecture%20Slides/2.1.%20Introduction%20to%20Reinforcement%20Learning.pdf#page=10) |
| Transition/reward model, policy and value function | [11-13](../Lecture%20Slides/2.1.%20Introduction%20to%20Reinforcement%20Learning.pdf#page=11) |
| Planning with a known model versus learning through interaction | [14-16](../Lecture%20Slides/2.1.%20Introduction%20to%20Reinforcement%20Learning.pdf#page=14) |

### 2.2. Markov decision processes.pdf

| Concept / method / exercise | PDF pages |
| --- | --- |
| Markov property; MDP tuple: states, actions, transitions, rewards, discount | [2-3](../Lecture%20Slides/2.2.%20Markov%20decision%20processes.pdf#page=2) |
| Racing example and search-tree representation | [4-5](../Lecture%20Slides/2.2.%20Markov%20decision%20processes.pdf#page=4) |
| Policy: probability of an action given a state | [6](../Lecture%20Slides/2.2.%20Markov%20decision%20processes.pdf#page=6) |
| Return, discount factor gamma, finite/infinite horizon; discounting quiz | [7-10](../Lecture%20Slides/2.2.%20Markov%20decision%20processes.pdf#page=7) |
| State value V and action value Q | [11](../Lecture%20Slides/2.2.%20Markov%20decision%20processes.pdf#page=11) |
| Bellman expectation equations; recursive value evaluation | [12-15](../Lecture%20Slides/2.2.%20Markov%20decision%20processes.pdf#page=12) |
| Optimal V/Q functions and optimal policy | [16-17](../Lecture%20Slides/2.2.%20Markov%20decision%20processes.pdf#page=16) |
| Bellman optimality equations; maximization over actions | [18-19](../Lecture%20Slides/2.2.%20Markov%20decision%20processes.pdf#page=18) |
| Dynamic programming: why the model is required | [20](../Lecture%20Slides/2.2.%20Markov%20decision%20processes.pdf#page=20) |
| Iterative policy evaluation and stopping criterion | [21-22](../Lecture%20Slides/2.2.%20Markov%20decision%20processes.pdf#page=21) |
| Value iteration and greedy action selection | [23-24](../Lecture%20Slides/2.2.%20Markov%20decision%20processes.pdf#page=23) |

### 2.3. Q-learning.pdf

| Concept / method / exercise | PDF pages |
| --- | --- |
| MDP recap and unknown transition/reward models | [3-5](../Lecture%20Slides/2.3.%20Q-learning.pdf#page=3) |
| Model-based versus model-free learning; passive prediction versus control | [6-10](../Lecture%20Slides/2.3.%20Q-learning.pdf#page=6) |
| Monte Carlo policy evaluation from complete episodes | [11-13](../Lecture%20Slides/2.3.%20Q-learning.pdf#page=11) |
| Incremental mean and incremental Monte Carlo update | [14-15](../Lecture%20Slides/2.3.%20Q-learning.pdf#page=14) |
| MC limitations; bootstrapping and temporal-difference learning | [16-20](../Lecture%20Slides/2.3.%20Q-learning.pdf#page=16) |
| Constant learning rates and forgetting old observations | [21](../Lecture%20Slides/2.3.%20Q-learning.pdf#page=21) |
| MC versus TD versus dynamic programming; update equations | [22-26](../Lecture%20Slides/2.3.%20Q-learning.pdf#page=22) |
| Monte Carlo value-update formula | [23](../Lecture%20Slides/2.3.%20Q-learning.pdf#page=23) |
| TD(0) value update and TD error | [24](../Lecture%20Slides/2.3.%20Q-learning.pdf#page=24) |
| Control and Q-values; greedy action selection without a transition model | [27-28](../Lecture%20Slides/2.3.%20Q-learning.pdf#page=27) |
| SARSA update: sampled next action | [29](../Lecture%20Slides/2.3.%20Q-learning.pdf#page=29) |
| Exploration versus exploitation; epsilon-greedy and regret | [30-33](../Lecture%20Slides/2.3.%20Q-learning.pdf#page=30) |
| Q-learning target, update formula and algorithm | [34-36](../Lecture%20Slides/2.3.%20Q-learning.pdf#page=34) |
| On-policy versus off-policy; SARSA versus Q-learning | [37-38](../Lecture%20Slides/2.3.%20Q-learning.pdf#page=37) |
| Large state spaces, features and linear value-function approximation | [39-42](../Lecture%20Slides/2.3.%20Q-learning.pdf#page=39) |
| Approximate Q-learning; TD-error-based weight updates | [43-44](../Lecture%20Slides/2.3.%20Q-learning.pdf#page=43) |
| Worked Pacman feature/Q-value/weight-update example | [45](../Lecture%20Slides/2.3.%20Q-learning.pdf#page=45) |
| Online least squares / gradient interpretation | [46](../Lecture%20Slides/2.3.%20Q-learning.pdf#page=46) |
| Deadly triad: function approximation, bootstrapping and off-policy learning | [47](../Lecture%20Slides/2.3.%20Q-learning.pdf#page=47) |

### 2.4. Policy Search.pdf

| Concept / method / exercise | PDF pages |
| --- | --- |
| Policy-based versus value-based RL; advantages and limitations | [2-3](../Lecture%20Slides/2.4.%20Policy%20Search.pdf#page=2) |
| Trajectory probability and its factorization | [4-5](../Lecture%20Slides/2.4.%20Policy%20Search.pdf#page=4) |
| Expected-return objective; gradient ascent on policy parameters | [6-7](../Lecture%20Slides/2.4.%20Policy%20Search.pdf#page=6) |
| Policy-gradient derivation and sampled update | [8-10](../Lecture%20Slides/2.4.%20Policy%20Search.pdf#page=8) |
| Softmax policy over action scores | [11](../Lecture%20Slides/2.4.%20Policy%20Search.pdf#page=11) |
| Automatic differentiation and REINFORCE; return-weighted log probability | [12-15](../Lecture%20Slides/2.4.%20Policy%20Search.pdf#page=12) |
| Actor-critic: actor policy, critic value/Q estimate | [16-17](../Lecture%20Slides/2.4.%20Policy%20Search.pdf#page=16) |
| Local/global policy optimization; gradient-free alternatives | [18-19](../Lecture%20Slides/2.4.%20Policy%20Search.pdf#page=18) |

## 3. Neural networks and deep learning fundamentals

### 3.1. Introduction to Deep Learning.pdf

| Concept / method / exercise | PDF pages |
| --- | --- |
| AI, ML and deep learning; what deep learning means | [6-10](../Lecture%20Slides/3.1.%20Introduction%20to%20Deep%20Learning.pdf#page=6) |
| Application examples: language, vision, control, science and engineering | [11-25](../Lecture%20Slides/3.1.%20Introduction%20to%20Deep%20Learning.pdf#page=11) |
| Deep learning and Big Data; opportunities and limitations | [26-29](../Lecture%20Slides/3.1.%20Introduction%20to%20Deep%20Learning.pdf#page=26) |
| DL pipeline, learning methodology and overfitting | [30-32, 36-37](../Lecture%20Slides/3.1.%20Introduction%20to%20Deep%20Learning.pdf#page=30) |
| Collecting and labeling data; coverage, classes and variability | [33-35](../Lecture%20Slides/3.1.%20Introduction%20to%20Deep%20Learning.pdf#page=33) |
| Handcrafted versus learned features; representation learning | [38-39](../Lecture%20Slides/3.1.%20Introduction%20to%20Deep%20Learning.pdf#page=38) |

### 3.2. Shallow NN.pdf

| Concept / method / exercise | PDF pages |
| --- | --- |
| Linear regression versus a shallow neural-network model | [4-6](../Lecture%20Slides/3.2.%20Shallow%20NN.pdf#page=4) |
| ReLU activation; example network and its ten parameters | [7-9](../Lecture%20Slides/3.2.%20Shallow%20NN.pdf#page=7) |
| Hidden-unit construction; weighted sums and piecewise-linear output | [10-17](../Lecture%20Slides/3.2.%20Shallow%20NN.pdf#page=10) |
| Activation patterns / active hidden units | [18](../Lecture%20Slides/3.2.%20Shallow%20NN.pdf#page=18) |
| Network diagrams, weights and hidden width | [19-22](../Lecture%20Slides/3.2.%20Shallow%20NN.pdf#page=19) |
| Universal approximation theorem | [23-24](../Lecture%20Slides/3.2.%20Shallow%20NN.pdf#page=23) |
| Multiple outputs; shared hidden representation and output-specific weights | [26-28](../Lecture%20Slides/3.2.%20Shallow%20NN.pdf#page=26) |
| Multiple inputs; activation boundaries and regions in 2D | [30-37](../Lecture%20Slides/3.2.%20Shallow%20NN.pdf#page=30) |
| General input/hidden/output dimensions; parameter-count exercise | [39-42](../Lecture%20Slides/3.2.%20Shallow%20NN.pdf#page=39) |
| Number of linear regions; dependence on input dimension and hidden width | [44-47](../Lecture%20Slides/3.2.%20Shallow%20NN.pdf#page=44) |
| Terminology: layers, units, biases and weights | [49-50](../Lecture%20Slides/3.2.%20Shallow%20NN.pdf#page=49) |
| Alternative activation functions | [51](../Lecture%20Slides/3.2.%20Shallow%20NN.pdf#page=51) |

### 3.3. Deep Learning Fundamentals.pdf

| Concept / method / exercise | PDF pages |
| --- | --- |
| Neuron/perceptron recap; composition of nonlinear layers | [3-7](../Lecture%20Slides/3.3.%20Deep%20Learning%20Fundamentals.pdf#page=3) |
| Depth, width, matrix formulation and deep-network parameter shapes | [8-11](../Lecture%20Slides/3.3.%20Deep%20Learning%20Fundamentals.pdf#page=8) |
| Shallow versus deep capacity; depth efficiency and linear regions | [12-14](../Lecture%20Slides/3.3.%20Deep%20Learning%20Fundamentals.pdf#page=12) |
| Scores / logits; mapping inputs to class scores | [16-21](../Lecture%20Slides/3.3.%20Deep%20Learning%20Fundamentals.pdf#page=16) |
| Loss functions; multiclass SVM / hinge loss | [22-23](../Lecture%20Slides/3.3.%20Deep%20Learning%20Fundamentals.pdf#page=22) |
| Softmax cross-entropy; score/probability interpretation and loss exercise | [24-26](../Lecture%20Slides/3.3.%20Deep%20Learning%20Fundamentals.pdf#page=24) |
| Choosing a task loss; adding regularization | [27-28](../Lecture%20Slides/3.3.%20Deep%20Learning%20Fundamentals.pdf#page=27) |
| Optimization, gradient descent, SGD and mini-batch noise | [29-35](../Lecture%20Slides/3.3.%20Deep%20Learning%20Fundamentals.pdf#page=29) |
| Local minima, saddle points and optimization difficulties | [31, 36](../Lecture%20Slides/3.3.%20Deep%20Learning%20Fundamentals.pdf#page=31) |
| Momentum and optimizer variants | [37-39](../Lecture%20Slides/3.3.%20Deep%20Learning%20Fundamentals.pdf#page=37) |
| Adam: moment estimates, normalization and bias correction | [40-42](../Lecture%20Slides/3.3.%20Deep%20Learning%20Fundamentals.pdf#page=40) |
| Parameters, hyperparameters and the training pipeline | [43-44](../Lecture%20Slides/3.3.%20Deep%20Learning%20Fundamentals.pdf#page=43) |

### 3.4. Deep Learning Fundamentals II.pdf

| Concept / method / exercise | PDF pages |
| --- | --- |
| Forward pass, backward pass, gradients and chain rule | [3-7](../Lecture%20Slides/3.4.%20Deep%20Learning%20Fundamentals%20II.pdf#page=3) |
| Scalar backpropagation examples and classroom exercise | [8-17](../Lecture%20Slides/3.4.%20Deep%20Learning%20Fundamentals%20II.pdf#page=8) |
| Computation graphs; local backward operations and autograd | [18-22](../Lecture%20Slides/3.4.%20Deep%20Learning%20Fundamentals%20II.pdf#page=18) |
| Input normalization; random initialization, He and gradient scale | [23-25](../Lecture%20Slides/3.4.%20Deep%20Learning%20Fundamentals%20II.pdf#page=23) |
| Generalization gap; explicit L2 regularization / weight decay | [26-29](../Lecture%20Slides/3.4.%20Deep%20Learning%20Fundamentals%20II.pdf#page=26) |
| Implicit regularization; SGD and early stopping | [30-31](../Lecture%20Slides/3.4.%20Deep%20Learning%20Fundamentals%20II.pdf#page=30) |
| Dropout; randomly disabling hidden units during training | [32, 34](../Lecture%20Slides/3.4.%20Deep%20Learning%20Fundamentals%20II.pdf#page=32) |
| More data, noise and label-preserving data augmentation | [33-35](../Lecture%20Slides/3.4.%20Deep%20Learning%20Fundamentals%20II.pdf#page=33) |
| Capacity, generalization and double descent | [36-38](../Lecture%20Slides/3.4.%20Deep%20Learning%20Fundamentals%20II.pdf#page=36) |
| Hyperparameter choices and overall training recipe | [39-42](../Lecture%20Slides/3.4.%20Deep%20Learning%20Fundamentals%20II.pdf#page=39) |
| Matrix derivatives; forward and backward propagation through layers | [44-48](../Lecture%20Slides/3.4.%20Deep%20Learning%20Fundamentals%20II.pdf#page=44) |
| ReLU derivative | [49-50](../Lecture%20Slides/3.4.%20Deep%20Learning%20Fundamentals%20II.pdf#page=49) |
| Gradients with respect to weights and biases | [51-52](../Lecture%20Slides/3.4.%20Deep%20Learning%20Fundamentals%20II.pdf#page=51) |
| Backpropagation: efficiency and limitations | [53](../Lecture%20Slides/3.4.%20Deep%20Learning%20Fundamentals%20II.pdf#page=53) |

## 4. CNNs and transfer learning

### 4.1. CNNs.pdf

| Concept / method / exercise | PDF pages |
| --- | --- |
| Image structure; local connectivity, weight sharing and convolutional features | [4-11](../Lecture%20Slides/4.1.%20CNNs.pdf#page=4) |
| One-dimensional convolution and filter sliding | [12-14](../Lecture%20Slides/4.1.%20CNNs.pdf#page=12) |
| Kernel, stride, padding, dilation; output-size formula and questions | [15-18](../Lecture%20Slides/4.1.%20CNNs.pdf#page=15) |
| Feature maps/channels and receptive fields | [19-23](../Lecture%20Slides/4.1.%20CNNs.pdf#page=19) |
| 2D/RGB convolution; input/output channels and parameter counts | [24-30](../Lecture%20Slides/4.1.%20CNNs.pdf#page=24) |
| Downsampling, pooling and strided convolution | [31-32](../Lecture%20Slides/4.1.%20CNNs.pdf#page=31) |
| Upsampling, interpolation, unpooling and transposed convolution | [33-35](../Lecture%20Slides/4.1.%20CNNs.pdf#page=33) |
| 1-by-1 / pointwise convolution; mixing channels | [36](../Lecture%20Slides/4.1.%20CNNs.pdf#page=36) |
| AlexNet, DeConvNet and feature-map visualization | [37-43](../Lecture%20Slides/4.1.%20CNNs.pdf#page=37) |
| VGG; small filters, depth and receptive-field comparison | [44-47](../Lecture%20Slides/4.1.%20CNNs.pdf#page=44) |
| Activation memory, batch size and deeper architectures | [48-50](../Lecture%20Slides/4.1.%20CNNs.pdf#page=48) |
| Vanishing gradients; ResNet, identity shortcuts and bottleneck blocks | [51-54](../Lecture%20Slides/4.1.%20CNNs.pdf#page=51) |
| Batch normalization: statistics, gamma/beta and parameter count | [55-56](../Lecture%20Slides/4.1.%20CNNs.pdf#page=55) |
| BN training versus inference; running statistics, eval mode and folding | [57](../Lecture%20Slides/4.1.%20CNNs.pdf#page=57) |
| Why normalization helps; batch/layer/instance/group normalization | [58-59](../Lecture%20Slides/4.1.%20CNNs.pdf#page=58) |
| ResNet family; addition versus concatenation; residual/BN quick questions | [60-62](../Lecture%20Slides/4.1.%20CNNs.pdf#page=60) |
| Inception/GoogLeNet and DenseNet modules | [63](../Lecture%20Slides/4.1.%20CNNs.pdf#page=63) |
| MobileNet depthwise-separable convolution; EfficientNet scaling | [64](../Lecture%20Slides/4.1.%20CNNs.pdf#page=64) |
| Vision Transformer / ConvNeXt comparison and architecture trends | [65-66](../Lecture%20Slides/4.1.%20CNNs.pdf#page=65) |
| Transfer learning and frozen feature extraction | [67-70](../Lecture%20Slides/4.1.%20CNNs.pdf#page=67) |
| Fine-tuning; dataset size/domain similarity and adaptation choices | [71-74](../Lecture%20Slides/4.1.%20CNNs.pdf#page=71) |
| Initial loss, overfitting a tiny set, learning curves, learning-rate decay | [75-81](../Lecture%20Slides/4.1.%20CNNs.pdf#page=75) |
| Detection, box regression, Faster R-CNN and YOLO | [82-86](../Lecture%20Slides/4.1.%20CNNs.pdf#page=82) |
| PoseNet; position/orientation regression | [87-88](../Lecture%20Slides/4.1.%20CNNs.pdf#page=87) |
| Semantic segmentation, FCN, SegNet and instance segmentation/Mask R-CNN | [90-93](../Lecture%20Slides/4.1.%20CNNs.pdf#page=90) |
| Video feature fusion, multimodal inputs and temporal-order limitations | [94-101](../Lecture%20Slides/4.1.%20CNNs.pdf#page=94) |
| Task summary; 1D/2D/3D engineering applications and simulation surrogates | [102-105](../Lecture%20Slides/4.1.%20CNNs.pdf#page=102) |
| Classroom calculation: feature-map sizes and convolution parameters | [106](../Lecture%20Slides/4.1.%20CNNs.pdf#page=106) |
| Lab 3 connection: toy CNNs and pretrained-model fine-tuning | [108-110](../Lecture%20Slides/4.1.%20CNNs.pdf#page=108) |

## 5. Advanced deep learning

### 5.1. Sequence Models.pdf

| Concept / method / exercise | PDF pages |
| --- | --- |
| Sequential order, variable lengths, recurrence and shared weights | [3-6](../Lecture%20Slides/5.1.%20Sequence%20Models.pdf#page=3) |
| Vanilla RNN equations; hidden state and character-level predictions | [7-9](../Lecture%20Slides/5.1.%20Sequence%20Models.pdf#page=7) |
| Generated sequences and interpretable recurrent units | [10-12](../Lecture%20Slides/5.1.%20Sequence%20Models.pdf#page=10) |
| Backpropagation through time (BPTT); vanishing/exploding gradients | [13-15](../Lecture%20Slides/5.1.%20Sequence%20Models.pdf#page=13) |
| Truncated BPTT; memory cost and long-range gradient limitations | [14, 16](../Lecture%20Slides/5.1.%20Sequence%20Models.pdf#page=14) |
| Gradient clipping, initialization and architectural remedies | [16](../Lecture%20Slides/5.1.%20Sequence%20Models.pdf#page=16) |
| LSTM cell/hidden states; forget, input, candidate and output gates | [17-20](../Lecture%20Slides/5.1.%20Sequence%20Models.pdf#page=17) |
| Additive memory path; GRU and its gates | [21](../Lecture%20Slides/5.1.%20Sequence%20Models.pdf#page=21) |
| Stacked and bidirectional recurrent networks | [22](../Lecture%20Slides/5.1.%20Sequence%20Models.pdf#page=22) |
| Video action recognition and dense captioning | [23-24](../Lecture%20Slides/5.1.%20Sequence%20Models.pdf#page=23) |
| Temporal convolutional networks (TCN); causal/dilated filters; WaveNet | [25-27](../Lecture%20Slides/5.1.%20Sequence%20Models.pdf#page=25) |
| Recurrent seq2seq encoder-decoder; fixed context vector | [28](../Lecture%20Slides/5.1.%20Sequence%20Models.pdf#page=28) |
| Teacher forcing, inference feedback, exposure bias and scheduled sampling | [29](../Lecture%20Slides/5.1.%20Sequence%20Models.pdf#page=29) |
| Attention over encoder states; captioning with attention | [30-31](../Lecture%20Slides/5.1.%20Sequence%20Models.pdf#page=30) |
| Summary equations: RNN, BPTT, LSTM, seq2seq and attention | [32](../Lecture%20Slides/5.1.%20Sequence%20Models.pdf#page=32) |
| Character-RNN practical exercise | [33](../Lecture%20Slides/5.1.%20Sequence%20Models.pdf#page=33) |

### 5.1. Extra Material.pdf

| Concept / method / exercise | PDF pages |
| --- | --- |
| LSTM cell diagrams and gates | [2-4](../Lecture%20Slides/5.1.%20Extra%20Material.pdf#page=2) |
| Tiny LSTM: matrix dimensions, vocabulary, hidden width and parameter counts | [5](../Lecture%20Slides/5.1.%20Extra%20Material.pdf#page=5) |
| Learned parameters versus computed states; changing vocabulary or hidden width | [6](../Lecture%20Slides/5.1.%20Extra%20Material.pdf#page=6) |
| Worked LSTM update: gates, cell/hidden state and next-character scores | [7](../Lecture%20Slides/5.1.%20Extra%20Material.pdf#page=7) |

### 5.2. Transformers.pdf

| Concept / method / exercise | PDF pages |
| --- | --- |
| RNN/CNN/attention comparison; weighted context and query/key/value intuition | [3-8](../Lecture%20Slides/5.2.%20Transformers.pdf#page=3) |
| Self-attention: value projections, query-key scores and softmax weights | [9-10](../Lecture%20Slides/5.2.%20Transformers.pdf#page=9) |
| Numerical attention example; shared parameters versus input-dependent weights | [11](../Lecture%20Slides/5.2.%20Transformers.pdf#page=11) |
| Matrix attention, tensor shapes, row softmax and square-root scaling | [12-14](../Lecture%20Slides/5.2.%20Transformers.pdf#page=12) |
| Permutation equivariance / order blindness; need for positional information | [15](../Lecture%20Slides/5.2.%20Transformers.pdf#page=15) |
| Sinusoidal, learned, relative, rotary (RoPE) and ALiBi positions | [16-17](../Lecture%20Slides/5.2.%20Transformers.pdf#page=16) |
| Encoder-only, decoder-only and encoder-decoder overview | [18](../Lecture%20Slides/5.2.%20Transformers.pdf#page=18) |
| Tokenization: words, characters, subwords and BPE | [19](../Lecture%20Slides/5.2.%20Transformers.pdf#page=19) |
| Token embeddings, embedding table and contextual representations | [20-22](../Lecture%20Slides/5.2.%20Transformers.pdf#page=20) |
| Transformer block and multi-head attention; concatenate and project | [23-24](../Lecture%20Slides/5.2.%20Transformers.pdf#page=23) |
| Residual connections; Add & Norm and layer normalization | [25, 27](../Lecture%20Slides/5.2.%20Transformers.pdf#page=25) |
| Positionwise feed-forward MLP | [26](../Lecture%20Slides/5.2.%20Transformers.pdf#page=26) |
| Encoder stack, masked language modeling and CLS readout | [28-29](../Lecture%20Slides/5.2.%20Transformers.pdf#page=28) |
| Autoregressive factorization; next-token cross-entropy and training parallelism | [30](../Lecture%20Slides/5.2.%20Transformers.pdf#page=30) |
| Causal mask; future-token leakage and zero attention to forbidden positions | [31](../Lecture%20Slides/5.2.%20Transformers.pdf#page=31) |
| Self-attention versus cross-attention; three transformer families | [32-35](../Lecture%20Slides/5.2.%20Transformers.pdf#page=32) |
| Quadratic attention cost; KV cache, FlashAttention and grouped-query attention | [36](../Lecture%20Slides/5.2.%20Transformers.pdf#page=36) |
| Vision Transformers: patches, projection, positions, CLS and hybrid designs | [37-40](../Lecture%20Slides/5.2.%20Transformers.pdf#page=37) |
| A/B classroom attention exercise; simplified divide-by-three normalization | [41-42](../Lecture%20Slides/5.2.%20Transformers.pdf#page=41) |

### 5.3. Foundation models.pdf

| Concept / method / exercise | PDF pages |
| --- | --- |
| Transformer-family recap; encoder, decoder and cross-attention | [5-8](../Lecture%20Slides/5.3.%20Foundation%20models.pdf#page=5) |
| Foundation-model definition; broad pretraining and downstream transfer | [9-11](../Lecture%20Slides/5.3.%20Foundation%20models.pdf#page=9) |
| Scale, data, hardware; total versus active MoE parameters; shared biases | [12-13](../Lecture%20Slides/5.3.%20Foundation%20models.pdf#page=12) |
| Training stages: self-supervised pretraining, SFT, preference RL, verifiable RL | [14](../Lecture%20Slides/5.3.%20Foundation%20models.pdf#page=14) |
| BERT: masked-token and next-sentence pretraining examples | [15](../Lecture%20Slides/5.3.%20Foundation%20models.pdf#page=15) |
| GPT-style generation and multimodal model examples; post-training | [16-17](../Lecture%20Slides/5.3.%20Foundation%20models.pdf#page=16) |
| CLIP: image-text embeddings, contrastive alignment and zero-shot classification | [19-20](../Lecture%20Slides/5.3.%20Foundation%20models.pdf#page=19) |
| DINOv2: self-distillation, visual features and downstream transfer | [21](../Lecture%20Slides/5.3.%20Foundation%20models.pdf#page=21) |
| SAM: promptable segmentation | [22](../Lecture%20Slides/5.3.%20Foundation%20models.pdf#page=22) |
| Text-conditioned image generation; text encoder, denoiser and VAE decoder | [23-25](../Lecture%20Slides/5.3.%20Foundation%20models.pdf#page=23) |
| Efficiency, explainability and fairness questions | [26](../Lecture%20Slides/5.3.%20Foundation%20models.pdf#page=26) |

### 5.4. Unsupervised learning.pdf

| Concept / method / exercise | PDF pages |
| --- | --- |
| Supervision strategies; unlabeled data and semi-supervised learning | [2-7](../Lecture%20Slides/5.4.%20Unsupervised%20learning.pdf#page=2) |
| When unlabeled data helps: distribution relevance | [7](../Lecture%20Slides/5.4.%20Unsupervised%20learning.pdf#page=7) |
| PCA: variance, projection, compression and retained components | [9-11](../Lecture%20Slides/5.4.%20Unsupervised%20learning.pdf#page=9) |
| t-SNE: local neighborhoods, perplexity and visualization pitfalls | [12-18](../Lecture%20Slides/5.4.%20Unsupervised%20learning.pdf#page=12) |
| Visualizing high-dimensional CNN features | [17-18](../Lecture%20Slides/5.4.%20Unsupervised%20learning.pdf#page=17) |
| K-means: initialization, assignments and centroid updates | [19-20](../Lecture%20Slides/5.4.%20Unsupervised%20learning.pdf#page=19) |
| Hierarchical clustering: agglomerative versus divisive | [21](../Lecture%20Slides/5.4.%20Unsupervised%20learning.pdf#page=21) |
| Latent Dirichlet Allocation (LDA); topic mixtures, not discriminant analysis | [22](../Lecture%20Slides/5.4.%20Unsupervised%20learning.pdf#page=22) |
| Self-supervised pretraining and proxy/pretext tasks | [24-27](../Lecture%20Slides/5.4.%20Unsupervised%20learning.pdf#page=24) |
| Patch position, jigsaws, colorization and inpainting examples | [26-27](../Lecture%20Slides/5.4.%20Unsupervised%20learning.pdf#page=26) |
| Contrastive learning; positive/negative pairs and triplet ideas | [28-29](../Lecture%20Slides/5.4.%20Unsupervised%20learning.pdf#page=28) |
| BYOL: online/target networks and learning without negative pairs | [30-31](../Lecture%20Slides/5.4.%20Unsupervised%20learning.pdf#page=30) |
| SuperPoint: self-supervised keypoint detection and description | [32](../Lecture%20Slides/5.4.%20Unsupervised%20learning.pdf#page=32) |
| Semi-supervised teacher-student learning, memory banks and pixel-level contrast | [33](../Lecture%20Slides/5.4.%20Unsupervised%20learning.pdf#page=33) |
| Connection to foundation models; PCA versus t-SNE summary | [34-36](../Lecture%20Slides/5.4.%20Unsupervised%20learning.pdf#page=34) |

### 5.5. Generative Models.pdf

| Concept / method / exercise | PDF pages |
| --- | --- |
| Discriminative versus generative modeling; learning a data distribution | [3-6](../Lecture%20Slides/5.5.%20Generative%20Models.pdf#page=3) |
| Autoencoder: encoder, latent code, decoder and reconstruction | [7](../Lecture%20Slides/5.5.%20Generative%20Models.pdf#page=7) |
| AE versus VAE; latent distributions, reconstruction plus KL regularization | [8](../Lecture%20Slides/5.5.%20Generative%20Models.pdf#page=8) |
| GANs: generator/discriminator roles and adversarial training | [9-12](../Lecture%20Slides/5.5.%20Generative%20Models.pdf#page=9) |
| GAN instability, weak gradients and mode collapse | [13](../Lecture%20Slides/5.5.%20Generative%20Models.pdf#page=13) |
| CycleGAN: unpaired translation and cycle consistency | [14](../Lecture%20Slides/5.5.%20Generative%20Models.pdf#page=14) |
| Image editing/style-transfer applications | [15-16](../Lecture%20Slides/5.5.%20Generative%20Models.pdf#page=15) |
| Forward diffusion: progressive Gaussian noising | [17](../Lecture%20Slides/5.5.%20Generative%20Models.pdf#page=17) |
| Learned reverse diffusion; denoising training versus sampling | [18-19](../Lecture%20Slides/5.5.%20Generative%20Models.pdf#page=18) |
| Conditional / latent diffusion; text representations and image decoding | [5, 20-21](../Lecture%20Slides/5.5.%20Generative%20Models.pdf#page=5) |
| AE/VAE/GAN/diffusion comparison: objective, stability, speed, quality, latent space | [22](../Lecture%20Slides/5.5.%20Generative%20Models.pdf#page=22) |
| Course map: AI, ML, neural networks, deep learning and application areas | [25-26](../Lecture%20Slides/5.5.%20Generative%20Models.pdf#page=25) |

## Lab 4 supplement: deployment, explainability and compression

### manolo_presentation.pdf (Lab Sessions / Lab4)

| Concept / method / exercise | PDF pages |
| --- | --- |
| Explainable AI (XAI) and model compression: definitions | [2](../Lab%20Sessions/Lab4/manolo_presentation.pdf#page=2) |
| AI governance / regulatory context discussed in the briefing | [3-4](../Lab%20Sessions/Lab4/manolo_presentation.pdf#page=3) |
| Trustworthiness, fairness, transparency and robustness | [5](../Lab%20Sessions/Lab4/manolo_presentation.pdf#page=5) |
| Edge deployment: latency, memory, compute, energy and privacy | [6](../Lab%20Sessions/Lab4/manolo_presentation.pdf#page=6) |
| Grad-CAM: class-specific image evidence and heatmaps | [7](../Lab%20Sessions/Lab4/manolo_presentation.pdf#page=7) |
| Compression families: quantization, pruning, distillation and low-rank methods | [8](../Lab%20Sessions/Lab4/manolo_presentation.pdf#page=8) |
| FP32 versus INT8 quantization; memory reduction and accuracy trade-off | [9](../Lab%20Sessions/Lab4/manolo_presentation.pdf#page=9) |
| Magnitude pruning, sparsity, fine-tuning and hardware-dependent speed | [10](../Lab%20Sessions/Lab4/manolo_presentation.pdf#page=10) |
| Compare accuracy and explanations before/after compression | [11](../Lab%20Sessions/Lab4/manolo_presentation.pdf#page=11) |
| Lab notebook workflow and evaluation tasks | [12](../Lab%20Sessions/Lab4/manolo_presentation.pdf#page=12) |
