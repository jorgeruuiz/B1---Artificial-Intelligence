---
title: "Artificial Intelligence: Two One-Hour Mock Papers"
subtitle: "Questions only · 23 October 2026"
author: "MAICE · Artificial Intelligence"
lang: en-GB
---

# Instructions

Each paper contains **20 multiple-choice questions and 8 short questions**, including **2 small calculations**. The papers contain different questions drawn from `AI_EXAM_PRACTICE_QUESTIONS.md`. They are suggested practice formats, not the teachers' announced question count or marking scheme.

Allow **60 minutes per paper**: 20 minutes for multiple choice, 32 minutes for short questions, and 8 minutes to review. Choose exactly one option for each MC question. Keep written responses to 1–3 sentences unless a short list is requested. For calculations, show a formula and substitution.

No answer key, marked options, or worked solutions are included. The bank identifiers are retained so you can locate each question and its source topic after finishing. The PDFs include writing space after short questions.

Use the source map in the full question bank to review the relevant slides after attempting a paper. The Lab 4 supplement is available in the bank but is not included in these two lecture-based mock papers.


# Paper A · Multiple choice

Suggested time: 20 minutes. Choose one best answer per question.


### 1. Q001 · MC

Which binary probability distribution has the greatest Shannon entropy?

- A. $(1.00, 0.00)$
- B. $(0.99, 0.01)$
- C. $(0.50, 0.50)$
- D. $(0.80, 0.20)$


### 2. Q008 · MC

You compare several hyperparameter settings. Which dataset should normally guide the choice, while preserving an independent final evaluation?

- A. The union of the training and test sets.
- B. The validation set, or validation folds within the training data.
- C. The test set, evaluated after every change.
- D. The training set alone.


### 3. Q010 · MC

In k-nearest-neighbour classification, increasing $k$ usually makes the decision boundary:

- A. Identical, because $k$ only affects inference speed.
- B. More irregular and more sensitive to individual examples.
- C. Smoother and less sensitive to individual training examples.
- D. Equivalent to the boundary of a linear SVM.


### 4. Q016 · MC

In ridge regression with objective $L(w)+\lambda\|w\|_2^2$, increasing $\lambda$ means:

- A. Increasing the number of polynomial features.
- B. Penalizing large coefficient magnitudes more strongly.
- C. Taking larger gradient steps.
- D. Giving less importance to large coefficient magnitudes.


### 5. Q018 · MC

A binary logistic-regression model outputs $p(y=1\mid x)=0.8$. Using a decision threshold of 0.5, what does this mean?

- A. The model has 80% accuracy on the dataset.
- B. It predicts class 1 and assigns that class probability 0.8 for this input.
- C. Exactly 80% of the input features indicate class 1.
- D. The true label is guaranteed to be 1.


### 6. Q028 · MC

In linear regression with Gaussian observation noise, a zero-mean isotropic Gaussian prior on the weights leads to which MAP penalty?

- A. An L2 penalty.
- B. An L1 penalty.
- C. A penalty on the validation error alone.
- D. A penalty on the number of observations.


### 7. Q030 · MC

For an RBF Gaussian-process kernel, increasing the length scale while keeping other hyperparameters fixed generally favours functions that:

- A. Have a larger observation-noise variance by definition.
- B. Become periodic.
- C. Vary more slowly, with correlation extending across larger input distances.
- D. Vary more rapidly over short input distances.


### 8. Q035 · MC

What does the Markov property require of a state representation?

- A. Given the current state and action, past history provides no additional information about the next-state distribution.
- B. All actions must have equal probability.
- C. The reward must depend on the full history.
- D. The next state must be deterministic.


### 9. Q037 · MC

What does setting the discount factor $\gamma=0$ do to the return objective?

- A. It prevents the agent from changing its policy.
- B. It makes all rewards equal to zero.
- C. It makes only the next immediate reward contribute.
- D. It makes all future rewards equally important.


### 10. Q042 · MC

Which next-action value appears in the standard Q-learning target?

- A. The average Q-value over all previous states.
- B. The value of the actual next action sampled from the behaviour policy.
- C. The minimum Q-value at the current state.
- D. The maximum Q-value over available actions at the next state.


