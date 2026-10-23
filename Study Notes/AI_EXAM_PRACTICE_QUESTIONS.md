---
title: "Artificial Intelligence: Exam Practice"
subtitle: "Questions only · Course slides · 23 October 2026"
author: "MAICE · Artificial Intelligence"
lang: en-GB
---

# How to use this question bank

**120 core questions and 8 supplementary questions. No answers or worked solutions are included.** This is a revision bank covering the supplied course slides, not a single one-hour paper. The selection emphasizes definitions, the meaning of values, comparisons between methods, and small calculations. It is a study selection, not a prediction of the teachers' exact questions or topic weights.

- **MC:** choose one best answer from A–D. Exactly one option is intended to be correct.
- **Short:** answer in 1–3 sentences, or a few brief points when requested.
- **Calculation:** show one formula and a short substitution. All numerical exercises are deliberately small; no long derivations or full training iterations are needed.

For timed practice, use **AI_EXAM_MOCK_PAPERS.md** or its PDF. Each paper contains 20 MC questions and 8 short questions, including 2 calculations. Suggested timing: 20 minutes for MC, 32 minutes for short questions, and 8 minutes to review. The two papers use different questions.

The core covers modules 0–5.5. The final supplement uses the Lab 4 briefing slides because explainability and ethics appear in the course outline but have no separate deck in `Lecture Slides`. The full multi-gate LSTM exercise is reduced to questions about states and one scalar update. Historical dates, product parameter counts, API details and lengthy proofs are not revision priorities here.

# 0. Mathematical background

Focus: probability, uncertainty, likelihood, and interpreting simple distributions.

### Q001 · MC

Which binary probability distribution has the greatest Shannon entropy?

- A. $(1.00, 0.00)$
- B. $(0.99, 0.01)$
- C. $(0.50, 0.50)$
- D. $(0.80, 0.20)$

### Q002 · MC

For two discrete probability distributions on the same finite set, what does $D_{KL}(p\|q)=0$ imply?

- A. They have disjoint supports.
- B. Both distributions are uniform.
- C. Their means agree, but their probabilities may differ.
- D. They assign identical probabilities to every outcome.

### Q003 · MC

Maximum-likelihood estimation chooses parameters that:

- A. Minimize the number of observations used for training.
- B. Make the posterior distribution uniform.
- C. Maximize the prior probability of the parameters alone.
- D. Maximize the probability or density of the observed data under the model.

### Q004 · MC

A scalar variable has distribution $X\sim\mathcal{N}(10,4)$, where the second argument is the variance. Which interpretation is correct?

- A. Every observation lies between 6 and 14.
- B. Mean 4, variance 10.
- C. Mean 10, standard deviation 4.
- D. Mean 10, standard deviation 2.

### Q005 · Calculation

Two hypotheses, $H_1$ and $H_2$, are mutually exclusive and exhaustive. You know $P(H_1)=0.4$, $P(D\mid H_1)=0.5$, and $P(D)=0.25$. Compute $P(H_1\mid D)$ using Bayes' rule.

### Q006 · Calculation

A reward $R$ is 0 with probability 0.25 and 4 with probability 0.75. Compute $\mathbb{E}[R]$. Does this expectation mean every trial produces that reward?

# 1.1. Learning fundamentals

Focus: learning settings, generalization, data splits, model selection, and k-NN.

### Q007 · MC

Which task is an example of unsupervised learning?

- A. Predicting house prices from examples with known prices.
- B. Classifying emails using examples labelled spam or not spam.
- C. Learning a robot policy from rewards.
- D. Grouping customers by similarity without predefined group labels.

### Q008 · MC

You compare several hyperparameter settings. Which dataset should normally guide the choice, while preserving an independent final evaluation?

- A. The union of the training and test sets.
- B. The validation set, or validation folds within the training data.
- C. The test set, evaluated after every change.
- D. The training set alone.

### Q009 · MC

A model has similarly high errors on its training and validation sets. Which diagnosis is most consistent with these observations?

- A. Evidence that the test labels leaked into training.
- B. A successful model with low irreducible error.
- C. Underfitting, or an optimization problem that prevents a good fit.
- D. Severe overfitting to the training examples.

### Q010 · MC

In k-nearest-neighbour classification, increasing $k$ usually makes the decision boundary:

- A. Identical, because $k$ only affects inference speed.
- B. More irregular and more sensitive to individual examples.
- C. Smoother and less sensitive to individual training examples.
- D. Equivalent to the boundary of a linear SVM.

### Q011 · MC

What is an inductive bias?

- A. The assumptions that favour some patterns or solutions over others.
- B. The difference between the training and validation set sizes.
- C. The scalar intercept of every machine-learning model.
- D. The average prediction error on the training set.

### Q012 · Short

Training accuracy keeps increasing, while validation accuracy has stopped improving and begins to decrease. Name the likely problem and give one appropriate response.

