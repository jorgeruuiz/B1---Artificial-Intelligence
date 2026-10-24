---
title: "Artificial Intelligence: Two One-Hour Mock Papers"
subtitle: "From the expanded slide-by-slide bank · Questions only"
author: "24 October 2026"
---

# Instructions

Each paper contains **20 multiple-choice questions and 8 short questions**, including **2 easy calculations**. Allow **60 minutes per paper**: 20 minutes for MC, 32 minutes for short questions, and 8 minutes to review. Choose one best option for each MC question. Keep written answers to 1–3 sentences unless a brief list is requested.

The papers use different questions from the expanded bank. Source titles, PDF page references, and stable question IDs are retained for review after your attempt. No answers, marked options, or worked solutions are included. The PDFs provide writing space for short answers.

**0. Presentation and 0.1. Math background are excluded.** The Lab 4 supplement is available separately in the bank. The question count and timing are suggested practice formats, not the teachers' confirmed marking scheme.


# Paper A · Multiple choice

Suggested time: 20 minutes.


### 1. 1.1-M05 · MC

*Source: [1.1. Fundamentals.pdf · PDF pp. 31–32, 41](../Lecture%20Slides/1.1.%20Fundamentals.pdf#page=31).*

Which split should guide hyperparameter selection while preserving an independent final evaluation?

- A. The validation set.
- B. All data merged together.
- C. The training labels alone.
- D. The test set after every experiment.


### 2. 1.2-M03 · MC

*Source: [1.2. Shallow Learning.pdf · PDF pp. 16–20](../Lecture%20Slides/1.2.%20Shallow%20Learning.pdf#page=16).*

Increasing $\lambda$ in $L(w)+\lambda\|w\|_2^2$ directly:

- A. Strengthens the penalty on large coefficient magnitudes.
- B. Removes the data-fit term.
- C. Increases the learning rate.
- D. Adds polynomial features.


### 3. 1.2-M06 · MC

*Source: [1.2. Shallow Learning.pdf · PDF pp. 60–65](../Lecture%20Slides/1.2.%20Shallow%20Learning.pdf#page=60).*

On data with 95% negatives, a classifier predicts every example as negative. Which is correct?

- A. Accuracy is 95%, but positive-class recall is 0%.
- B. Positive-class recall is 95%.
- C. Positive-class F1 is 95%.
- D. It detects most positive examples.


### 4. 1.3-M06 · MC

*Source: [1.3. Bayesian Learning.pdf · PDF pp. 30–35](../Lecture%20Slides/1.3.%20Bayesian%20Learning.pdf#page=30).*

A Gaussian process specifies that:

- A. Function values at any finite collection of inputs have a joint Gaussian distribution.
- B. All function values are independent.
- C. Input features must be Gaussian.
- D. Every sampled function is a Gaussian bell curve.


### 5. 2.1-M09 · MC

*Source: [2.1. Introduction to Reinforcement Learning.pdf · PDF pp. 14–16](../Lecture%20Slides/2.1.%20Introduction%20to%20Reinforcement%20Learning.pdf#page=14).*

What distinguishes planning with a known model from learning by interaction?

- A. Planning has no objective.
- B. Planning always needs human action labels.
- C. Learning needs deterministic transitions.
- D. Planning computes consequences using a model; learning obtains information from experience.


### 6. 2.2-M01 · MC

*Source: [2.2. Markov decision processes.pdf · PDF pp. 2–3](../Lecture%20Slides/2.2.%20Markov%20decision%20processes.pdf#page=2).*

The Markov property means that, given the current state and action:

- A. The history adds no information about the next-state distribution.
- B. The next state must be deterministic.
- C. All actions have equal value.
- D. Rewards must be positive.


### 7. 2.2-M07 · MC

*Source: [2.2. Markov decision processes.pdf · PDF pp. 12–15](../Lecture%20Slides/2.2.%20Markov%20decision%20processes.pdf#page=12).*

The Bellman expectation equation decomposes value into:

- A. Reward divided by the number of actions.
- B. Expected immediate reward plus discounted successor value.
- C. Prior probability and likelihood.
- D. Training error and validation error.


### 8. 2.3-M06 · MC

*Source: [2.3. Q-learning.pdf · PDF pp. 35–38](../Lecture%20Slides/2.3.%20Q-learning.pdf#page=35).*

The standard Q-learning target uses:

- A. The maximum next-state action value.
- B. The average value of all states.
- C. The actual sampled next action's value.
- D. The minimum current-state action value.


### 9. 2.4-M06 · MC

*Source: [2.4. Policy Search.pdf · PDF pp. 9–14](../Lecture%20Slides/2.4.%20Policy%20Search.pdf#page=9).*

In REINFORCE, sampled returns primarily:

- A. Guarantee the best trajectory is repeated exactly.
- B. Weight gradients of log action probabilities.
- C. Replace the environment model with correct labels.
- D. Remove the need to sample actions.


### 10. 3.1-M04 · MC

*Source: [3.1. Introduction to Deep Learning.pdf · PDF pp. 38–39](../Lecture%20Slides/3.1.%20Introduction%20to%20Deep%20Learning.pdf#page=38).*

What changes in an end-to-end deep classifier compared with a fixed handcrafted-feature pipeline?

- A. Feature extraction can be optimized jointly with the prediction stage.
- B. It no longer needs a prediction objective.
- C. Evaluation becomes unnecessary.
- D. It no longer needs training data.


### 11. 3.2-M05 · MC

*Source: [3.2. Shallow NN.pdf · PDF pp. 23–24](../Lecture%20Slides/3.2.%20Shallow%20NN.pdf#page=23).*

The universal approximation theorem establishes, under its usual assumptions:

- A. SGD always finds the best approximation.
- B. Perfect generalization from a finite dataset.
- C. Sufficiently wide shallow networks can approximate continuous functions on compact domains arbitrarily well.
- D. One hidden unit is enough for every function.


### 12. 3.3-M06 · MC

*Source: [3.3. Deep Learning Fundamentals.pdf · PDF pp. 24–26](../Lecture%20Slides/3.3.%20Deep%20Learning%20Fundamentals.pdf#page=24).*

For one-hot targets, cross-entropy $-\log p_{true}$ is smaller when:

- A. The parameter count is larger, regardless of predictions.
- B. The true class receives a larger probability.
- C. The true class probability is ignored.
- D. The true class receives a smaller probability.


### 13. 3.4-M08 · MC

*Source: [3.4. Deep Learning Fundamentals II.pdf · PDF pp. 32, 34](../Lecture%20Slides/3.4.%20Deep%20Learning%20Fundamentals%20II.pdf#page=32).*

Standard dropout during training:

- A. Drops only incorrect training examples.
- B. Is normally applied unchanged during ordinary inference.
- C. Randomly suppresses some activations and uses an appropriate scaling convention.
- D. Permanently deletes a fixed subset of units.


### 14. 4.1-M08 · MC

*Source: [4.1. CNNs.pdf · PDF pp. 55–59](../Lecture%20Slides/4.1.%20CNNs.pdf#page=55).*

Standard batch normalization with running statistics normally uses:

- A. The current evaluation batch for every deployment prediction.
- B. No learned scale or shift.
- C. Test-set statistics to fit its training parameters.
- D. Batch statistics during training and stored statistics during evaluation.


### 15. 5.1-M09 · MC

*Source: [5.1. Sequence Models.pdf · PDF pp. 28–29](../Lecture%20Slides/5.1.%20Sequence%20Models.pdf#page=28).*

Teacher forcing feeds the decoder:

- A. The final target sentence as a single class label.
- B. Only its own mistakes during training.
- C. The ground-truth next token at inference time.
- D. The ground-truth previous token during training.


### 16. 5.1E-M09 · MC

*Source: [5.1. Extra Material.pdf · PDF pp. 6](../Lecture%20Slides/5.1.%20Extra%20Material.pdf#page=6).*

Which quantities normally change while a trained LSTM reads a sequence without training updates?

- A. Vocabulary size at every step.
- B. All layer dimensions at every step.
- C. Only the weights.
- D. $c_t$ and $h_t$, while learned weights stay fixed.


### 17. 5.2-M08 · MC

*Source: [5.2. Transformers.pdf · PDF pp. 30–31](../Lecture%20Slides/5.2.%20Transformers.pdf#page=30).*

At input position $t$ predicting token $t+1$, the usual causal mask permits attention to:

- A. Only position $t+1$.
- B. Only future positions.
- C. Input positions $1,\ldots,t$.
- D. Every position except $t$.


### 18. 5.3-M06 · MC

*Source: [5.3. Foundation models.pdf · PDF pp. 19–20](../Lecture%20Slides/5.3.%20Foundation%20models.pdf#page=19).*

CLIP learns:

- A. A separate encoder for every future class name.
- B. A transition model for an RL environment.
- C. A shared representation space for images and text.
- D. Only a pixel reconstruction model.


### 19. 5.4-M03 · MC

*Source: [5.4. Unsupervised learning.pdf · PDF pp. 13–18, 36](../Lecture%20Slides/5.4.%20Unsupervised%20learning.pdf#page=13).*

A defensible interpretation of t-SNE is that it mainly aims to preserve:

- A. All pairwise distances exactly.
- B. Local neighbourhood structure in a low-dimensional visualization.
- C. Cluster sizes as exact population proportions.
- D. Only the covariance eigenvalues.


### 20. 5.5-M08 · MC

*Source: [5.5. Generative Models.pdf · PDF pp. 13](../Lecture%20Slides/5.5.%20Generative%20Models.pdf#page=13).*

A generator produces only a few similar outputs despite varied noise inputs. This is:

- A. Feature normalization.
- B. Gradient clipping.
- C. Teacher forcing.
- D. Mode collapse.


# Paper A · Short questions

Suggested time: 32 minutes, then 8 minutes to review the paper.


### 21. 1.2-C01 · Calculation

*Source: [1.2. Shallow Learning.pdf · PDF pp. 60–61](../Lecture%20Slides/1.2.%20Shallow%20Learning.pdf#page=60).*

A classifier has $TP=30$, $FP=10$, and $FN=20$. Compute positive-class precision and recall.


### 22. 3.2-C01 · Calculation

*Source: [3.2. Shallow NN.pdf · PDF pp. 39–42](../Lecture%20Slides/3.2.%20Shallow%20NN.pdf#page=39).*

A fully connected shallow network has 2 inputs, 3 hidden units, and 1 output. Include one bias for every hidden and output unit. Compute the total number of trainable parameters.


### 23. 1.3-S03 · Short

*Source: [1.3. Bayesian Learning.pdf · PDF pp. 14](../Lecture%20Slides/1.3.%20Bayesian%20Learning.pdf#page=14).*

Distinguish uncertainty about the latent function from observation noise. Which can often be reduced by additional informative data?


### 24. 2.3-S04 · Short

*Source: [2.3. Q-learning.pdf · PDF pp. 29, 35–38](../Lecture%20Slides/2.3.%20Q-learning.pdf#page=29).*

At the next state, the behaviour policy chooses a low-value exploratory action. How can the SARSA and Q-learning targets differ?


### 25. 2.4-S06 · Short

*Source: [2.4. Policy Search.pdf · PDF pp. 17](../Lecture%20Slides/2.4.%20Policy%20Search.pdf#page=17).*

State the actor's and critic's roles in one sentence each. Which one directly determines action probabilities?


### 26. 4.1-S05 · Short

*Source: [4.1. CNNs.pdf · PDF pp. 67–73](../Lecture%20Slides/4.1.%20CNNs.pdf#page=67).*

Distinguish frozen feature extraction from fine-tuning. Which weights change in each case?


### 27. 5.2-S04 · Short

*Source: [5.2. Transformers.pdf · PDF pp. 30–31](../Lecture%20Slides/5.2.%20Transformers.pdf#page=30).*

Why can next-token training evaluate all known sequence positions in parallel while ordinary autoregressive generation produces new tokens sequentially?


### 28. 5.5-S06 · Short

*Source: [5.5. Generative Models.pdf · PDF pp. 17–18](../Lecture%20Slides/5.5.%20Generative%20Models.pdf#page=17).*

Distinguish the fixed forward noising process from the learned reverse process in diffusion.


# Paper B · Multiple choice

Suggested time: 20 minutes.


### 1. 1.1-M09 · MC

*Source: [1.1. Fundamentals.pdf · PDF pp. 26](../Lecture%20Slides/1.1.%20Fundamentals.pdf#page=26).*

A model finds a strong correlation between two variables. What follows?

- A. The association alone does not establish causation.
- B. Confounding variables can be ruled out.
- C. The first variable necessarily causes the second.
- D. The second variable necessarily causes the first.


### 2. 1.2-M08 · MC

*Source: [1.2. Shallow Learning.pdf · PDF pp. 72–76](../Lecture%20Slides/1.2.%20Shallow%20Learning.pdf#page=72).*

The hard-margin SVM chooses a separating hyperplane that:

- A. Maximizes the margin to the closest examples.
- B. Minimizes the margin to the closest examples.
- C. Maximizes the number of features.
- D. Passes through the class means.


### 3. 1.2-M10 · MC

*Source: [1.2. Shallow Learning.pdf · PDF pp. 82–84](../Lecture%20Slides/1.2.%20Shallow%20Learning.pdf#page=82).*

Which distinction between bagging and boosting is correct?

- A. Bagging uses only one model.
- B. Random forests are linear regressors.
- C. Boosting requires independent learners.
- D. Bagging combines resampled learners; boosting builds learners sequentially to address remaining errors.


### 4. 1.3-M08 · MC

*Source: [1.3. Bayesian Learning.pdf · PDF pp. 38, 46–47](../Lecture%20Slides/1.3.%20Bayesian%20Learning.pdf#page=38).*

A larger RBF length scale generally favours:

- A. Higher noise variance by definition.
- B. More rapid variation across nearby inputs.
- C. Correlations extending over larger input distances.
- D. Periodicity with a shorter period.


### 5. 2.1-M04 · MC

*Source: [2.1. Introduction to Reinforcement Learning.pdf · PDF pp. 8–9](../Lecture%20Slides/2.1.%20Introduction%20to%20Reinforcement%20Learning.pdf#page=8).*

In stochastic gridworld, choosing North means:

- A. The state is necessarily unobservable.
- B. The successor cell must be North.
- C. The policy is necessarily random.
- D. Actual movement is sampled from a transition distribution.


### 6. 2.2-M10 · MC

*Source: [2.2. Markov decision processes.pdf · PDF pp. 20–24](../Lecture%20Slides/2.2.%20Markov%20decision%20processes.pdf#page=20).*

Policy iteration repeatedly alternates:

- A. Clustering and dimensionality reduction.
- B. Policy evaluation and policy improvement.
- C. Random action selection and restarting all values.
- D. Reward deletion and state deletion.


### 7. 2.3-M10 · MC

*Source: [2.3. Q-learning.pdf · PDF pp. 47](../Lecture%20Slides/2.3.%20Q-learning.pdf#page=47).*

Which three ingredients form the deadly triad associated with instability?

- A. Discounting, rewards, terminal states.
- B. Function approximation, bootstrapping, off-policy learning.
- C. Exploration, deterministic policies, finite horizons.
- D. Labels, minibatches, cross-entropy.


### 8. 2.4-M03 · MC

*Source: [2.4. Policy Search.pdf · PDF pp. 6–7](../Lecture%20Slides/2.4.%20Policy%20Search.pdf#page=6).*

The policy objective $J(\theta)$ is typically:

- A. The negative transition probability.
- B. The number of policy parameters.
- C. Expected return under the parameterized policy.
- D. A supervised class-accuracy score by definition.


### 9. 3.1-M07 · MC

*Source: [3.1. Introduction to Deep Learning.pdf · PDF pp. 26–34](../Lecture%20Slides/3.1.%20Introduction%20to%20Deep%20Learning.pdf#page=26).*

Which is the most useful first check for a large training dataset?

- A. Whether its examples, labels, and variability suit the intended task.
- B. Whether every image has the same filename length.
- C. Whether the network can memorize its row order.
- D. Whether the file is larger than all previous datasets.


### 10. 3.2-M07 · MC

*Source: [3.2. Shallow NN.pdf · PDF pp. 26–28](../Lecture%20Slides/3.2.%20Shallow%20NN.pdf#page=26).*

In a shallow network with two outputs and one shared hidden layer:

- A. The hidden units cannot be shared.
- B. The two outputs require identical output biases.
- C. Each output must equal the other.
- D. Each output can use a different weighted combination of the same hidden activations.


### 11. 3.3-M10 · MC

*Source: [3.3. Deep Learning Fundamentals.pdf · PDF pp. 40–42](../Lecture%20Slides/3.3.%20Deep%20Learning%20Fundamentals.pdf#page=40).*

Adam combines momentum-like information with:

- A. Exact Hessian inversion at every step.
- B. A rule that all parameters share identical gradients.
- C. Per-parameter scaling based on squared-gradient statistics.
- D. Removal of the learning rate.


### 12. 3.4-M03 · MC

*Source: [3.4. Deep Learning Fundamentals II.pdf · PDF pp. 10–16](../Lecture%20Slides/3.4.%20Deep%20Learning%20Fundamentals%20II.pdf#page=10).*

If a parameter influences loss through two computational paths, its gradient receives:

- A. Only the larger contribution.
- B. Only the first path's contribution.
- C. The sum of contributions from both paths.
- D. Their average regardless of the computation.


### 13. 4.1-M06 · MC

*Source: [4.1. CNNs.pdf · PDF pp. 36](../Lecture%20Slides/4.1.%20CNNs.pdf#page=36).*

A stride-1 $1\times1$ convolution primarily:

- A. Expands the spatial receptive field to $3\times3$.
- B. Mixes channels at each location and can change channel count.
- C. Removes all channel information.
- D. Pools neighbouring pixels.


### 14. 4.1-M10 · MC

*Source: [4.1. CNNs.pdf · PDF pp. 90–93](../Lecture%20Slides/4.1.%20CNNs.pdf#page=90).*

Instance segmentation differs from semantic segmentation by:

- A. Assigning no class labels to objects.
- B. Avoiding pixel-level outputs.
- C. Predicting only one class for the whole image.
- D. Separating distinct objects even when they have the same class.


### 15. 5.1-M07 · MC

*Source: [5.1. Sequence Models.pdf · PDF pp. 21](../Lecture%20Slides/5.1.%20Sequence%20Models.pdf#page=21).*

Relative to an LSTM, the usual GRU:

- A. Has an additional separate cell state.
- B. Cannot process variable-length sequences.
- C. Has update/reset gates and no separate LSTM-style cell state.
- D. Uses no gates.


### 16. 5.1E-M08 · MC

*Source: [5.1. Extra Material.pdf · PDF pp. 2–4, 7](../Lecture%20Slides/5.1.%20Extra%20Material.pdf#page=2).*

The output gate primarily controls:

- A. The size of the vocabulary.
- B. The number of stored training sequences.
- C. How much of the transformed cell state is exposed as hidden output.
- D. Which input column is selected.


### 17. 5.2-M09 · MC

*Source: [5.2. Transformers.pdf · PDF pp. 32–35](../Lecture%20Slides/5.2.%20Transformers.pdf#page=32).*

In encoder–decoder cross-attention:

- A. Queries come from decoder representations; keys and values come from encoder output.
- B. Queries, keys, and values must all come from the same sequence.
- C. The encoder queries future decoder outputs.
- D. Keys are the future target labels.


### 18. 5.3-M05 · MC

*Source: [5.3. Foundation models.pdf · PDF pp. 14](../Lecture%20Slides/5.3.%20Foundation%20models.pdf#page=14).*

Which is an example of a verifiable reward?

- A. A random score independent of the output.
- B. The number of training parameters alone.
- C. Whether generated code passes specified unit tests.
- D. A manually supplied next-token label by definition.


### 19. 5.4-M10 · MC

*Source: [5.4. Unsupervised learning.pdf · PDF pp. 30–31](../Lecture%20Slides/5.4.%20Unsupervised%20learning.pdf#page=30).*

The basic BYOL approach is notable for:

- A. Needing a separate classifier for every image.
- B. Learning from two views using online/target networks without explicit negatives.
- C. Requiring manually labelled negative examples.
- D. Replacing the encoder with k-means.


### 20. 5.5-M05 · MC

*Source: [5.5. Generative Models.pdf · PDF pp. 8](../Lecture%20Slides/5.5.%20Generative%20Models.pdf#page=8).*

The KL regularization term in a VAE encourages:

- A. Removal of the reconstruction objective.
- B. Every reconstruction to be identical.
- C. Infinite latent variance for every input.
- D. The latent distribution to agree with a chosen prior.


# Paper B · Short questions

Suggested time: 32 minutes, then 8 minutes to review the paper.


### 21. 2.3-C01 · Calculation

*Source: [2.3. Q-learning.pdf · PDF pp. 35–36](../Lecture%20Slides/2.3.%20Q-learning.pdf#page=35).*

Perform one Q-learning update with $Q(s,a)=2$, $r=1$, $\gamma=0.5$, $\alpha=0.5$, and $\max_{a'}Q(s',a')=6$. First compute the target, then $Q_{new}=Q+\alpha(\text{target}-Q)$.


### 22. 4.1-C01 · Calculation

*Source: [4.1. CNNs.pdf · PDF pp. 15–17](../Lecture%20Slides/4.1.%20CNNs.pdf#page=15).*

A $7\times7$ input is convolved with a $3\times3$ kernel, stride 2, padding 1 per side, and dilation 1. Use $W_{out}=\lfloor(W-K+2P)/S\rfloor+1$ to compute output height and width.


### 23. 1.1-S04 · Short

*Source: [1.1. Fundamentals.pdf · PDF pp. 6, 30, 33–36](../Lecture%20Slides/1.1.%20Fundamentals.pdf#page=6).*

Distinguish a learned parameter from a hyperparameter. In k-NN, which is $k$?


### 24. 3.3-S05 · Short

*Source: [3.3. Deep Learning Fundamentals.pdf · PDF pp. 32–37](../Lecture%20Slides/3.3.%20Deep%20Learning%20Fundamentals.pdf#page=32).*

What can happen if the learning rate is too high? What if it is extremely low?


### 25. 3.4-S01 · Short

*Source: [3.4. Deep Learning Fundamentals II.pdf · PDF pp. 7–22](../Lecture%20Slides/3.4.%20Deep%20Learning%20Fundamentals%20II.pdf#page=7).*

Distinguish the forward pass, backward pass, and optimizer step. Which computes predictions and which changes weights?


### 26. 5.1-S06 · Short

*Source: [5.1. Sequence Models.pdf · PDF pp. 29](../Lecture%20Slides/5.1.%20Sequence%20Models.pdf#page=29).*

What is exposure bias in a teacher-forced decoder? Why can an early inference-time mistake affect later outputs?


### 27. 5.3-S04 · Short

*Source: [5.3. Foundation models.pdf · PDF pp. 14](../Lecture%20Slides/5.3.%20Foundation%20models.pdf#page=14).*

Distinguish human demonstrations, preference rankings, and automatically verifiable rewards as training signals.


### 28. 5.4-S06 · Short

*Source: [5.4. Unsupervised learning.pdf · PDF pp. 28–31](../Lecture%20Slides/5.4.%20Unsupervised%20learning.pdf#page=28).*

What is representation collapse? Why would mapping every input to the same vector be unhelpful for downstream tasks?