### 11. Q053 · MC

For a ReLU unit whose input is strictly negative, its output and local derivative with respect to that input are:

- A. Output 0; derivative 0.
- B. Output negative; derivative 1.
- C. Output 0; derivative 1.
- D. Output positive; derivative 0.


### 12. Q057 · MC

For one example with a one-hot target, cross-entropy is $-\log p_{\text{true}}$. Which prediction receives the larger loss?

- A. It depends only on the number of hidden layers.
- B. A prediction assigning 0.1 to the true class.
- C. Both receive the same loss if their predicted class is correct.
- D. A prediction assigning 0.9 to the true class.


### 13. Q070 · MC

In a residual block $y=x+F(x)$ with matching shapes, what happens if $F(x)=0$?

- A. The block discards the input.
- B. The block implements the identity mapping.
- C. The block output becomes zero.
- D. The number of output channels doubles.


### 14. Q071 · MC

For standard batch normalization with stored running statistics, which statement is correct?

- A. Evaluation updates the convolution weights using test-batch statistics.
- B. Batch normalization has no learnable scale or shift parameters.
- C. Training and evaluation both recompute statistics from the test set.
- D. Training uses current mini-batch statistics; evaluation normally uses stored running statistics.


### 15. Q081 · MC

In an LSTM, a forget-gate value close to 1 primarily means:

- A. Completely erase the corresponding previous cell-state component.
- B. Prevent any output from being computed.
- C. Set the corresponding hidden-state component to exactly 1.
- D. Retain most of the corresponding previous cell-state component before adding the new contribution.


### 16. Q089 · MC

Why is the dot-product score divided by $\sqrt{d_k}$ in standard scaled attention?

- A. To control score magnitudes and reduce softmax saturation as key/query dimension grows.
- B. To reduce the number of token positions to $d_k$.
- C. To replace positional encoding.
- D. To make attention weights independent of the input.


### 17. Q091 · MC

At position $t$ in a decoder trained to predict the next token from tokens $1,\ldots,t$, a causal mask allows attention to:

- A. Positions $1,\ldots,t$, including the current input token.
- B. Future tokens only.
- C. Only position $t+1$.
- D. Every position except $t$.


### 18. Q099 · MC

Which property best characterizes a foundation model?

- A. It contains a fixed minimum number of layers.
- B. It is pretrained on broad data and can be adapted to many downstream tasks.
- C. It is defined by always using an encoder–decoder architecture.
- D. It is trained from scratch separately for each individual input.


### 19. Q109 · MC

In a standard contrastive objective with positive and negative pairs, training encourages:

- A. Positive-pair representations to become similar and negative-pair representations to remain separated.
- B. Positive-pair representations to move apart.
- C. Predictions to reproduce the raw input pixels exactly.
- D. Identical representations for every input.


### 20. Q116 · MC

A GAN generator produces a few realistic-looking outputs repeatedly despite receiving many different noise inputs. What is this failure mode called?

- A. Mode collapse.
- B. Teacher forcing.
- C. Gradient clipping.
- D. Covariate normalization.


# Paper A · Short questions

Suggested time: 32 minutes. Then use the final 8 minutes to review the whole paper.


### 21. Q022 · Calculation

For a chosen positive class, a classifier has $TP=30$, $FP=10$, and $FN=20$. Compute its precision and recall. Leave the results as fractions or percentages.


### 22. Q046 · Calculation