### Q013 · Short

Distinguish a model parameter from a hyperparameter. Give one example of each for a model studied in the course.

### Q014 · Short

Why can feature scaling strongly affect a Euclidean-distance k-NN classifier? Which data split should be used to fit the scaling transformation before applying it to validation and test data?

# 1.2. Shallow learning

Focus: regression, regularization, classification, evaluation metrics, SVMs, and ensembles.

### Q015 · MC

The model $\hat y=w_0+w_1x+w_2x^2$ is called linear regression with polynomial features because it is:

- A. Linear in $x$.
- B. Restricted to straight-line predictions.
- C. Linear in the fitted parameters $w_0,w_1,w_2$.
- D. Trained without an optimization objective.

### Q016 · MC

In ridge regression with objective $L(w)+\lambda\|w\|_2^2$, increasing $\lambda$ means:

- A. Increasing the number of polynomial features.
- B. Penalizing large coefficient magnitudes more strongly.
- C. Taking larger gradient steps.
- D. Giving less importance to large coefficient magnitudes.

### Q017 · MC

Which regularizer is especially associated with producing exactly zero coefficients and therefore sparse models?

- A. A larger validation set.
- B. An L1 penalty on the coefficients.
- C. An L2 penalty on the coefficients.
- D. An increase in the learning rate.

### Q018 · MC

A binary logistic-regression model outputs $p(y=1\mid x)=0.8$. Using a decision threshold of 0.5, what does this mean?

- A. The model has 80% accuracy on the dataset.
- B. It predicts class 1 and assigns that class probability 0.8 for this input.
- C. Exactly 80% of the input features indicate class 1.
- D. The true label is guaranteed to be 1.

### Q019 · MC

A dataset contains 95% negative examples. A classifier predicts every example as negative. Which statement is correct?

- A. Its positive-class recall is 95%.
- B. Its accuracy is 95%, but its positive-class recall is 0%.
- C. Its high accuracy establishes that it detects positive examples well.
- D. Its accuracy and positive-class F1 score are both 95%.

### Q020 · MC

For linearly separable data, a hard-margin SVM selects a separating hyperplane by:

- A. Minimizing the number of input features.
- B. Maximizing the margin to the closest training examples.
- C. Maximizing the distance to the average training example.
- D. Maximizing the number of support vectors.

### Q021 · MC

Which description correctly distinguishes the ensemble methods discussed in the slides?

- A. Random forests contain one tree; boosting combines only linear models.
- B. Boosting trains all learners independently on bootstrap samples and only averages them.
- C. Random forests combine randomized trees; boosting builds learners sequentially to address errors of the current ensemble.
- D. Bagging requires each new learner to correct the previous learner's residuals.

### Q022 · Calculation

For a chosen positive class, a classifier has $TP=30$, $FP=10$, and $FN=20$. Compute its precision and recall. Leave the results as fractions or percentages.

### Q023 · Short

Using the standard definition $R^2=1-\mathrm{SSE}/\mathrm{SST}$ on a test set with nonconstant targets, interpret $R^2=1$, $R^2=0$, and $R^2<0$ relative to predicting the test-set mean.

### Q024 · Short

Why is squared-error regression more sensitive to large outliers than absolute-error regression? Name one robust fitting method or loss mentioned in the slides.

### Q025 · Short

What does the kernel trick allow an SVM to do without explicitly constructing a potentially very large feature vector?

### Q026 · Short

What does a decision tree do at an internal node? Why can allowing a tree to grow very deep increase overfitting?

# 1.3. Bayesian learning

Focus: priors and posteriors, prediction with uncertainty, Gaussian processes, and kernel hyperparameters.

### Q027 · MC

Which statement best distinguishes full Bayesian parameter learning from maximum-likelihood or MAP point estimation?

- A. MAP keeps a distribution, but Bayesian learning keeps only its maximum.
- B. Bayesian learning keeps a distribution over plausible parameter values.
- C. Maximum likelihood requires a prior, but Bayesian learning does not.
- D. Bayesian learning removes the need for a likelihood.

### Q028 · MC

In linear regression with Gaussian observation noise, a zero-mean isotropic Gaussian prior on the weights leads to which MAP penalty?

- A. An L2 penalty.
- B. An L1 penalty.
- C. A penalty on the validation error alone.
- D. A penalty on the number of observations.

### Q029 · MC

Two Bayesian predictions have the same mean but different predictive variances. The one with larger variance represents:

- A. A guarantee of a larger prediction error on the next observation.
- B. A larger number of training examples at that input.
- C. Greater predictive uncertainty under the model.
- D. A larger predicted target value.

### Q030 · MC

For an RBF Gaussian-process kernel, increasing the length scale while keeping other hyperparameters fixed generally favours functions that:

- A. Have a larger observation-noise variance by definition.
- B. Become periodic.
- C. Vary more slowly, with correlation extending across larger input distances.
- D. Vary more rapidly over short input distances.

### Q031 · MC

What does the kernel $k(x,x')$ specify in a Gaussian process?

- A. The probability that $x$ and $x'$ have the same label.
- B. The posterior mean at $x$ for every dataset.
- C. The covariance between function values at $x$ and $x'$.
- D. The number of basis functions stored for each input.

### Q032 · Short

In $p(w\mid D)\propto p(D\mid w)p(w)$, identify the prior, likelihood, and posterior. Which expresses beliefs before observing this dataset?

### Q033 · Short

Distinguish uncertainty about an underlying function $f(x)$ from observation noise in $y=f(x)+\epsilon$. Which source can often be reduced by collecting more informative training data?

### Q034 · Short

In an ARD RBF kernel, one input dimension has a much larger length scale than the others. With comparably scaled input dimensions, what does this suggest about the model's sensitivity to that dimension?

# 2. Reinforcement learning

Focus: MDPs, returns and values, Bellman updates, exploration, TD methods, Q-learning, and policy search.

### Q035 · MC

What does the Markov property require of a state representation?

- A. Given the current state and action, past history provides no additional information about the next-state distribution.
- B. All actions must have equal probability.
- C. The reward must depend on the full history.
- D. The next state must be deterministic.

### Q036 · MC

A stochastic policy $\pi(a\mid s)$ specifies:

- A. A probability distribution over actions in state $s$.
- B. The immediate reward for taking action $a$.
- C. A probability distribution over next states for a fixed action.
- D. The optimal discounted return in state $s$.

### Q037 · MC

What does setting the discount factor $\gamma=0$ do to the return objective?

- A. It prevents the agent from changing its policy.
- B. It makes all rewards equal to zero.
- C. It makes only the next immediate reward contribute.
- D. It makes all future rewards equally important.

### Q038 · MC

What does $Q^\pi(s,a)$ represent?

- A. The expected return after taking $a$ in $s$ and then following $\pi$.
- B. The probability of reaching state $s$ under policy $\pi$.
- C. Only the immediate reward from action $a$.
- D. The probability that $a$ is the optimal action.

### Q039 · MC

What distinguishes a Bellman optimality backup from a Bellman expectation backup for a fixed policy?

- A. It removes the immediate reward.
- B. It averages uniformly over all actions.
- C. It sets the discount factor to 1.
- D. It chooses the best action instead of averaging actions according to the fixed policy.

### Q040 · MC

Which statement correctly compares Monte Carlo policy evaluation with one-step TD evaluation?

- A. Both require an exact transition model.
- B. Monte Carlo bootstraps from the next state's value; TD always waits for the full return.
- C. Monte Carlo uses completed sampled returns; TD can update using a reward and an estimated successor value before an episode ends.
- D. TD does not use observed rewards.

### Q041 · MC

Under the usual $\epsilon$-greedy rule, with probability $\epsilon$ an action is selected uniformly at random. Increasing $\epsilon$ directly increases:

- A. The number of states in the environment model.
- B. The step size of every value update.
- C. The frequency of random action selection.
- D. The weight assigned to future rewards.

### Q042 · MC

Which next-action value appears in the standard Q-learning target?

- A. The average Q-value over all previous states.
- B. The value of the actual next action sampled from the behaviour policy.
- C. The minimum Q-value at the current state.
- D. The maximum Q-value over available actions at the next state.

### Q043 · MC

Why is standard SARSA described as on-policy?

- A. Its update uses the next action sampled from the policy whose behaviour it is learning about.
- B. It requires a known transition model.
- C. It updates only at the end of an episode.
- D. It uses only deterministic policies.

### Q044 · MC

In REINFORCE, sampled returns are used primarily to:

- A. Guarantee a global maximum of the policy objective.
- B. Weight policy-gradient updates so actions associated with better returns are reinforced.
- C. Supervise an exact transition-probability table.
- D. Replace the policy with a list of fixed class labels.

### Q045 · Calculation

The next two rewards are 2 and 4, and the episode then ends. With $\gamma=0.5$, compute the discounted return $G=2+\gamma\,4$.

### Q046 · Calculation

Perform one Q-learning update. The current value is $Q(s,a)=2$, the received reward is $r=1$, $\gamma=0.5$, $\alpha=0.5$, and $\max_{a'}Q(s',a')=6$. Compute the target $r+\gamma\max Q(s',a')$ and then the updated value $Q(s,a)+\alpha[\text{target}-Q(s,a)]$.

### Q047 · Short

Distinguish policy evaluation, value iteration, and policy iteration by stating what each computes or alternates between.

### Q048 · Short

What distinguishes model-based from model-free reinforcement learning? Identify what “model” refers to in this distinction.

### Q049 · Short

Why use a function approximator for $Q(s,a)$ instead of a table when the state space is very large? What does deep RL change about the representation?

### Q050 · Short

In actor–critic learning, what is the actor's role and what is the critic's role? Compared with plain Monte Carlo policy gradients, what variance–bias trade-off can a learned critic introduce?

# 3. Neural networks and deep-learning fundamentals

Focus: learned representations, capacity, activations, losses, optimization, backpropagation, and regularization.

### Q051 · MC

In an end-to-end deep-learning classifier, what does “representation learning” refer to?

- A. Converting every input into a one-hot class label before prediction.
- B. Selecting a fixed handcrafted feature vector before training begins.
- C. Storing the training labels in the final layer.
- D. Learning useful intermediate features from data as part of training.

### Q052 · MC

Several fully connected affine layers are composed with no nonlinear activations between them. The resulting mapping is:

- A. Necessarily a quadratic mapping.
- B. Able to represent any continuous function.
- C. Equivalent to nearest-neighbour classification.
- D. Another affine mapping.

### Q053 · MC

For a ReLU unit whose input is strictly negative, its output and local derivative with respect to that input are:

- A. Output 0; derivative 0.
- B. Output negative; derivative 1.
- C. Output 0; derivative 1.
- D. Output positive; derivative 0.

### Q054 · MC

What does the universal approximation theorem establish, under its usual assumptions?

- A. Every target function needs only one hidden unit.
- B. A shallow network trained on finite data always generalizes perfectly.
- C. Gradient descent will find such an approximation from any initialization.
- D. A sufficiently wide shallow network can approximate any continuous function on a compact domain arbitrarily well.

### Q055 · MC

Why can depth be useful even when a shallow network has universal approximation capacity?

- A. Every extra layer guarantees lower test error.
- B. Some compositional functions can be represented much more efficiently using multiple layers.
- C. Deep models need no training examples.
- D. Depth removes the need for activation functions.

### Q056 · MC

For multiclass classification with exactly one correct class, softmax is normally used to:

- A. Convert probabilities into arbitrary real-valued logits.
- B. Compute the derivative of every hidden layer.
- C. Convert class logits into nonnegative probabilities that sum to 1.
- D. Set every class score to either 0 or 1 during training.

### Q057 · MC

For one example with a one-hot target, cross-entropy is $-\log p_{\text{true}}$. Which prediction receives the larger loss?

- A. It depends only on the number of hidden layers.
- B. A prediction assigning 0.1 to the true class.
- C. Both receive the same loss if their predicted class is correct.
- D. A prediction assigning 0.9 to the true class.

### Q058 · MC

What does backpropagation compute?

- A. The generalization error without a validation set.
- B. The parameter update independently of any optimizer or learning rate.
- C. The optimal architecture for the dataset.
- D. Gradients of the loss with respect to parameters by applying the chain rule.

### Q059 · MC

What is a main reason to avoid identical zero initialization of all hidden units in the same layer?

- A. The loss cannot be evaluated if a weight is zero.
- B. The units can remain symmetric and learn the same features.
- C. Bias terms must be positive to train a network.
- D. Zero is outside the valid range of a neural-network weight.

### Q060 · MC

Which statement correctly describes standard dropout?

- A. It randomly deletes labels from the validation set.
- B. It randomly suppresses activations during training and is normally disabled during ordinary inference, with the appropriate scaling convention.
- C. It is an optimizer that accumulates past gradients.
- D. It deletes a fixed subset of units permanently before training.

### Q061 · Calculation

A fully connected layer has 3 inputs and 2 output units, with one bias per output unit. How many trainable scalar parameters does it have?

### Q062 · Calculation

A scalar weight is $w=2$, its loss gradient is $\partial L/\partial w=3$, and the learning rate is $\eta=0.1$. Compute one gradient-descent update. State whether the weight increases or decreases.

### Q063 · Calculation

At a particular point in a computational graph, $\partial L/\partial h=3$ and $\partial h/\partial w=2$, with no other path from $w$ to $L$. Compute $\partial L/\partial w$.

### Q064 · Short

What does mini-batch SGD change relative to full-batch gradient descent? Give one benefit and one consequence for the variability of the updates.

### Q065 · Short

What information from earlier updates does momentum use? What additional per-parameter information does Adam track to adapt update sizes?

### Q066 · Short

Explain how early stopping and label-preserving data augmentation can help generalization. What should be monitored to decide when to stop training?

# 4. CNNs and transfer learning

Focus: convolution, shapes and parameter counts, architectural building blocks, normalization, transfer, and vision tasks.

### Q067 · MC

Which pair of properties most directly reduces the parameter count of a convolutional layer compared with a fully connected layer on an image?

- A. Global connectivity and a separate bias for every input pixel.
- B. Larger input images and more output classes.
- C. Local connectivity and weight sharing across spatial positions.
- D. A separate filter for every pixel and no shared weights.

### Q068 · MC

What is the main role of a $1\times1$ convolution with stride 1?

- A. Increase the spatial receptive field by mixing neighbouring pixels.
- B. Remove all nonlinearities from the network.
- C. Pool neighbouring spatial positions by taking their maximum.
- D. Mix input channels at each spatial location and optionally change the channel count.

### Q069 · MC

For a standard convolution, what does the number of output channels equal?

- A. The number of spatial output positions.
- B. The stride multiplied by the input channel count.
- C. The kernel width.
- D. The number of filters.

### Q070 · MC

In a residual block $y=x+F(x)$ with matching shapes, what happens if $F(x)=0$?

- A. The block discards the input.
- B. The block implements the identity mapping.
- C. The block output becomes zero.
- D. The number of output channels doubles.

### Q071 · MC

For standard batch normalization with stored running statistics, which statement is correct?

- A. Evaluation updates the convolution weights using test-batch statistics.
- B. Batch normalization has no learnable scale or shift parameters.
- C. Training and evaluation both recompute statistics from the test set.
- D. Training uses current mini-batch statistics; evaluation normally uses stored running statistics.

### Q072 · MC

You have a small labelled image dataset similar to the data used to pretrain an available CNN. Which is a reasonable initial transfer-learning strategy?

- A. Choose the number of classes by inspecting test accuracy.
- B. Freeze the pretrained feature extractor and train a new task-specific classification head.
- C. Keep the old classification head even if its classes differ from the new task.
- D. Randomly initialize the entire network and discard the pretrained weights.

### Q073 · MC

What distinguishes instance segmentation from semantic segmentation?

- A. Semantic segmentation does not assign class labels to pixels.
- B. Instance segmentation predicts only one label per image.
- C. Semantic segmentation always predicts bounding boxes.
- D. Instance segmentation separates different objects of the same class.

### Q074 · Calculation

A convolution receives a $7\times7$ spatial input and uses a $3\times3$ kernel, stride 2, padding 1 on each side, and dilation 1. Using $W_{\text{out}}=\lfloor(W-K+2P)/S\rfloor+1$, compute the output height and width.

### Q075 · Calculation

A standard $3\times3$ convolution has 2 input channels, 4 output channels, and one bias per output channel. How many trainable parameters does it have? Spatial image dimensions are not needed.

### Q076 · Short

What is a unit's receptive field? How does dilation increase the spatial reach of a convolution without increasing the number of kernel weights?

### Q077 · Short

Distinguish feature extraction with a frozen pretrained network from fine-tuning. In each case, which weights are updated?

### Q078 · Short

A deeper plain CNN has higher **training** error than a shallower one. Why is this observation alone insufficient to diagnose overfitting? How can residual connections help with the relevant training difficulty?

# 5.1. Sequence models

Focus: recurrent state, shared parameters, gradient problems, gated units, and sequence-to-sequence training.

### Q079 · MC

When a trained RNN reads a sequence at inference time, which statement is correct?

- A. Both hidden-state size and parameter count grow with every token.
- B. The hidden state changes, while the same learned weights are reused across time steps.
- C. The hidden state remains fixed while the weights change.
- D. A new independent weight matrix is learned for each position.

### Q080 · MC

Which technique directly limits an exploding gradient's norm while preserving its direction when rescaling is needed?

- A. Increasing the learning rate.
- B. Removing all recurrent connections after training.
- C. Increasing the sequence length.
- D. Norm-based gradient clipping.

### Q081 · MC

In an LSTM, a forget-gate value close to 1 primarily means:

- A. Completely erase the corresponding previous cell-state component.
- B. Prevent any output from being computed.
- C. Set the corresponding hidden-state component to exactly 1.
- D. Retain most of the corresponding previous cell-state component before adding the new contribution.

### Q082 · MC

What is teacher forcing in sequence-to-sequence training?

- A. Feeding the correct previous token to the decoder during training.
- B. Selecting only the highest-probability token during every training step.
- C. Training the network without target sequences.
- D. Replacing the decoder with the encoder at inference time.

### Q083 · MC

What limitation of a basic fixed-context encoder–decoder does attention address?

- A. The decoder cannot produce sequences of variable length.
- B. The encoder cannot share weights over time.
- C. Compressing the entire input into one fixed-size context vector can lose information, especially for long inputs.
- D. The loss cannot be applied to discrete tokens.

### Q084 · Short

What is backpropagation through time? Why can repeated multiplication of derivatives make long-range dependencies difficult for a vanilla RNN to learn?

### Q085 · Calculation

For one LSTM cell-state component, use $c_t=f_t c_{t-1}+i_t g_t$. If $c_{t-1}=2$, $f_t=0.5$, $i_t=0.25$, and $g_t=0.8$, compute $c_t$. The gate values have already been calculated.

### Q086 · Short

What makes a temporal convolution causal? What must change if a temporal convolutional network needs to use information from much farther back in the sequence?

# 5.2. Attention and transformers

Focus: Q/K/V, attention weights, position, masks, architecture families, and computational cost.

### Q087 · MC

In scaled dot-product attention, which quantities determine the attention scores before softmax?

- A. Only the positional indices, independently of token content.
- B. Only the norms of the value vectors.
- C. Dot products between queries and keys.
- D. Dot products between values and final class labels.

### Q088 · MC

After computing attention weights for one query, the output is formed as:

- A. A weighted sum of the keys only.
- B. A weighted sum of the value vectors.
- C. The single value with the largest norm, discarding the weights.
- D. The sum of all query vectors without normalization.

### Q089 · MC

Why is the dot-product score divided by $\sqrt{d_k}$ in standard scaled attention?

- A. To control score magnitudes and reduce softmax saturation as key/query dimension grows.
- B. To reduce the number of token positions to $d_k$.
- C. To replace positional encoding.
- D. To make attention weights independent of the input.

### Q090 · MC

Why add positional information to an unmasked self-attention model?

- A. To ensure all words have different vocabulary indices.
- B. Self-attention alone is permutation equivariant and does not identify sequence positions.
- C. To make every attention weight equal.
- D. To remove the need for learned embeddings.

### Q091 · MC

At position $t$ in a decoder trained to predict the next token from tokens $1,\ldots,t$, a causal mask allows attention to:

- A. Positions $1,\ldots,t$, including the current input token.
- B. Future tokens only.
- C. Only position $t+1$.
- D. Every position except $t$.

### Q092 · MC

In encoder–decoder cross-attention, which sources normally provide queries, keys, and values?

- A. All three must come from the same sequence.
- B. Queries come from the encoder; keys and values come from future target labels.
- C. All three come from the encoder output.
- D. Queries come from decoder representations; keys and values come from encoder output.

### Q093 · MC

What distinguishes a token's initial embedding from a contextual embedding after transformer processing?

- A. The contextual embedding can depend on the surrounding tokens available to the model.
- B. The initial embedding already changes with surrounding tokens before attention is applied.
- C. The initial embedding is a class prediction, while the contextual embedding is a vocabulary index.
- D. The contextual embedding is always a one-hot vector.

### Q094 · MC

What does multi-head attention add to a single attention head?

- A. A new vocabulary for each position.
- B. A separate loss function that must be supervised for every head.
- C. An independent training dataset for each head.
- D. Several learned projection sets that can capture different relationships in parallel.

### Q095 · Calculation

One attention query has normalized weights $(0.25,0.75)$ over two scalar values $v_1=2$ and $v_2=6$. Compute its attention output.

### Q096 · Calculation

For one head, a full attention score matrix for $N$ tokens has $N^2$ entries. If sequence length increases from 100 to 200 tokens, by what factor does the number of score entries increase?

### Q097 · Short

Distinguish an encoder-only model, a decoder-only model, and an encoder–decoder model by their attention access and a typical task for each. Keep each description to one short line.

### Q098 · Short

Why can a causal transformer compute next-token losses for all positions in a known training sequence in parallel, while ordinary autoregressive generation still produces new tokens sequentially?

# 5.3. Foundation models

Focus: broad pretraining, adaptation, supervision sources, and transferable multimodal representations.

### Q099 · MC

Which property best characterizes a foundation model?

- A. It contains a fixed minimum number of layers.
- B. It is pretrained on broad data and can be adapted to many downstream tasks.
- C. It is defined by always using an encoder–decoder architecture.
- D. It is trained from scratch separately for each individual input.

### Q100 · MC

What is the source of target information in self-supervised pretraining?

- A. A human manually annotates every training target.
- B. Targets are constructed from the data itself.
- C. A reward is required from an interactive environment.
- D. Targets are taken from the held-out test labels.

### Q101 · MC

What is the main representation-learning objective of CLIP?

- A. Generate an image by iteratively removing Gaussian noise.
- B. Compress every image into a fixed handcrafted descriptor.
- C. Align corresponding images and text in a shared embedding space.
- D. Predict a separate semantic class for every image pixel using only masks.

### Q102 · MC

Which model–purpose pairing matches the slides?

- A. DINOv2: an adversarial image generator with a discriminator.
- B. DINOv2: self-supervised visual features; SAM: segmentation prompted by user input.
- C. CLIP: a method that requires retraining its encoders for every new class name.
- D. SAM: a method for next-token language modelling only.

### Q103 · Short

Distinguish supervised fine-tuning from preference-based reinforcement learning by stating the training signal used in each. What changes when rewards instead come from an automatic verifier, such as a unit test?

### Q104 · Short

What does zero-shot image classification mean in a CLIP-style system? Briefly describe how candidate class descriptions are used to classify a new image.

# 5.4. Unsupervised and self-supervised learning

Focus: PCA, visualization, clustering, limited labels, and representation-learning objectives.

### Q105 · MC

The first principal component of centred data is the direction that:

- A. Separates the labelled classes with the largest margin.
- B. Gives the greatest projected variance among unit directions.
- C. Gives the smallest projected variance.
- D. Maximizes the distance from the data mean.

### Q106 · MC

Which interpretation of a t-SNE plot is most defensible?

- A. It is mainly a visualization of local neighbourhood structure; global distances and cluster sizes need care.
- B. Changing perplexity cannot change the visualization.
- C. The distance between any two plotted clusters exactly preserves their original distance.
- D. A visible gap proves that the data have distinct ground-truth classes.

### Q107 · MC

Which description matches standard k-means?

- A. Choose directions that maximize projected variance.
- B. Learn a classifier from predefined cluster labels.
- C. Start with one cluster per observation and repeatedly merge the closest clusters.
- D. Alternate assigning points to the nearest centre and recomputing each centre as its assigned points' mean.

### Q108 · MC

Which setup is semi-supervised learning?

- A. Using only labelled examples but training for fewer epochs.
- B. Replacing all labels with rewards from an interactive agent.
- C. Using a small labelled dataset together with relevant unlabelled data.
- D. Training solely on manually labelled validation examples.

### Q109 · MC

In a standard contrastive objective with positive and negative pairs, training encourages:

- A. Positive-pair representations to become similar and negative-pair representations to remain separated.
- B. Positive-pair representations to move apart.
- C. Predictions to reproduce the raw input pixels exactly.
- D. Identical representations for every input.

### Q110 · Calculation

The covariance eigenvalues of a dataset are 6, 3, and 1. What fraction of total variance is retained by keeping the first two principal components?

### Q111 · Short

Give one self-supervised image pretext task from the slides. State what its target is and how that target is obtained without manually annotating semantic classes.

### Q112 · Short

BYOL uses an online network and a target network. What relationship should their outputs learn for two augmented views of the same image? Does its basic training setup require explicit negative examples?

# 5.5. Generative models

Focus: modelling data distributions, autoencoders and VAEs, GAN training, and diffusion.

### Q113 · MC

Which description best distinguishes generative modelling from ordinary discriminative classification?

- A. A generative model is any classifier with more than two classes.
- B. A generative model is defined by using no learned parameters.
- C. A generative model must always produce images rather than text or audio.
- D. A generative model learns a data-generating distribution or sampling mechanism, rather than only a mapping from inputs to class predictions.

### Q114 · MC

What target is normally used when training a basic autoencoder for reconstruction?

- A. A manually supplied class label.
- B. The discriminator's prediction.
- C. The original input itself.
- D. The nearest cluster centre.

### Q115 · MC

Compared with a basic deterministic autoencoder, a variational autoencoder typically:

- A. Encodes a distribution over latent variables and regularizes it toward a prior.
- B. Uses a discriminator instead of an encoder.
- C. Removes the reconstruction objective entirely.
- D. Prohibits sampling from the latent space.

### Q116 · MC

A GAN generator produces a few realistic-looking outputs repeatedly despite receiving many different noise inputs. What is this failure mode called?

- A. Mode collapse.
- B. Teacher forcing.
- C. Gradient clipping.
- D. Covariate normalization.

### Q117 · MC

Which description matches the basic diffusion-model procedure?

- A. Two classifiers compete to predict the correct semantic label.
- B. Sampling reconstructs only images already stored in the training set.
- C. The forward process classifies images and the reverse process sorts the classes.
- D. A fixed forward process adds noise; a learned reverse process progressively denoises to generate samples.

### Q118 · Short

In a GAN, what is the discriminator trained to distinguish, and what is the generator trying to achieve relative to that discriminator?

### Q119 · Short

Why might decoding an arbitrary random latent vector with a basic autoencoder give a poor result? What is the purpose of the KL regularization term in a VAE in this context?

### Q120 · Short

Compare the training objective of an autoregressive language model with that of a diffusion model at a conceptual level. In a text-conditioned image generator, what role does the text representation play?

# Supplement. Explainability, compression, and responsible evaluation

These questions come from the **Lab 4 MANOLO briefing**, not a separate numbered lecture module. Use them as supplementary theory practice. No legal dates, article numbers, or implementation-specific API details are required.

### Q121 · MC

A Grad-CAM heatmap is intended to highlight:

- A. Image regions that support a selected class score according to a gradient-based attribution method.
- B. The exact causal explanation for every possible model error.
- C. Only the pixels with the highest raw intensity.
- D. Pixels whose true semantic labels have been manually verified.

### Q122 · MC

What does FP32-to-INT8 quantization primarily change?

- A. The number of output classes.
- B. The spatial dimensions of every convolutional filter.
- C. The numerical representation and precision of model values.
- D. The definition of the target labels.

### Q123 · MC

Why might unstructured pruning fail to reduce measured inference latency when the model still uses dense tensors and dense kernels?

- A. Pruning removes training examples rather than weights.
- B. A zero weight requires more bits than a nonzero weight.
- C. The implementation may still store and process the zero entries.
- D. Pruning necessarily increases the number of layers.

### Q124 · MC

What is knowledge distillation?

- A. Replacing every floating-point weight with an integer without retraining.
- B. Training a smaller student to imitate a larger teacher's outputs or representations.
- C. Visualizing which image regions affect a class score.
- D. Deleting all weights below a chosen magnitude.

### Q125 · MC

After compression, overall accuracy is unchanged but recall for a rare class falls substantially. Which conclusion is justified?

- A. Recall is irrelevant once overall accuracy is known.
- B. Aggregate accuracy can hide important degradation, so per-class or subgroup evaluation is needed.
- C. The rare class must have incorrect labels.
- D. Compression has preserved all relevant aspects of performance.

### Q126 · Calculation

A model stores 1 million weights. Ignoring metadata and all other tensors, compare weight storage using 32 bits per weight with storage using 8 bits per weight. Give the two sizes in decimal MB ($1\,\mathrm{MB}=10^6$ bytes) and the reduction factor.

### Q127 · Short

A classifier predicts an object correctly, but its Grad-CAM map highlights a watermark in the background. What concern does this raise, and why is a plausible-looking heatmap alone insufficient to establish that a model is trustworthy?

### Q128 · Short

Name one risk of reusing a broadly pretrained model across many applications. Give one concrete check or mitigation relevant to that risk.

# Source map

All references below use **PDF page numbers counted from 1**, including title pages. The numbers refer to the current local PDFs, not older extracted notes or the printed slide numbers. Questions are newly written study exercises based on the listed concepts.

| Questions | Primary source and relevant PDF pages |
| --- | --- |
| Q001–Q006 | `0.1. Math background.pdf`, pp. 1–9: probability, expectation, Gaussian parameters, entropy, KL, likelihood. |
| Q007–Q014 | `1.1. Fundamentals.pdf`, pp. 6, 9–18, 26–44; `1.2. Shallow Learning.pdf`, pp. 13–25, 43. |
| Q015–Q026 | `1.2. Shallow Learning.pdf`, pp. 5–25, 34–40, 45–56, 60–67, 72–84. |
| Q027–Q034 | `1.3. Bayesian Learning.pdf`, pp. 5–19, 30–51. |
| Q035–Q039, Q045, Q047 | `2.1. Introduction to Reinforcement Learning.pdf`, conceptual introduction; `2.2. Markov decision processes.pdf`, pp. 2–24. |
| Q040–Q043, Q046, Q048–Q049 | `2.3. Q-learning.pdf`, pp. 6–10, 11–26, 28–44; deep function approximation also appears in `2.4. Policy Search.pdf`, p. 18. |
| Q044, Q050 | `2.4. Policy Search.pdf`, pp. 2–3, 6–17. |
| Q051 | `3.1. Introduction to Deep Learning.pdf`, pp. 30–39. |
| Q052–Q055, Q061 | `3.2. Shallow NN.pdf`, pp. 5–24, 26–42; `3.3. Deep Learning Fundamentals.pdf`, pp. 3–14. |
| Q056–Q057, Q062, Q064–Q065 | `3.3. Deep Learning Fundamentals.pdf`, pp. 17–44; `1.2. Shallow Learning.pdf`, pp. 27–32. |
| Q058–Q060, Q063, Q066 | `3.4. Deep Learning Fundamentals II.pdf`, pp. 7–24, 26–34, 44–53. |
| Q067–Q069, Q074–Q076 | `4.1. CNNs.pdf`, pp. 10–36. |
| Q070–Q073, Q077–Q078 | `4.1. CNNs.pdf`, pp. 51–62, 67–79, 90–93. |
| Q079–Q086 | `5.1. Sequence Models.pdf`, pp. 4–9, 13–22, 25–32; `5.1. Extra Material.pdf`, pp. 5–7, simplified to a single-component update. |
| Q087–Q098 | `5.2. Transformers.pdf`, pp. 8–36. |
| Q099–Q104 | `5.3. Foundation models.pdf`, pp. 10–22. |
| Q105–Q112 | `5.4. Unsupervised learning.pdf`, pp. 6–21, 25–36; PCA also in `1.2. Shallow Learning.pdf`, pp. 68–69. |
| Q113–Q120 | `5.5. Generative Models.pdf`, pp. 3–13, 17–22. |
| Q121–Q128 | `Lab Sessions/Lab4/manolo_presentation.pdf`, pp. 2, 5–11; foundation-model risks also in `5.3. Foundation models.pdf`, pp. 12, 26. |

Lecture PDFs are in `Lecture Slides/`. The administrative course-presentation deck establishes scope; it is not treated as a separate theory topic.