Perform one Q-learning update. The current value is $Q(s,a)=2$, the received reward is $r=1$, $\gamma=0.5$, $\alpha=0.5$, and $\max_{a'}Q(s',a')=6$. Compute the target $r+\gamma\max Q(s',a')$ and then the updated value $Q(s,a)+\alpha[\text{target}-Q(s,a)]$.


### 23. Q032 · Short

In $p(w\mid D)\propto p(D\mid w)p(w)$, identify the prior, likelihood, and posterior. Which expresses beliefs before observing this dataset?


### 24. Q064 · Short

What does mini-batch SGD change relative to full-batch gradient descent? Give one benefit and one consequence for the variability of the updates.


### 25. Q077 · Short

Distinguish feature extraction with a frozen pretrained network from fine-tuning. In each case, which weights are updated?


### 26. Q084 · Short

What is backpropagation through time? Why can repeated multiplication of derivatives make long-range dependencies difficult for a vanilla RNN to learn?


### 27. Q098 · Short

Why can a causal transformer compute next-token losses for all positions in a known training sequence in parallel, while ordinary autoregressive generation still produces new tokens sequentially?


### 28. Q119 · Short

Why might decoding an arbitrary random latent vector with a basic autoencoder give a poor result? What is the purpose of the KL regularization term in a VAE in this context?


# Paper B · Multiple choice

Suggested time: 20 minutes. Choose one best answer per question.


### 1. Q002 · MC

For two discrete probability distributions on the same finite set, what does $D_{KL}(p\|q)=0$ imply?

- A. They have disjoint supports.
- B. Both distributions are uniform.
- C. Their means agree, but their probabilities may differ.
- D. They assign identical probabilities to every outcome.


### 2. Q007 · MC

Which task is an example of unsupervised learning?

- A. Predicting house prices from examples with known prices.
- B. Classifying emails using examples labelled spam or not spam.
- C. Learning a robot policy from rewards.
- D. Grouping customers by similarity without predefined group labels.


### 3. Q011 · MC

What is an inductive bias?

- A. The assumptions that favour some patterns or solutions over others.
- B. The difference between the training and validation set sizes.
- C. The scalar intercept of every machine-learning model.
- D. The average prediction error on the training set.


### 4. Q017 · MC

Which regularizer is especially associated with producing exactly zero coefficients and therefore sparse models?

- A. A larger validation set.
- B. An L1 penalty on the coefficients.
- C. An L2 penalty on the coefficients.
- D. An increase in the learning rate.


### 5. Q019 · MC

A dataset contains 95% negative examples. A classifier predicts every example as negative. Which statement is correct?

- A. Its positive-class recall is 95%.
- B. Its accuracy is 95%, but its positive-class recall is 0%.
- C. Its high accuracy establishes that it detects positive examples well.
- D. Its accuracy and positive-class F1 score are both 95%.


### 6. Q020 · MC

For linearly separable data, a hard-margin SVM selects a separating hyperplane by:

- A. Minimizing the number of input features.
- B. Maximizing the margin to the closest training examples.
- C. Maximizing the distance to the average training example.
- D. Maximizing the number of support vectors.


### 7. Q027 · MC

Which statement best distinguishes full Bayesian parameter learning from maximum-likelihood or MAP point estimation?

- A. MAP keeps a distribution, but Bayesian learning keeps only its maximum.
- B. Bayesian learning keeps a distribution over plausible parameter values.
- C. Maximum likelihood requires a prior, but Bayesian learning does not.
- D. Bayesian learning removes the need for a likelihood.


### 8. Q031 · MC

What does the kernel $k(x,x')$ specify in a Gaussian process?

- A. The probability that $x$ and $x'$ have the same label.
- B. The posterior mean at $x$ for every dataset.
- C. The covariance between function values at $x$ and $x'$.
- D. The number of basis functions stored for each input.


### 9. Q039 · MC

What distinguishes a Bellman optimality backup from a Bellman expectation backup for a fixed policy?

- A. It removes the immediate reward.
- B. It averages uniformly over all actions.
- C. It sets the discount factor to 1.
- D. It chooses the best action instead of averaging actions according to the fixed policy.


### 10. Q040 · MC

Which statement correctly compares Monte Carlo policy evaluation with one-step TD evaluation?

- A. Both require an exact transition model.
- B. Monte Carlo bootstraps from the next state's value; TD always waits for the full return.
- C. Monte Carlo uses completed sampled returns; TD can update using a reward and an estimated successor value before an episode ends.
- D. TD does not use observed rewards.


### 11. Q044 · MC

In REINFORCE, sampled returns are used primarily to:

- A. Guarantee a global maximum of the policy objective.
- B. Weight policy-gradient updates so actions associated with better returns are reinforced.
- C. Supervise an exact transition-probability table.
- D. Replace the policy with a list of fixed class labels.


### 12. Q055 · MC

Why can depth be useful even when a shallow network has universal approximation capacity?

- A. Every extra layer guarantees lower test error.
- B. Some compositional functions can be represented much more efficiently using multiple layers.
- C. Deep models need no training examples.
- D. Depth removes the need for activation functions.


### 13. Q058 · MC

What does backpropagation compute?

- A. The generalization error without a validation set.
- B. The parameter update independently of any optimizer or learning rate.
- C. The optimal architecture for the dataset.
- D. Gradients of the loss with respect to parameters by applying the chain rule.


### 14. Q060 · MC

Which statement correctly describes standard dropout?

- A. It randomly deletes labels from the validation set.
- B. It randomly suppresses activations during training and is normally disabled during ordinary inference, with the appropriate scaling convention.
- C. It is an optimizer that accumulates past gradients.
- D. It deletes a fixed subset of units permanently before training.


### 15. Q067 · MC

Which pair of properties most directly reduces the parameter count of a convolutional layer compared with a fully connected layer on an image?

- A. Global connectivity and a separate bias for every input pixel.
- B. Larger input images and more output classes.
- C. Local connectivity and weight sharing across spatial positions.
- D. A separate filter for every pixel and no shared weights.


### 16. Q082 · MC

What is teacher forcing in sequence-to-sequence training?

- A. Feeding the correct previous token to the decoder during training.
- B. Selecting only the highest-probability token during every training step.
- C. Training the network without target sequences.
- D. Replacing the decoder with the encoder at inference time.


### 17. Q090 · MC

Why add positional information to an unmasked self-attention model?

- A. To ensure all words have different vocabulary indices.
- B. Self-attention alone is permutation equivariant and does not identify sequence positions.
- C. To make every attention weight equal.
- D. To remove the need for learned embeddings.


### 18. Q094 · MC

What does multi-head attention add to a single attention head?

- A. A new vocabulary for each position.
- B. A separate loss function that must be supervised for every head.
- C. An independent training dataset for each head.
- D. Several learned projection sets that can capture different relationships in parallel.


### 19. Q101 · MC

What is the main representation-learning objective of CLIP?

- A. Generate an image by iteratively removing Gaussian noise.
- B. Compress every image into a fixed handcrafted descriptor.
- C. Align corresponding images and text in a shared embedding space.
- D. Predict a separate semantic class for every image pixel using only masks.


### 20. Q117 · MC

Which description matches the basic diffusion-model procedure?

- A. Two classifiers compete to predict the correct semantic label.
- B. Sampling reconstructs only images already stored in the training set.
- C. The forward process classifies images and the reverse process sorts the classes.
- D. A fixed forward process adds noise; a learned reverse process progressively denoises to generate samples.


# Paper B · Short questions

Suggested time: 32 minutes. Then use the final 8 minutes to review the whole paper.


### 21. Q023 · Short

Using the standard definition $R^2=1-\mathrm{SSE}/\mathrm{SST}$ on a test set with nonconstant targets, interpret $R^2=1$, $R^2=0$, and $R^2<0$ relative to predicting the test-set mean.


### 22. Q050 · Short

In actor–critic learning, what is the actor's role and what is the critic's role? Compared with plain Monte Carlo policy gradients, what variance–bias trade-off can a learned critic introduce?


### 23. Q061 · Calculation

A fully connected layer has 3 inputs and 2 output units, with one bias per output unit. How many trainable scalar parameters does it have?


### 24. Q076 · Short

What is a unit's receptive field? How does dilation increase the spatial reach of a convolution without increasing the number of kernel weights?


### 25. Q086 · Short

What makes a temporal convolution causal? What must change if a temporal convolutional network needs to use information from much farther back in the sequence?


### 26. Q095 · Calculation

One attention query has normalized weights $(0.25,0.75)$ over two scalar values $v_1=2$ and $v_2=6$. Compute its attention output.


### 27. Q103 · Short

Distinguish supervised fine-tuning from preference-based reinforcement learning by stating the training signal used in each. What changes when rewards instead come from an automatic verifier, such as a unit test?


### 28. Q111 · Short

Give one self-supervised image pretext task from the slides. State what its target is and how that target is obtained without manually annotating semantic classes.
