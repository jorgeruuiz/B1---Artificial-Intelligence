---
title: "Artificial Intelligence: Slide-by-Slide Exam Practice"
subtitle: "10 multiple choice + 7 short answers + 3 easy calculations per deck"
author: "Questions only · 24 October 2026"
---

# How to use this question bank

**380 questions, with no answers or worked solutions:** 360 questions for the 18 teaching PDFs, plus a separate 20-question Lab 4 supplement. **0. Presentation and 0.1. Math background are excluded.** Each teaching PDF has its own section, using its exact filename title. The separate **5.1. Extra Material** PDF has its own LSTM section, identified by `5.1E` in question IDs.

Every section contains exactly:

- **M01–M10: 10 multiple-choice questions.** Choose one best answer from A–D.
- **S01–S07: 7 short-answer questions.** Aim for 1–3 sentences, or a few brief points when asked.
- **C01–C03: 3 easy calculation problems.** Show a short calculation; no long derivations or multi-step training simulations are needed.

Questions prioritize definitions, the meaning of values and hyperparameters, distinctions between methods, and small applications of the concepts. Parameter counts include biases only when stated. Numerical examples are newly constructed practice applications; the source pages identify the underlying concept, not necessarily an identical exercise in the slides. Introductory decks use simple data or representation calculations appropriate to their content.

**Source references count PDF pages from 1, including title pages**, rather than using printed slide numbers. Each question has a page reference under its ID. For example, `3.2-C01` is calculation 1 from **3.2. Shallow NN.pdf**. Click the source reference to open the relevant local PDF.

This is a revision bank, not one exam. A useful deck-level session is about 30–40 minutes. For full-course timing, the accompanying **AI_EXAM_MOCK_PAPERS.pdf** contains two different one-hour papers: 20 MC questions and 8 short questions each, including 2 calculations. Allow 20 minutes for MC, 32 minutes for short questions, and 8 minutes to review. These are practice formats, not a prediction of the teachers' question count or topic weighting.


# 1.1. Fundamentals

**Slides:** [1.1. Fundamentals.pdf](../Lecture%20Slides/1.1.%20Fundamentals.pdf). **20 questions: 10 MC · 7 short answers · 3 easy calculations.**


## Multiple choice


### 1.1-M01 · MC

*Source: [PDF pp. 10–14](../Lecture%20Slides/1.1.%20Fundamentals.pdf#page=10).*

Predicting a house's selling price from examples with known prices is:

- A. Reinforcement learning.
- B. Unsupervised clustering.
- C. Supervised regression.
- D. Supervised classification.


### 1.1-M02 · MC

*Source: [PDF pp. 15–18](../Lecture%20Slides/1.1.%20Fundamentals.pdf#page=15).*

Which task is unsupervised learning?

- A. Fitting a curve to known targets.
- B. Predicting labelled disease categories.
- C. Learning actions from rewards.
- D. Grouping observations without predefined group labels.


### 1.1-M03 · MC

*Source: [PDF pp. 18–21](../Lecture%20Slides/1.1.%20Fundamentals.pdf#page=18).*

What distinguishes reinforcement learning from ordinary supervised learning?

- A. It uses adjustable model parameters.
- B. Actions affect future experience, and feedback takes the form of rewards.
- C. It always receives the correct action label.
- D. It can use numerical inputs.


### 1.1-M04 · MC

*Source: [PDF pp. 6](../Lecture%20Slides/1.1.%20Fundamentals.pdf#page=6).*

An inductive bias is:

- A. The average training error.
- B. The scalar intercept of any model.
- C. An error caused only by unbalanced data.
- D. An assumption that favours certain patterns or solutions.


### 1.1-M05 · MC

*Source: [PDF pp. 31–32, 41](../Lecture%20Slides/1.1.%20Fundamentals.pdf#page=31).*

Which split should guide hyperparameter selection while preserving an independent final evaluation?

- A. The validation set.
- B. All data merged together.
- C. The training labels alone.
- D. The test set after every experiment.


### 1.1-M06 · MC

*Source: [PDF pp. 31–32, 41](../Lecture%20Slides/1.1.%20Fundamentals.pdf#page=31).*

What is the main purpose of a held-out test set?

- A. Fit model weights.
- B. Estimate performance on unseen data after model selection.
- C. Increase training-set size during evaluation.
- D. Select preprocessing settings repeatedly.


### 1.1-M07 · MC

*Source: [PDF pp. 33–36](../Lecture%20Slides/1.1.%20Fundamentals.pdf#page=33).*

Increasing $k$ in k-NN classification usually makes predictions:

- A. Independent of the training data.
- B. Equivalent to a linear classifier.
- C. More sensitive to single noisy neighbours.
- D. Smoother and less sensitive to individual examples.


### 1.1-M08 · MC

*Source: [PDF pp. 33–34](../Lecture%20Slides/1.1.%20Fundamentals.pdf#page=33).*

What does standard k-NN need at prediction time?

- A. Only one learned slope and intercept.
- B. A reward function.
- C. Stored training examples and a distance rule.
- D. Only the class frequencies.


### 1.1-M09 · MC

*Source: [PDF pp. 26](../Lecture%20Slides/1.1.%20Fundamentals.pdf#page=26).*

A model finds a strong correlation between two variables. What follows?

- A. The association alone does not establish causation.
- B. Confounding variables can be ruled out.
- C. The first variable necessarily causes the second.
- D. The second variable necessarily causes the first.


### 1.1-M10 · MC

*Source: [PDF pp. 27–30](../Lecture%20Slides/1.1.%20Fundamentals.pdf#page=27).*

Why might a very large training dataset still give poor deployment performance?

- A. Its examples may poorly represent the deployment population.
- B. Generalization depends only on sample count.
- C. Large datasets cannot contain labels.
- D. More examples necessarily increase estimation error.


## Short answers


### 1.1-S01 · Short

*Source: [PDF pp. 10–17](../Lecture%20Slides/1.1.%20Fundamentals.pdf#page=10).*

Distinguish classification from regression using the type of output. Give one example of each.


### 1.1-S02 · Short

*Source: [PDF pp. 31–32, 41](../Lecture%20Slides/1.1.%20Fundamentals.pdf#page=31).*

What are the roles of training, validation, and test data? Use one short phrase per split.


### 1.1-S03 · Short

*Source: [PDF pp. 31–32, 41](../Lecture%20Slides/1.1.%20Fundamentals.pdf#page=31).*

Why can repeatedly choosing models using test results make reported test performance misleading?


### 1.1-S04 · Short

*Source: [PDF pp. 6, 30, 33–36](../Lecture%20Slides/1.1.%20Fundamentals.pdf#page=6).*

Distinguish a learned parameter from a hyperparameter. In k-NN, which is $k$?


### 1.1-S05 · Short

*Source: [PDF pp. 33–36](../Lecture%20Slides/1.1.%20Fundamentals.pdf#page=33).*

A k-NN model uses height in metres and income in euros with Euclidean distance. Why might scaling matter?


### 1.1-S06 · Short

*Source: [PDF pp. 6](../Lecture%20Slides/1.1.%20Fundamentals.pdf#page=6).*

What practical lesson does the No Free Lunch idea give about choosing a learning algorithm before examining the problem and data?


### 1.1-S07 · Short

*Source: [PDF pp. 27–30, 42–44](../Lecture%20Slides/1.1.%20Fundamentals.pdf#page=27).*

A dataset contains many near-duplicate images from one camera. Why might adding varied examples help more than adding more such duplicates?


## Easy calculations


### 1.1-C01 · Calculation

*Source: [PDF pp. 33–34](../Lecture%20Slides/1.1.%20Fundamentals.pdf#page=33).*

The five nearest neighbours have labels A, B, A, A, B. What class does unweighted 5-NN predict, and what fraction of neighbours support it?


### 1.1-C02 · Calculation

*Source: [PDF pp. 33–34](../Lecture%20Slides/1.1.%20Fundamentals.pdf#page=33).*

For k-NN regression, suppose the rule is to average neighbours' targets. The three nearest targets are 2, 4, and 6. Compute the prediction.


### 1.1-C03 · Calculation

*Source: [PDF pp. 31–32](../Lecture%20Slides/1.1.%20Fundamentals.pdf#page=31).*

Split 1,000 examples into 70% training, 15% validation, and the remainder for testing. How many examples are in each split?


# 1.2. Shallow Learning

**Slides:** [1.2. Shallow Learning.pdf](../Lecture%20Slides/1.2.%20Shallow%20Learning.pdf). **20 questions: 10 MC · 7 short answers · 3 easy calculations.**


## Multiple choice


### 1.2-M01 · MC

*Source: [PDF pp. 5, 11–12](../Lecture%20Slides/1.2.%20Shallow%20Learning.pdf#page=5).*

Why is $\hat y=w_0+w_1x+w_2x^2$ linear regression with polynomial features?

- A. It has only one coefficient.
- B. It is a straight line in $x$.
- C. It needs no loss function.
- D. It is linear in the fitted coefficients.


### 1.2-M02 · MC

*Source: [PDF pp. 7–8](../Lecture%20Slides/1.2.%20Shallow%20Learning.pdf#page=7).*

Least-squares regression corresponds to maximum likelihood under which noise assumption?

- A. Uniform noise with unknown support.
- B. Independent Gaussian noise with fixed common variance.
- C. Noise that is always zero.
- D. Bernoulli noise on continuous targets.


### 1.2-M03 · MC

*Source: [PDF pp. 16–20](../Lecture%20Slides/1.2.%20Shallow%20Learning.pdf#page=16).*

Increasing $\lambda$ in $L(w)+\lambda\|w\|_2^2$ directly:

- A. Strengthens the penalty on large coefficient magnitudes.
- B. Removes the data-fit term.
- C. Increases the learning rate.
- D. Adds polynomial features.


### 1.2-M04 · MC

*Source: [PDF pp. 19](../Lecture%20Slides/1.2.%20Shallow%20Learning.pdf#page=19).*

Which penalty is particularly associated with exactly zero coefficients?

- A. A squared residual penalty alone.
- B. A larger validation set.
- C. An L1 weight penalty.
- D. An L2 weight penalty.


### 1.2-M05 · MC

*Source: [PDF pp. 49–53](../Lecture%20Slides/1.2.%20Shallow%20Learning.pdf#page=49).*

Logistic regression outputs $p(y=1\mid x)=0.8$. What does this express?

- A. The dataset's overall accuracy.
- B. A guarantee that the true class is 1.
- C. The proportion of correctly fitted coefficients.
- D. The model's probability for class 1 on this input.


### 1.2-M06 · MC

*Source: [PDF pp. 60–65](../Lecture%20Slides/1.2.%20Shallow%20Learning.pdf#page=60).*

On data with 95% negatives, a classifier predicts every example as negative. Which is correct?

- A. Accuracy is 95%, but positive-class recall is 0%.
- B. Positive-class recall is 95%.
- C. Positive-class F1 is 95%.
- D. It detects most positive examples.


### 1.2-M07 · MC

*Source: [PDF pp. 63–64](../Lecture%20Slides/1.2.%20Shallow%20Learning.pdf#page=63).*

For fixed scores, lowering the positive-class decision threshold:

- A. Decreases both true positives and false positives.
- B. Guarantees increased precision.
- C. Changes the learned coefficients.
- D. Cannot decrease recall, but can increase false positives.


### 1.2-M08 · MC

*Source: [PDF pp. 72–76](../Lecture%20Slides/1.2.%20Shallow%20Learning.pdf#page=72).*

The hard-margin SVM chooses a separating hyperplane that:

- A. Maximizes the margin to the closest examples.
- B. Minimizes the margin to the closest examples.
- C. Maximizes the number of features.
- D. Passes through the class means.


### 1.2-M09 · MC

*Source: [PDF pp. 78–79](../Lecture%20Slides/1.2.%20Shallow%20Learning.pdf#page=78).*

The kernel trick allows an SVM to:

- A. Convert every task into clustering.
- B. Avoid any similarity computation.
- C. Learn without training examples.
- D. Compute feature-space inner products without explicitly constructing the feature vectors.


### 1.2-M10 · MC

*Source: [PDF pp. 82–84](../Lecture%20Slides/1.2.%20Shallow%20Learning.pdf#page=82).*

Which distinction between bagging and boosting is correct?

- A. Bagging uses only one model.
- B. Random forests are linear regressors.
- C. Boosting requires independent learners.
- D. Bagging combines resampled learners; boosting builds learners sequentially to address remaining errors.


## Short answers


### 1.2-S01 · Short

*Source: [PDF pp. 13–15, 21–25](../Lecture%20Slides/1.2.%20Shallow%20Learning.pdf#page=13).*

Training error is low but validation error is high. Name the likely problem and one appropriate change to try.


### 1.2-S02 · Short

*Source: [PDF pp. 34–39](../Lecture%20Slides/1.2.%20Shallow%20Learning.pdf#page=34).*

Why are squared residuals sensitive to outliers? Name one robust alternative from the slides.


### 1.2-S03 · Short

*Source: [PDF pp. 40](../Lecture%20Slides/1.2.%20Shallow%20Learning.pdf#page=40).*

Using $R^2=1-\mathrm{SSE}/\mathrm{SST}$ on a nonconstant test target, interpret $R^2=1$, $R^2=0$, and $R^2<0$ relative to the test-mean predictor.


### 1.2-S04 · Short

*Source: [PDF pp. 60–65](../Lecture%20Slides/1.2.%20Shallow%20Learning.pdf#page=60).*

Distinguish precision from recall in words. Which measures the fraction of actual positives detected?


### 1.2-S05 · Short

*Source: [PDF pp. 65](../Lecture%20Slides/1.2.%20Shallow%20Learning.pdf#page=65).*

What two metrics does F1 combine? Why is a large value of only one insufficient for a high F1?


### 1.2-S06 · Short

*Source: [PDF pp. 68–71](../Lecture%20Slides/1.2.%20Shallow%20Learning.pdf#page=68).*

Distinguish the goals of PCA and k-means. Does either require class labels for its usual fitting procedure?


### 1.2-S07 · Short

*Source: [PDF pp. 81–84](../Lecture%20Slides/1.2.%20Shallow%20Learning.pdf#page=81).*

What does a decision-tree split do? Why can a deep tree overfit, and how can averaging randomized trees help?


## Easy calculations


### 1.2-C01 · Calculation

*Source: [PDF pp. 60–61](../Lecture%20Slides/1.2.%20Shallow%20Learning.pdf#page=60).*

A classifier has $TP=30$, $FP=10$, and $FN=20$. Compute positive-class precision and recall.


### 1.2-C02 · Calculation

*Source: [PDF pp. 40](../Lecture%20Slides/1.2.%20Shallow%20Learning.pdf#page=40).*

Two predictions have residuals $y-\hat y$ equal to 1 and $-3$. Compute their mean absolute error and mean squared error.


### 1.2-C03 · Calculation

*Source: [PDF pp. 16–18](../Lecture%20Slides/1.2.%20Shallow%20Learning.pdf#page=16).*

The unregularized loss is 5, $\|w\|_2^2=4$, and $\lambda=0.5$. Compute $J=L+\lambda\|w\|_2^2$. If $\lambda$ increases while $w$ stays fixed, does this objective rise or fall?


# 1.3. Bayesian Learning

**Slides:** [1.3. Bayesian Learning.pdf](../Lecture%20Slides/1.3.%20Bayesian%20Learning.pdf). **20 questions: 10 MC · 7 short answers · 3 easy calculations.**


## Multiple choice


### 1.3-M01 · MC

*Source: [PDF pp. 5–8](../Lecture%20Slides/1.3.%20Bayesian%20Learning.pdf#page=5).*

In Bayesian parameter learning, the posterior represents:

- A. Fixed labels for future data.
- B. Updated parameter uncertainty after observing data.
- C. The optimization step size.
- D. Only the input probability before fitting.


### 1.3-M02 · MC

*Source: [PDF pp. 7–8](../Lecture%20Slides/1.3.%20Bayesian%20Learning.pdf#page=7).*

Compared with full Bayesian inference, MAP estimation returns:

- A. The entire predictive distribution by definition.
- B. Every parameter value with equal weight.
- C. A single parameter value maximizing the posterior density.
- D. The likelihood with no prior contribution.


### 1.3-M03 · MC

*Source: [PDF pp. 9–14](../Lecture%20Slides/1.3.%20Bayesian%20Learning.pdf#page=9).*

Gaussian regression likelihoods and Gaussian weight priors are convenient because:

- A. The weight posterior can also be obtained in Gaussian form.
- B. They guarantee nonlinear decision boundaries.
- C. They eliminate uncertainty.
- D. They need no observed targets.


### 1.3-M04 · MC

*Source: [PDF pp. 13](../Lecture%20Slides/1.3.%20Bayesian%20Learning.pdf#page=13).*

A zero-mean isotropic Gaussian weight prior gives a MAP estimate associated with:

- A. A tree-depth penalty.
- B. An L2 penalty.
- C. An entropy-only objective.
- D. An L1 penalty.


### 1.3-M05 · MC

*Source: [PDF pp. 14, 19–20](../Lecture%20Slides/1.3.%20Bayesian%20Learning.pdf#page=14).*

Two predictive distributions share a mean. The one with larger variance expresses:

- A. Greater error on every sample.
- B. More observations at that input.
- C. A larger predicted mean target.
- D. Greater predictive uncertainty under the model.


### 1.3-M06 · MC

*Source: [PDF pp. 30–35](../Lecture%20Slides/1.3.%20Bayesian%20Learning.pdf#page=30).*

A Gaussian process specifies that:

- A. Function values at any finite collection of inputs have a joint Gaussian distribution.
- B. All function values are independent.
- C. Input features must be Gaussian.
- D. Every sampled function is a Gaussian bell curve.


### 1.3-M07 · MC

*Source: [PDF pp. 31–38](../Lecture%20Slides/1.3.%20Bayesian%20Learning.pdf#page=31).*

What does a GP kernel $k(x,x')$ describe?

- A. The posterior mean at both inputs.
- B. Covariance between the corresponding function values.
- C. The observation count at $x'$.
- D. The chance of selecting $x$ during SGD.


### 1.3-M08 · MC

*Source: [PDF pp. 38, 46–47](../Lecture%20Slides/1.3.%20Bayesian%20Learning.pdf#page=38).*

A larger RBF length scale generally favours:

- A. Higher noise variance by definition.
- B. More rapid variation across nearby inputs.
- C. Correlations extending over larger input distances.
- D. Periodicity with a shorter period.


### 1.3-M09 · MC

*Source: [PDF pp. 42–45](../Lecture%20Slides/1.3.%20Bayesian%20Learning.pdf#page=42).*

Which kernel component suits a repeating seasonal pattern?

- A. Only independent white noise.
- B. A linear kernel alone.
- C. A constant kernel alone.
- D. A periodic kernel.


### 1.3-M10 · MC

*Source: [PDF pp. 49–52](../Lecture%20Slides/1.3.%20Bayesian%20Learning.pdf#page=49).*

GP kernel hyperparameters can be selected by optimizing:

- A. Test error after every update.
- B. The number of target labels.
- C. The marginal likelihood of the observed data.
- D. Only the unconditioned prior mean.


## Short answers


### 1.3-S01 · Short

*Source: [PDF pp. 5–8](../Lecture%20Slides/1.3.%20Bayesian%20Learning.pdf#page=5).*

Identify the prior, likelihood, and posterior in $p(w\mid D)\propto p(D\mid w)p(w)$.


### 1.3-S02 · Short

*Source: [PDF pp. 7, 14](../Lecture%20Slides/1.3.%20Bayesian%20Learning.pdf#page=7).*

How does Bayesian prediction account for weight uncertainty instead of using just one fitted weight vector?


### 1.3-S03 · Short

*Source: [PDF pp. 14](../Lecture%20Slides/1.3.%20Bayesian%20Learning.pdf#page=14).*

Distinguish uncertainty about the latent function from observation noise. Which can often be reduced by additional informative data?


### 1.3-S04 · Short

*Source: [PDF pp. 36](../Lecture%20Slides/1.3.%20Bayesian%20Learning.pdf#page=36).*

Why is a GP called nonparametric even though its kernel has hyperparameters?


### 1.3-S05 · Short

*Source: [PDF pp. 46–48](../Lecture%20Slides/1.3.%20Bayesian%20Learning.pdf#page=46).*

With comparably scaled input dimensions, what does a very large ARD length scale for one dimension suggest about its relevance?


### 1.3-S06 · Short

*Source: [PDF pp. 44–45](../Lecture%20Slides/1.3.%20Bayesian%20Learning.pdf#page=44).*

What pattern might a sum of a linear kernel and a periodic kernel model? Give a one-sentence example.


### 1.3-S07 · Short

*Source: [PDF pp. 51–52](../Lecture%20Slides/1.3.%20Bayesian%20Learning.pdf#page=51).*

Why solve a linear system using a Cholesky factor rather than explicitly form a matrix inverse in GP regression?


## Easy calculations


### 1.3-C01 · Calculation

*Source: [PDF pp. 5–6](../Lecture%20Slides/1.3.%20Bayesian%20Learning.pdf#page=5).*

Two exhaustive hypotheses have prior probabilities 0.5 each. Data likelihoods are 0.8 under $H_1$ and 0.2 under $H_2$. Compute $P(H_1\mid D)$ by normalizing the prior-times-likelihood scores.


### 1.3-C02 · Calculation

*Source: [PDF pp. 13–14](../Lecture%20Slides/1.3.%20Bayesian%20Learning.pdf#page=13).*

For one scalar weight, prior precision is 1 and data precision is 3. Posterior variance is $1/(1+3)$ and posterior mean is $(1\cdot0+3\cdot4)/(1+3)$. Compute both posterior quantities.


### 1.3-C03 · Calculation

*Source: [PDF pp. 14](../Lecture%20Slides/1.3.%20Bayesian%20Learning.pdf#page=14).*

Latent-function predictive variance is 0.25 and independent observation-noise variance is 0.75. Compute the variance and standard deviation of the noisy prediction.


# 2.1. Introduction to Reinforcement Learning

**Slides:** [2.1. Introduction to Reinforcement Learning.pdf](../Lecture%20Slides/2.1.%20Introduction%20to%20Reinforcement%20Learning.pdf). **20 questions: 10 MC · 7 short answers · 3 easy calculations.**


## Multiple choice


### 2.1-M01 · MC

*Source: [PDF pp. 3–5](../Lecture%20Slides/2.1.%20Introduction%20to%20Reinforcement%20Learning.pdf#page=3).*

What feedback does a standard RL agent receive?

- A. The gradient of the environment's hidden equations.
- B. The complete optimal policy.
- C. A scalar reward signal.
- D. The correct action at every step.


### 2.1-M02 · MC

*Source: [PDF pp. 5](../Lecture%20Slides/2.1.%20Introduction%20to%20Reinforcement%20Learning.pdf#page=5).*

The usual RL objective is to maximize:

- A. Expected cumulative reward.
- B. Visited-state count regardless of reward.
- C. The size of the action set.
- D. Only the first action's reward.


### 2.1-M03 · MC

*Source: [PDF pp. 7](../Lecture%20Slides/2.1.%20Introduction%20to%20Reinforcement%20Learning.pdf#page=7).*

Which describes the interaction loop?

- A. The agent acts; the environment supplies a successor state and reward.
- B. The environment selects the agent's policy and ends training.
- C. The agent directly changes transition probabilities.
- D. The agent supplies a correct label and receives examples.


### 2.1-M04 · MC

*Source: [PDF pp. 8–9](../Lecture%20Slides/2.1.%20Introduction%20to%20Reinforcement%20Learning.pdf#page=8).*

In stochastic gridworld, choosing North means:

- A. The state is necessarily unobservable.
- B. The successor cell must be North.
- C. The policy is necessarily random.
- D. Actual movement is sampled from a transition distribution.


### 2.1-M05 · MC

*Source: [PDF pp. 8](../Lecture%20Slides/2.1.%20Introduction%20to%20Reinforcement%20Learning.pdf#page=8).*

What happens at a terminal state in an episodic task?

- A. The policy is retrained from scratch.
- B. Earlier rewards are erased.
- C. That episode ends.
- D. Its reward must be negative.


### 2.1-M06 · MC

*Source: [PDF pp. 11–12](../Lecture%20Slides/2.1.%20Introduction%20to%20Reinforcement%20Learning.pdf#page=11).*

A policy describes:

- A. Rewards attached to terminal states.
- B. The environment's dynamics.
- C. The agent's behaviour: which actions to take in each state.
- D. Sensor noise.


### 2.1-M07 · MC

*Source: [PDF pp. 11](../Lecture%20Slides/2.1.%20Introduction%20to%20Reinforcement%20Learning.pdf#page=11).*

A transition model predicts:

- A. The best action without a state.
- B. Only accumulated past reward.
- C. The final trained weights.
- D. Successor-state probabilities given the current state and action.


### 2.1-M08 · MC

*Source: [PDF pp. 13](../Lecture%20Slides/2.1.%20Introduction%20to%20Reinforcement%20Learning.pdf#page=13).*

A state's value under a policy concerns:

- A. The available-action count.
- B. Expected future return starting there and following that policy.
- C. Only rewards already collected.
- D. Its chance of being the initial state.


### 2.1-M09 · MC

*Source: [PDF pp. 14–16](../Lecture%20Slides/2.1.%20Introduction%20to%20Reinforcement%20Learning.pdf#page=14).*

What distinguishes planning with a known model from learning by interaction?

- A. Planning has no objective.
- B. Planning always needs human action labels.
- C. Learning needs deterministic transitions.
- D. Planning computes consequences using a model; learning obtains information from experience.


### 2.1-M10 · MC

*Source: [PDF pp. 16](../Lecture%20Slides/2.1.%20Introduction%20to%20Reinforcement%20Learning.pdf#page=16).*

Trying an unfamiliar action to learn whether it is useful is:

- A. Known-model policy evaluation.
- B. Exploitation.
- C. Reward normalization.
- D. Exploration.


## Short answers


### 2.1-S01 · Short

*Source: [PDF pp. 3](../Lecture%20Slides/2.1.%20Introduction%20to%20Reinforcement%20Learning.pdf#page=3).*

Why does an RL agent's behaviour influence the data it later learns from?


### 2.1-S02 · Short

*Source: [PDF pp. 5–6](../Lecture%20Slides/2.1.%20Introduction%20to%20Reinforcement%20Learning.pdf#page=5).*

State the relationship between maximizing reward and minimizing cost. Give one reward or cost suitable for a walking robot.


### 2.1-S03 · Short

*Source: [PDF pp. 7, 10](../Lecture%20Slides/2.1.%20Introduction%20to%20Reinforcement%20Learning.pdf#page=7).*

Distinguish the environment's true state from the agent's observation when sensing is incomplete.


### 2.1-S04 · Short

*Source: [PDF pp. 12](../Lecture%20Slides/2.1.%20Introduction%20to%20Reinforcement%20Learning.pdf#page=12).*

Distinguish deterministic and stochastic policies. Does a deterministic policy imply deterministic transitions?


### 2.1-S05 · Short

*Source: [PDF pp. 8, 12](../Lecture%20Slides/2.1.%20Introduction%20to%20Reinforcement%20Learning.pdf#page=8).*

Why can a more negative per-step living reward encourage a gridworld agent to finish sooner?


### 2.1-S06 · Short

*Source: [PDF pp. 13](../Lecture%20Slides/2.1.%20Introduction%20to%20Reinforcement%20Learning.pdf#page=13).*

What does the discount factor control? How does reducing it change the importance of delayed rewards?


### 2.1-S07 · Short

*Source: [PDF pp. 14–16](../Lecture%20Slides/2.1.%20Introduction%20to%20Reinforcement%20Learning.pdf#page=14).*

Why might always choosing the currently best-known action prevent discovery of a better policy?


## Easy calculations


### 2.1-C01 · Calculation

*Source: [PDF pp. 8](../Lecture%20Slides/2.1.%20Introduction%20to%20Reinforcement%20Learning.pdf#page=8).*

When North is selected, movement is North with probability 0.8, East with 0.1, and West with 0.1. Assume no walls. What is the probability of sideways movement and its expected count in 10 such actions?


### 2.1-C02 · Calculation

*Source: [PDF pp. 5, 8](../Lecture%20Slides/2.1.%20Introduction%20to%20Reinforcement%20Learning.pdf#page=5).*

An episode has four nonterminal moves with reward $-1$ each, followed by a terminal transition with reward $+10$. With no discounting, compute total reward.


### 2.1-C03 · Calculation

*Source: [PDF pp. 13](../Lecture%20Slides/2.1.%20Introduction%20to%20Reinforcement%20Learning.pdf#page=13).*

The next two rewards are 2 and 4, after which the episode ends. With $\gamma=0.5$, compute $G=2+\gamma\,4$.


# 2.2. Markov decision processes

**Slides:** [2.2. Markov decision processes.pdf](../Lecture%20Slides/2.2.%20Markov%20decision%20processes.pdf). **20 questions: 10 MC · 7 short answers · 3 easy calculations.**


## Multiple choice


### 2.2-M01 · MC

*Source: [PDF pp. 2–3](../Lecture%20Slides/2.2.%20Markov%20decision%20processes.pdf#page=2).*

The Markov property means that, given the current state and action:

- A. The history adds no information about the next-state distribution.
- B. The next state must be deterministic.
- C. All actions have equal value.
- D. Rewards must be positive.


### 2.2-M02 · MC

*Source: [PDF pp. 3](../Lecture%20Slides/2.2.%20Markov%20decision%20processes.pdf#page=3).*

Which tuple describes the main ingredients of the discounted MDP in the slides?

- A. Prior, likelihood, posterior, kernel, noise.
- B. Features, labels, loss, optimizer, batch size.
- C. States, actions, transitions, rewards, discount factor.
- D. Inputs, hidden layers, outputs, weights, biases.


### 2.2-M03 · MC

*Source: [PDF pp. 6](../Lecture%20Slides/2.2.%20Markov%20decision%20processes.pdf#page=6).*

A stochastic policy $\pi(a\mid s)$ gives:

- A. Only the reward of action $a$.
- B. A probability distribution over actions in state $s$.
- C. The probability of the next state.
- D. The optimal return from $s$.


### 2.2-M04 · MC

*Source: [PDF pp. 7–8](../Lecture%20Slides/2.2.%20Markov%20decision%20processes.pdf#page=7).*

If $\gamma=0$, the discounted-return objective considers:

- A. Only the next immediate reward.
- B. Only rewards before the current state.
- C. No rewards at all.
- D. All future rewards equally.


### 2.2-M05 · MC

*Source: [PDF pp. 8–10](../Lecture%20Slides/2.2.%20Markov%20decision%20processes.pdf#page=8).*

With bounded rewards, using $0\leq\gamma<1$ in an infinite-horizon problem helps ensure:

- A. A finite discounted return.
- B. Deterministic transitions.
- C. Every policy has the same value.
- D. An episode ends after exactly $1/\gamma$ steps.


### 2.2-M06 · MC

*Source: [PDF pp. 11](../Lecture%20Slides/2.2.%20Markov%20decision%20processes.pdf#page=11).*

What does $Q^\pi(s,a)$ represent?

- A. The probability that $a$ is optimal.
- B. Only the immediate reward.
- C. Expected return after taking $a$ in $s$ and then following $\pi$.
- D. The number of visits to $(s,a)$.


### 2.2-M07 · MC

*Source: [PDF pp. 12–15](../Lecture%20Slides/2.2.%20Markov%20decision%20processes.pdf#page=12).*

The Bellman expectation equation decomposes value into:

- A. Reward divided by the number of actions.
- B. Expected immediate reward plus discounted successor value.
- C. Prior probability and likelihood.
- D. Training error and validation error.


### 2.2-M08 · MC

*Source: [PDF pp. 16–19](../Lecture%20Slides/2.2.%20Markov%20decision%20processes.pdf#page=16).*

An optimal policy is greedy with respect to:

- A. The largest transition probability alone.
- B. Immediate rewards alone, for every discount factor.
- C. Any randomly initialized value estimates.
- D. The optimal action-value function.


### 2.2-M09 · MC

*Source: [PDF pp. 20–22](../Lecture%20Slides/2.2.%20Markov%20decision%20processes.pdf#page=20).*

Policy evaluation computes:

- A. The value of a given policy.
- B. The supervised classification error.
- C. Only an environment model from samples.
- D. A new policy without using the current one.


### 2.2-M10 · MC

*Source: [PDF pp. 20–24](../Lecture%20Slides/2.2.%20Markov%20decision%20processes.pdf#page=20).*

Policy iteration repeatedly alternates:

- A. Clustering and dimensionality reduction.
- B. Policy evaluation and policy improvement.
- C. Random action selection and restarting all values.
- D. Reward deletion and state deletion.


## Short answers


### 2.2-S01 · Short

*Source: [PDF pp. 2–3](../Lecture%20Slides/2.2.%20Markov%20decision%20processes.pdf#page=2).*

Why might a robot's position alone fail to be Markov if its velocity affects what happens next?


### 2.2-S02 · Short

*Source: [PDF pp. 11–15](../Lecture%20Slides/2.2.%20Markov%20decision%20processes.pdf#page=11).*

Distinguish $V^\pi(s)$ from $Q^\pi(s,a)$. How does a stochastic policy relate the two?


### 2.2-S03 · Short

*Source: [PDF pp. 16–19](../Lecture%20Slides/2.2.%20Markov%20decision%20processes.pdf#page=16).*

What changes between a Bellman expectation backup for a fixed policy and a Bellman optimality backup?


### 2.2-S04 · Short

*Source: [PDF pp. 20–24](../Lecture%20Slides/2.2.%20Markov%20decision%20processes.pdf#page=20).*

How does value iteration differ from policy iteration? State the central operation of each.


### 2.2-S05 · Short

*Source: [PDF pp. 10, 22](../Lecture%20Slides/2.2.%20Markov%20decision%20processes.pdf#page=10).*

Why is the continuation value after reaching a terminal state usually zero? Does this remove the reward on the transition into it?


### 2.2-S06 · Short

*Source: [PDF pp. 6, 10](../Lecture%20Slides/2.2.%20Markov%20decision%20processes.pdf#page=6).*

Why might an optimal action in a finite-horizon task depend on the time remaining as well as the state?


### 2.2-S07 · Short

*Source: [PDF pp. 21–24](../Lecture%20Slides/2.2.%20Markov%20decision%20processes.pdf#page=21).*

In synchronous value iteration, why should all updates in one sweep use the preceding sweep's values?


## Easy calculations


### 2.2-C01 · Calculation

*Source: [PDF pp. 7–9](../Lecture%20Slides/2.2.%20Markov%20decision%20processes.pdf#page=7).*

Option A gives reward 3 immediately. Option B gives 0 immediately and 8 one step later, then ends. With $\gamma=0.5$, compute both returns and choose the better option.


### 2.2-C02 · Calculation

*Source: [PDF pp. 13–15](../Lecture%20Slides/2.2.%20Markov%20decision%20processes.pdf#page=13).*

A policy selects action A with probability 0.25 and B with probability 0.75. Given $Q^\pi(s,A)=8$ and $Q^\pi(s,B)=4$, compute $V^\pi(s)$.


### 2.2-C03 · Calculation

*Source: [PDF pp. 18–24](../Lecture%20Slides/2.2.%20Markov%20decision%20processes.pdf#page=18).*

For one value-iteration backup, action A gives reward 1 and deterministically reaches a state with old value 6; action B terminates with reward 3. With $\gamma=0.5$, compute the new value of the current state and its greedy action.


# 2.3. Q-learning

**Slides:** [2.3. Q-learning.pdf](../Lecture%20Slides/2.3.%20Q-learning.pdf). **20 questions: 10 MC · 7 short answers · 3 easy calculations.**


## Multiple choice


### 2.3-M01 · MC

*Source: [PDF pp. 6–10](../Lecture%20Slides/2.3.%20Q-learning.pdf#page=6).*

Which description is model-free RL?

- A. Planning only from known transition probabilities.
- B. Learning values or policies from experience without requiring an explicit transition model.
- C. Learning with no parameters of any kind.
- D. Acting without observing rewards.


### 2.3-M02 · MC

*Source: [PDF pp. 11–16](../Lecture%20Slides/2.3.%20Q-learning.pdf#page=11).*

Monte Carlo policy evaluation normally uses:

- A. Exact expectations over a known model.
- B. Only the next immediate reward.
- C. Complete sampled returns from episodes.
- D. Only predicted successor values.


### 2.3-M03 · MC

*Source: [PDF pp. 19–26](../Lecture%20Slides/2.3.%20Q-learning.pdf#page=19).*

Bootstrapping in TD learning means:

- A. Resampling a supervised dataset with replacement.
- B. Initializing every value to zero.
- C. Updating an estimate using another current estimate.
- D. Waiting for all episodes to finish.


### 2.3-M04 · MC

*Source: [PDF pp. 19–24](../Lecture%20Slides/2.3.%20Q-learning.pdf#page=19).*

In $V\leftarrow V+\alpha(\text{target}-V)$, $\alpha=1$ means:

- A. Set the target to zero.
- B. Average all past targets equally.
- C. Replace the current estimate by this target.
- D. Ignore the new target.


### 2.3-M05 · MC

*Source: [PDF pp. 30–32](../Lecture%20Slides/2.3.%20Q-learning.pdf#page=30).*

Under the usual $\epsilon$-greedy rule, increasing $\epsilon$ increases:

- A. The frequency of random action selection.
- B. The number of possible states.
- C. The value-update step size.
- D. The discount factor.


### 2.3-M06 · MC

*Source: [PDF pp. 35–38](../Lecture%20Slides/2.3.%20Q-learning.pdf#page=35).*

The standard Q-learning target uses:

- A. The maximum next-state action value.
- B. The average value of all states.
- C. The actual sampled next action's value.
- D. The minimum current-state action value.


### 2.3-M07 · MC

*Source: [PDF pp. 29, 37–38](../Lecture%20Slides/2.3.%20Q-learning.pdf#page=29).*

SARSA is on-policy because its update uses:

- A. The next action sampled from the policy being followed and evaluated.
- B. The best next action regardless of behaviour.
- C. A known environment model.
- D. Only the immediate reward.


### 2.3-M08 · MC

*Source: [PDF pp. 35–38](../Lecture%20Slides/2.3.%20Q-learning.pdf#page=35).*

Q-learning is called off-policy because:

- A. It requires a separate labelled dataset.
- B. Its target can evaluate greedy behaviour while data come from an exploratory policy.
- C. It cannot collect data online.
- D. It never explores.


### 2.3-M09 · MC

*Source: [PDF pp. 39–44](../Lecture%20Slides/2.3.%20Q-learning.pdf#page=39).*

Function approximation helps with large state spaces by:

- A. Making rewards deterministic.
- B. Sharing parameters and generalizing between states.
- C. Storing a separate independent entry for every state.
- D. Removing the need for experience.


### 2.3-M10 · MC

*Source: [PDF pp. 47](../Lecture%20Slides/2.3.%20Q-learning.pdf#page=47).*

Which three ingredients form the deadly triad associated with instability?

- A. Discounting, rewards, terminal states.
- B. Function approximation, bootstrapping, off-policy learning.
- C. Exploration, deterministic policies, finite horizons.
- D. Labels, minibatches, cross-entropy.


## Short answers


### 2.3-S01 · Short

*Source: [PDF pp. 11–26](../Lecture%20Slides/2.3.%20Q-learning.pdf#page=11).*

Why can one-step TD update before an episode finishes, whereas ordinary Monte Carlo return estimation waits for the episode's outcome?


### 2.3-S02 · Short

*Source: [PDF pp. 19–24](../Lecture%20Slides/2.3.%20Q-learning.pdf#page=19).*

What is a TD error? Interpret a positive error relative to the current value estimate.


### 2.3-S03 · Short

*Source: [PDF pp. 30–32](../Lecture%20Slides/2.3.%20Q-learning.pdf#page=30).*

Why can a purely greedy learner get stuck choosing an inferior action? What problem arises if it keeps exploring almost all the time?


### 2.3-S04 · Short

*Source: [PDF pp. 29, 35–38](../Lecture%20Slides/2.3.%20Q-learning.pdf#page=29).*

At the next state, the behaviour policy chooses a low-value exploratory action. How can the SARSA and Q-learning targets differ?


### 2.3-S05 · Short

*Source: [PDF pp. 35–36](../Lecture%20Slides/2.3.%20Q-learning.pdf#page=35).*

For a truly terminal successor state, what continuation term is used in the Q-learning target, and what happens to the observed terminal reward?


### 2.3-S06 · Short

*Source: [PDF pp. 42–44](../Lecture%20Slides/2.3.%20Q-learning.pdf#page=42).*

In $Q(s,a)=\sum_i w_i f_i(s,a)$, distinguish features from learned weights. Why can one weight update affect several state–action pairs?


### 2.3-S07 · Short

*Source: [PDF pp. 31](../Lecture%20Slides/2.3.%20Q-learning.pdf#page=31).*

What does regret measure relative to a reference best strategy? Does one positive immediate reward necessarily mean zero regret?


## Easy calculations


### 2.3-C01 · Calculation

*Source: [PDF pp. 35–36](../Lecture%20Slides/2.3.%20Q-learning.pdf#page=35).*

Perform one Q-learning update with $Q(s,a)=2$, $r=1$, $\gamma=0.5$, $\alpha=0.5$, and $\max_{a'}Q(s',a')=6$. First compute the target, then $Q_{new}=Q+\alpha(\text{target}-Q)$.


### 2.3-C02 · Calculation

*Source: [PDF pp. 30–32](../Lecture%20Slides/2.3.%20Q-learning.pdf#page=30).*

An $\epsilon$-greedy policy has four actions, one uniquely greedy action, and $\epsilon=0.2$. The random branch samples uniformly from all four actions. Compute the probability of choosing the greedy action.


### 2.3-C03 · Calculation

*Source: [PDF pp. 42–44](../Lecture%20Slides/2.3.%20Q-learning.pdf#page=42).*

A linear approximation uses $Q(s,a)=2f_1(s,a)-f_2(s,a)$. If $f_1=3$ and $f_2=2$, compute $Q(s,a)$. Is this value a probability?


# 2.4. Policy Search

**Slides:** [2.4. Policy Search.pdf](../Lecture%20Slides/2.4.%20Policy%20Search.pdf). **20 questions: 10 MC · 7 short answers · 3 easy calculations.**


## Multiple choice


### 2.4-M01 · MC

*Source: [PDF pp. 2](../Lecture%20Slides/2.4.%20Policy%20Search.pdf#page=2).*

Policy-based RL directly parameterizes:

- A. Only a table of optimal Q-values.
- B. Only the transition matrix.
- C. The action-selection policy.
- D. The test-set labels.


### 2.4-M02 · MC

*Source: [PDF pp. 3](../Lecture%20Slides/2.4.%20Policy%20Search.pdf#page=3).*

One reason to use policy search is that it:

- A. Always finds a global optimum.
- B. Eliminates sampling variance.
- C. Does not require reward feedback.
- D. Naturally supports stochastic policies and continuous actions.


### 2.4-M03 · MC

*Source: [PDF pp. 6–7](../Lecture%20Slides/2.4.%20Policy%20Search.pdf#page=6).*

The policy objective $J(\theta)$ is typically:

- A. The negative transition probability.
- B. The number of policy parameters.
- C. Expected return under the parameterized policy.
- D. A supervised class-accuracy score by definition.


### 2.4-M04 · MC

*Source: [PDF pp. 7](../Lecture%20Slides/2.4.%20Policy%20Search.pdf#page=7).*

To maximize $J(\theta)$ using its gradient, the update direction is:

- A. Independent of $J$.
- B. $-\nabla_\theta J$.
- C. Always towards zero parameters.
- D. $+\nabla_\theta J$.


### 2.4-M05 · MC

*Source: [PDF pp. 11](../Lecture%20Slides/2.4.%20Policy%20Search.pdf#page=11).*

A softmax policy converts action scores into:

- A. Rewards guaranteed to be positive.
- B. State-transition probabilities.
- C. Nonnegative action probabilities that sum to 1.
- D. A single continuous action without a distribution.


### 2.4-M06 · MC

*Source: [PDF pp. 9–14](../Lecture%20Slides/2.4.%20Policy%20Search.pdf#page=9).*

In REINFORCE, sampled returns primarily:

- A. Guarantee the best trajectory is repeated exactly.
- B. Weight gradients of log action probabilities.
- C. Replace the environment model with correct labels.
- D. Remove the need to sample actions.


### 2.4-M07 · MC

*Source: [PDF pp. 9, 14–15](../Lecture%20Slides/2.4.%20Policy%20Search.pdf#page=9).*

REINFORCE estimates the expected policy gradient using:

- A. Monte Carlo samples of trajectories or returns.
- B. A supervised test-set confusion matrix.
- C. Only the initial state distribution.
- D. Exact enumeration of every possible trajectory.


### 2.4-M08 · MC

*Source: [PDF pp. 17](../Lecture%20Slides/2.4.%20Policy%20Search.pdf#page=17).*

In actor–critic, the critic learns:

- A. Only a transition model.
- B. A value estimate that helps guide policy updates.
- C. The input-feature normalization.
- D. A replacement for the action space.


### 2.4-M09 · MC

*Source: [PDF pp. 17](../Lecture%20Slides/2.4.%20Policy%20Search.pdf#page=17).*

Compared with plain Monte Carlo policy gradients, a learned critic can:

- A. Make the reward function unnecessary.
- B. Remove every source of bias and variance.
- C. Guarantee a globally optimal policy.
- D. Reduce variance while introducing approximation or bootstrapping bias.


### 2.4-M10 · MC

*Source: [PDF pp. 18–19](../Lecture%20Slides/2.4.%20Policy%20Search.pdf#page=18).*

Which policy-search approach can be used without policy derivatives?

- A. Exact differentiation of $J$.
- B. An evolutionary optimization method.
- C. Backpropagated policy gradient.
- D. Gradient ascent through the policy network.


## Short answers


### 2.4-S01 · Short

*Source: [PDF pp. 2–3](../Lecture%20Slides/2.4.%20Policy%20Search.pdf#page=2).*

Contrast obtaining a policy from Q-values with directly learning a parameterized policy.


### 2.4-S02 · Short

*Source: [PDF pp. 5](../Lecture%20Slides/2.4.%20Policy%20Search.pdf#page=5).*

What factors determine the probability of a sampled trajectory? Name the roles of the initial state, policy, and environment transitions.


### 2.4-S03 · Short

*Source: [PDF pp. 8–10](../Lecture%20Slides/2.4.%20Policy%20Search.pdf#page=8).*

Why can sampling trajectories avoid the need to enumerate all possible futures when estimating a policy gradient?


### 2.4-S04 · Short

*Source: [PDF pp. 12–14](../Lecture%20Slides/2.4.%20Policy%20Search.pdf#page=12).*

Why does the REINFORCE loss weight log action probabilities by returns instead of simply imitating all sampled actions equally?


### 2.4-S05 · Short

*Source: [PDF pp. 14–15](../Lecture%20Slides/2.4.%20Policy%20Search.pdf#page=14).*

Why can an estimate based on only one episode be noisy even when the gradient calculation for that episode is exact?


### 2.4-S06 · Short

*Source: [PDF pp. 17](../Lecture%20Slides/2.4.%20Policy%20Search.pdf#page=17).*

State the actor's and critic's roles in one sentence each. Which one directly determines action probabilities?


### 2.4-S07 · Short

*Source: [PDF pp. 3, 7, 18](../Lecture%20Slides/2.4.%20Policy%20Search.pdf#page=3).*

Does policy-gradient ascent guarantee the globally best policy? Give one reason why optimizing a parameterized policy can be difficult.


## Easy calculations


### 2.4-C01 · Calculation

*Source: [PDF pp. 7](../Lecture%20Slides/2.4.%20Policy%20Search.pdf#page=7).*

A scalar policy parameter is $\theta=1$, the estimated return gradient is 2, and the ascent step size is 0.1. Compute the updated parameter.


### 2.4-C02 · Calculation

*Source: [PDF pp. 11](../Lecture%20Slides/2.4.%20Policy%20Search.pdf#page=11).*

Two action scores have exponentials 1 and 3. Compute their softmax probabilities without evaluating any exponentials yourself.


### 2.4-C03 · Calculation

*Source: [PDF pp. 6, 9](../Lecture%20Slides/2.4.%20Policy%20Search.pdf#page=6).*

Three sampled episodes under the same policy have undiscounted returns 2, 4, and 6. Compute the Monte Carlo estimate of expected return. Does this sample average prove the policy is optimal?


# 3.1. Introduction to Deep Learning

**Slides:** [3.1. Introduction to Deep Learning.pdf](../Lecture%20Slides/3.1.%20Introduction%20to%20Deep%20Learning.pdf). **20 questions: 10 MC · 7 short answers · 3 easy calculations.**


## Multiple choice


### 3.1-M01 · MC

*Source: [PDF pp. 6–10](../Lecture%20Slides/3.1.%20Introduction%20to%20Deep%20Learning.pdf#page=6).*

Deep learning is best described as:

- A. A guarantee of human-like understanding.
- B. A family of machine-learning methods using multiple learned representation layers.
- C. Every program with many lines of code.
- D. Any method using a large dataset.


### 3.1-M02 · MC

*Source: [PDF pp. 6–10](../Lecture%20Slides/3.1.%20Introduction%20to%20Deep%20Learning.pdf#page=6).*

Which relationship is correct?

- A. AI is a subset of deep learning.
- B. Deep learning is part of machine learning, which is part of AI.
- C. Machine learning and AI are disjoint.
- D. Every AI system is a neural network.


### 3.1-M03 · MC

*Source: [PDF pp. 9–10, 38–39](../Lecture%20Slides/3.1.%20Introduction%20to%20Deep%20Learning.pdf#page=9).*

Representation learning means:

- A. Learning useful intermediate features from data.
- B. Choosing a plotting colour for every class.
- C. Manually writing all useful features.
- D. Storing only class labels.


### 3.1-M04 · MC

*Source: [PDF pp. 38–39](../Lecture%20Slides/3.1.%20Introduction%20to%20Deep%20Learning.pdf#page=38).*

What changes in an end-to-end deep classifier compared with a fixed handcrafted-feature pipeline?

- A. Feature extraction can be optimized jointly with the prediction stage.
- B. It no longer needs a prediction objective.
- C. Evaluation becomes unnecessary.
- D. It no longer needs training data.


### 3.1-M05 · MC

*Source: [PDF pp. 13–25](../Lecture%20Slides/3.1.%20Introduction%20to%20Deep%20Learning.pdf#page=13).*

Which statement about deep-learning applications matches the slides?

- A. They are limited to image classification.
- B. They require only categorical outputs.
- C. They include language, vision, control, and scientific tasks.
- D. They exclude sequential data.


### 3.1-M06 · MC

*Source: [PDF pp. 15–16](../Lecture%20Slides/3.1.%20Introduction%20to%20Deep%20Learning.pdf#page=15).*

Face detection and face recognition differ because:

- A. They always have identical outputs.
- B. Detection locates faces; recognition concerns identity.
- C. Recognition cannot use learned representations.
- D. Detection identifies a person; recognition finds image coordinates only.


### 3.1-M07 · MC

*Source: [PDF pp. 26–34](../Lecture%20Slides/3.1.%20Introduction%20to%20Deep%20Learning.pdf#page=26).*

Which is the most useful first check for a large training dataset?

- A. Whether its examples, labels, and variability suit the intended task.
- B. Whether every image has the same filename length.
- C. Whether the network can memorize its row order.
- D. Whether the file is larger than all previous datasets.


### 3.1-M08 · MC

*Source: [PDF pp. 31–37](../Lecture%20Slides/3.1.%20Introduction%20to%20Deep%20Learning.pdf#page=31).*

Which evaluation practice remains necessary in deep learning?

- A. Select everything on test performance.
- B. Separate fitting, model selection, and final evaluation.
- C. Assume depth guarantees generalization.
- D. Evaluate only on training examples.


### 3.1-M09 · MC

*Source: [PDF pp. 34–35](../Lecture%20Slides/3.1.%20Introduction%20to%20Deep%20Learning.pdf#page=34).*

Training an object detector normally needs which richer annotation than image classification?

- A. Only image resolution.
- B. Only the camera's manufacturer.
- C. Only one label for the entire image.
- D. Object locations as well as categories.


### 3.1-M10 · MC

*Source: [PDF pp. 16](../Lecture%20Slides/3.1.%20Introduction%20to%20Deep%20Learning.pdf#page=16).*

For face-identity embeddings, a useful training objective encourages:

- A. Same-identity examples to be maximally distant.
- B. Embeddings to depend only on file size.
- C. All people to share one embedding.
- D. Same-identity examples to be close and different identities separated.


## Short answers


### 3.1-S01 · Short

*Source: [PDF pp. 6–10](../Lecture%20Slides/3.1.%20Introduction%20to%20Deep%20Learning.pdf#page=6).*

Give one AI approach that need not learn from data. Explain why this shows that AI and machine learning are not synonyms.


### 3.1-S02 · Short

*Source: [PDF pp. 9–10, 38–39](../Lecture%20Slides/3.1.%20Introduction%20to%20Deep%20Learning.pdf#page=9).*

What is meant by a hierarchy of learned representations? Use a simple image example.


### 3.1-S03 · Short

*Source: [PDF pp. 30–39](../Lecture%20Slides/3.1.%20Introduction%20to%20Deep%20Learning.pdf#page=30).*

Contrast a handcrafted feature with a learned feature. Which part of the pipeline is learned in each case?


### 3.1-S04 · Short

*Source: [PDF pp. 27–34](../Lecture%20Slides/3.1.%20Introduction%20to%20Deep%20Learning.pdf#page=27).*

Why can adding more images from one narrow setting fail to solve poor generalization to another setting?


### 3.1-S05 · Short

*Source: [PDF pp. 34–35](../Lecture%20Slides/3.1.%20Introduction%20to%20Deep%20Learning.pdf#page=34).*

How do the required labels differ between image classification and pixel-level segmentation?


### 3.1-S06 · Short

*Source: [PDF pp. 31–37](../Lecture%20Slides/3.1.%20Introduction%20to%20Deep%20Learning.pdf#page=31).*

A deep model performs very well on training images but poorly on new images. Give two plausible data or methodology issues to investigate.


### 3.1-S07 · Short

*Source: [PDF pp. 16, 38–39](../Lecture%20Slides/3.1.%20Introduction%20to%20Deep%20Learning.pdf#page=16).*

Why might a useful embedding support more than one downstream task, rather than only the task used to learn it?


## Easy calculations


### 3.1-C01 · Calculation

*Source: [PDF pp. 30–32, 38–39](../Lecture%20Slides/3.1.%20Introduction%20to%20Deep%20Learning.pdf#page=30).*

Represent a $16\times16$ RGB image by flattening all three colour channels. How many scalar input values does the resulting vector contain?


### 3.1-C02 · Calculation

*Source: [PDF pp. 31–32](../Lecture%20Slides/3.1.%20Introduction%20to%20Deep%20Learning.pdf#page=31).*

For a toy dataset of 2,000 images, allocate 80% to training and 10% to validation. How many remain for testing?


### 3.1-C03 · Calculation

*Source: [PDF pp. 34–35](../Lecture%20Slides/3.1.%20Introduction%20to%20Deep%20Learning.pdf#page=34).*

You have 100 images of size $8\times8$. Compare the number of target class labels needed for image classification (one per image) with semantic segmentation (one per pixel).


# 3.2. Shallow NN

**Slides:** [3.2. Shallow NN.pdf](../Lecture%20Slides/3.2.%20Shallow%20NN.pdf). **20 questions: 10 MC · 7 short answers · 3 easy calculations.**


## Multiple choice


### 3.2-M01 · MC

*Source: [PDF pp. 5–9, 49–50](../Lecture%20Slides/3.2.%20Shallow%20NN.pdf#page=5).*

In an affine unit $z=wx+b$, the bias $b$:

- A. Must equal zero after training.
- B. Shifts the preactivation independently of the input value.
- C. Is the same thing as the loss gradient.
- D. Determines the number of input samples.


### 3.2-M02 · MC

*Source: [PDF pp. 7–8, 51](../Lecture%20Slides/3.2.%20Shallow%20NN.pdf#page=7).*

The ReLU activation is:

- A. A probability distribution over classes.
- B. $z^2$.
- C. $\min(0,z)$.
- D. $\max(0,z)$.


### 3.2-M03 · MC

*Source: [PDF pp. 11–18](../Lecture%20Slides/3.2.%20Shallow%20NN.pdf#page=11).*

A 1D shallow ReLU network with an affine output represents:

- A. Only discontinuous step functions.
- B. A continuous piecewise-linear function.
- C. Only periodic functions.
- D. Only one straight line.


### 3.2-M04 · MC

*Source: [PDF pp. 12–18](../Lecture%20Slides/3.2.%20Shallow%20NN.pdf#page=12).*

An activation pattern identifies:

- A. The training-example order.
- B. Which hidden ReLU units are active for an input.
- C. The optimizer's learning rate.
- D. The sample's class label.


### 3.2-M05 · MC

*Source: [PDF pp. 23–24](../Lecture%20Slides/3.2.%20Shallow%20NN.pdf#page=23).*

The universal approximation theorem establishes, under its usual assumptions:

- A. SGD always finds the best approximation.
- B. Perfect generalization from a finite dataset.
- C. Sufficiently wide shallow networks can approximate continuous functions on compact domains arbitrarily well.
- D. One hidden unit is enough for every function.


### 3.2-M06 · MC

*Source: [PDF pp. 24](../Lecture%20Slides/3.2.%20Shallow%20NN.pdf#page=24).*

What does universal approximation alone NOT guarantee?

- A. That approximation accuracy can depend on width.
- B. That training will discover suitable parameters efficiently.
- C. That hidden units may be needed.
- D. The existence of useful nonlinear approximations.


### 3.2-M07 · MC

*Source: [PDF pp. 26–28](../Lecture%20Slides/3.2.%20Shallow%20NN.pdf#page=26).*

In a shallow network with two outputs and one shared hidden layer:

- A. The hidden units cannot be shared.
- B. The two outputs require identical output biases.
- C. Each output must equal the other.
- D. Each output can use a different weighted combination of the same hidden activations.


### 3.2-M08 · MC

*Source: [PDF pp. 30–42](../Lecture%20Slides/3.2.%20Shallow%20NN.pdf#page=30).*

For column-vector inputs $x\in\mathbb{R}^{d}$ and $h$ hidden units, $Wx+b$ uses a weight matrix of shape:

- A. $h\times h$.
- B. $d\times h$ when used directly as $Wx$.
- C. $d\times d$.
- D. $h\times d$.


### 3.2-M09 · MC

*Source: [PDF pp. 39–42](../Lecture%20Slides/3.2.%20Shallow%20NN.pdf#page=39).*

For a fully connected layer with one bias per output, the parameter count depends on:

- A. The random seed alone.
- B. The number of evaluation examples.
- C. Only the number of training batches.
- D. Input width and output width.


### 3.2-M10 · MC

*Source: [PDF pp. 18, 30–46](../Lecture%20Slides/3.2.%20Shallow%20NN.pdf#page=18).*

The linear regions of a ReLU network partition:

- A. Input space according to hidden activation patterns.
- B. The training epochs into equal intervals.
- C. The set of optimizer names.
- D. Only the parameter file on disk.


## Short answers


### 3.2-S01 · Short

*Source: [PDF pp. 5–9, 12–16](../Lecture%20Slides/3.2.%20Shallow%20NN.pdf#page=5).*

Describe the forward pass of a one-hidden-layer network in three steps, from inputs to output.


### 3.2-S02 · Short

*Source: [PDF pp. 7–18](../Lecture%20Slides/3.2.%20Shallow%20NN.pdf#page=7).*

Why are nonlinear activations needed if we want more than an affine input–output mapping?


### 3.2-S03 · Short

*Source: [PDF pp. 12–18](../Lecture%20Slides/3.2.%20Shallow%20NN.pdf#page=12).*

What happens to a ReLU hidden unit's contribution when its preactivation becomes negative?


### 3.2-S04 · Short

*Source: [PDF pp. 23–24](../Lecture%20Slides/3.2.%20Shallow%20NN.pdf#page=23).*

Distinguish a network's ability to represent a function from its ability to learn that function from limited data.


### 3.2-S05 · Short

*Source: [PDF pp. 26–28, 37](../Lecture%20Slides/3.2.%20Shallow%20NN.pdf#page=26).*

If a second output is added while the hidden layer stays fixed, which parameters must be added? Do the existing input-to-hidden weights need to be duplicated?


### 3.2-S06 · Short

*Source: [PDF pp. 39–42, 49–50](../Lecture%20Slides/3.2.%20Shallow%20NN.pdf#page=39).*

Distinguish input dimension, hidden-layer width, and output dimension. Give a situation where output dimension exceeds one.


### 3.2-S07 · Short

*Source: [PDF pp. 18, 44–46](../Lecture%20Slides/3.2.%20Shallow%20NN.pdf#page=18).*

Why can a ReLU network be linear within each activation region but nonlinear over the full input space?


## Easy calculations


### 3.2-C01 · Calculation

*Source: [PDF pp. 39–42](../Lecture%20Slides/3.2.%20Shallow%20NN.pdf#page=39).*

A fully connected shallow network has 2 inputs, 3 hidden units, and 1 output. Include one bias for every hidden and output unit. Compute the total number of trainable parameters.


### 3.2-C02 · Calculation

*Source: [PDF pp. 7–16](../Lecture%20Slides/3.2.%20Shallow%20NN.pdf#page=7).*

A hidden unit computes $h=\max(0,2x-3)$. Evaluate $h$ at $x=1$ and at $x=2$.


### 3.2-C03 · Calculation

*Source: [PDF pp. 17, 22, 44–47](../Lecture%20Slides/3.2.%20Shallow%20NN.pdf#page=17).*

A 1D shallow network has three ReLU hidden units with three distinct breakpoints. Assume their slope changes survive in the output. How many linear intervals can these breakpoints create?


# 3.3. Deep Learning Fundamentals

**Slides:** [3.3. Deep Learning Fundamentals.pdf](../Lecture%20Slides/3.3.%20Deep%20Learning%20Fundamentals.pdf). **20 questions: 10 MC · 7 short answers · 3 easy calculations.**


## Multiple choice


### 3.3-M01 · MC

*Source: [PDF pp. 5–8](../Lecture%20Slides/3.3.%20Deep%20Learning%20Fundamentals.pdf#page=5).*

Network depth and width refer respectively to:

- A. Image height and image width in every model.
- B. Learning rate and batch size.
- C. Training-set size and test-set size.
- D. Number of successive layers and number of units in a layer.


### 3.3-M02 · MC

*Source: [PDF pp. 5–14](../Lecture%20Slides/3.3.%20Deep%20Learning%20Fundamentals.pdf#page=5).*

Why can depth help represent some functions efficiently?

- A. It composes intermediate transformations instead of representing everything in one wide layer.
- B. It guarantees lower test error with every layer.
- C. It makes parameter learning unnecessary.
- D. It removes nonlinearities.


### 3.3-M03 · MC

*Source: [PDF pp. 3–10](../Lecture%20Slides/3.3.%20Deep%20Learning%20Fundamentals.pdf#page=3).*

Composing affine layers without nonlinear activations gives:

- A. A kernel classifier.
- B. An arbitrary nonlinear function.
- C. Another affine mapping.
- D. A piecewise-constant function.


### 3.3-M04 · MC

*Source: [PDF pp. 17–24](../Lecture%20Slides/3.3.%20Deep%20Learning%20Fundamentals.pdf#page=17).*

A raw class score or logit:

- A. Must lie in $[0,1]$.
- B. Is already a calibrated probability.
- C. Must sum to 1 across classes.
- D. Can be any real value before probability normalization.


### 3.3-M05 · MC

*Source: [PDF pp. 24–26](../Lecture%20Slides/3.3.%20Deep%20Learning%20Fundamentals.pdf#page=24).*

Softmax transforms logits into:

- A. Independent unbounded scores.
- B. Nonnegative probabilities summing to 1.
- C. One-hot vectors in every forward pass.
- D. Parameter gradients.


### 3.3-M06 · MC

*Source: [PDF pp. 24–26](../Lecture%20Slides/3.3.%20Deep%20Learning%20Fundamentals.pdf#page=24).*

For one-hot targets, cross-entropy $-\log p_{true}$ is smaller when:

- A. The parameter count is larger, regardless of predictions.
- B. The true class receives a larger probability.
- C. The true class probability is ignored.
- D. The true class receives a smaller probability.


### 3.3-M07 · MC

*Source: [PDF pp. 23, 25–26](../Lecture%20Slides/3.3.%20Deep%20Learning%20Fundamentals.pdf#page=23).*

Multiclass hinge loss encourages the correct-class score to:

- A. Exceed incorrect-class scores by a specified margin.
- B. Equal zero for every example.
- C. Be the smallest score.
- D. Match every incorrect-class score.


### 3.3-M08 · MC

*Source: [PDF pp. 29–35](../Lecture%20Slides/3.3.%20Deep%20Learning%20Fundamentals.pdf#page=29).*

Mini-batch SGD estimates a gradient using:

- A. Every possible input in the world.
- B. A subset of training examples at each update.
- C. Only the model's architecture.
- D. Only validation labels.


### 3.3-M09 · MC

*Source: [PDF pp. 38–39](../Lecture%20Slides/3.3.%20Deep%20Learning%20Fundamentals.pdf#page=38).*

Momentum uses:

- A. A separate label for every parameter.
- B. A running combination of recent gradients or updates.
- C. Only the current test accuracy.
- D. A fixed random direction forever.


### 3.3-M10 · MC

*Source: [PDF pp. 40–42](../Lecture%20Slides/3.3.%20Deep%20Learning%20Fundamentals.pdf#page=40).*

Adam combines momentum-like information with:

- A. Exact Hessian inversion at every step.
- B. A rule that all parameters share identical gradients.
- C. Per-parameter scaling based on squared-gradient statistics.
- D. Removal of the learning rate.


## Short answers


### 3.3-S01 · Short

*Source: [PDF pp. 8–14](../Lecture%20Slides/3.3.%20Deep%20Learning%20Fundamentals.pdf#page=8).*

Why does universal approximation by shallow networks not make deeper architectures useless?


### 3.3-S02 · Short

*Source: [PDF pp. 17–27](../Lecture%20Slides/3.3.%20Deep%20Learning%20Fundamentals.pdf#page=17).*

Distinguish a score function, a loss function, and an optimizer in one phrase each.


### 3.3-S03 · Short

*Source: [PDF pp. 23–26](../Lecture%20Slides/3.3.%20Deep%20Learning%20Fundamentals.pdf#page=23).*

Why can two predictions have the same correct top-1 class but different cross-entropy losses?


### 3.3-S04 · Short

*Source: [PDF pp. 27–28](../Lecture%20Slides/3.3.%20Deep%20Learning%20Fundamentals.pdf#page=27).*

Why should the output activation and loss match the task? Suggest a suitable loss for continuous-target regression.


### 3.3-S05 · Short

*Source: [PDF pp. 32–37](../Lecture%20Slides/3.3.%20Deep%20Learning%20Fundamentals.pdf#page=32).*

What can happen if the learning rate is too high? What if it is extremely low?


### 3.3-S06 · Short

*Source: [PDF pp. 32–35](../Lecture%20Slides/3.3.%20Deep%20Learning%20Fundamentals.pdf#page=32).*

Distinguish an epoch from a mini-batch update. Why can their counts differ substantially?


### 3.3-S07 · Short

*Source: [PDF pp. 38–44](../Lecture%20Slides/3.3.%20Deep%20Learning%20Fundamentals.pdf#page=38).*

How can momentum reduce oscillation during optimization? Does using Adam remove the need to tune hyperparameters?


## Easy calculations


### 3.3-C01 · Calculation

*Source: [PDF pp. 8–10](../Lecture%20Slides/3.3.%20Deep%20Learning%20Fundamentals.pdf#page=8).*

A fully connected network has 3 inputs, one hidden layer of 4 units, and 2 outputs. Include one bias per hidden/output unit. Count all trainable parameters.


### 3.3-C02 · Calculation

*Source: [PDF pp. 24–26](../Lecture%20Slides/3.3.%20Deep%20Learning%20Fundamentals.pdf#page=24).*

Three logits have exponentials $(1,2,1)$; class 2 is correct. Compute its softmax probability and the cross-entropy. Use $\ln2=0.693$.


### 3.3-C03 · Calculation

*Source: [PDF pp. 23, 25](../Lecture%20Slides/3.3.%20Deep%20Learning%20Fundamentals.pdf#page=23).*

For one example, the correct-class score is 2 and the two incorrect scores are 1 and 4. With margin 1, compute $L=\sum_{j\ne y}\max(0,s_j-s_y+1)$.


# 3.4. Deep Learning Fundamentals II

**Slides:** [3.4. Deep Learning Fundamentals II.pdf](../Lecture%20Slides/3.4.%20Deep%20Learning%20Fundamentals%20II.pdf). **20 questions: 10 MC · 7 short answers · 3 easy calculations.**


## Multiple choice


### 3.4-M01 · MC

*Source: [PDF pp. 7–21](../Lecture%20Slides/3.4.%20Deep%20Learning%20Fundamentals%20II.pdf#page=7).*

Backpropagation computes:

- A. Test labels from training labels.
- B. The optimal architecture without training.
- C. Loss gradients with respect to parameters using the chain rule.
- D. Parameter updates without an optimizer.


### 3.4-M02 · MC

*Source: [PDF pp. 7, 19–21](../Lecture%20Slides/3.4.%20Deep%20Learning%20Fundamentals%20II.pdf#page=7).*

Why store intermediate activations during the forward pass?

- A. They can be needed to compute local derivatives during the backward pass.
- B. They become new permanent parameters.
- C. They guarantee zero training error.
- D. They replace all training labels.


### 3.4-M03 · MC

*Source: [PDF pp. 10–16](../Lecture%20Slides/3.4.%20Deep%20Learning%20Fundamentals%20II.pdf#page=10).*

If a parameter influences loss through two computational paths, its gradient receives:

- A. Only the larger contribution.
- B. Only the first path's contribution.
- C. The sum of contributions from both paths.
- D. Their average regardless of the computation.


### 3.4-M04 · MC

*Source: [PDF pp. 23–25](../Lecture%20Slides/3.4.%20Deep%20Learning%20Fundamentals%20II.pdf#page=23).*

Why avoid identical zero initialization of hidden units in one layer?

- A. Zero is an invalid parameter value.
- B. Biases must always be positive.
- C. Units can remain symmetric and learn the same features.
- D. The forward pass becomes undefined.


### 3.4-M05 · MC

*Source: [PDF pp. 24–25](../Lecture%20Slides/3.4.%20Deep%20Learning%20Fundamentals%20II.pdf#page=24).*

Initialization schemes such as He initialization are intended partly to:

- A. Make all neurons identical.
- B. Control activation and gradient scales across layers.
- C. Fit test labels before training.
- D. Eliminate the need for nonlinearities.


### 3.4-M06 · MC

*Source: [PDF pp. 27–29](../Lecture%20Slides/3.4.%20Deep%20Learning%20Fundamentals%20II.pdf#page=27).*

An explicit L2 regularizer directly encourages:

- A. Higher output entropy in every case.
- B. Larger training batches.
- C. Smaller weight magnitudes.
- D. More hidden layers.


### 3.4-M07 · MC

*Source: [PDF pp. 31](../Lecture%20Slides/3.4.%20Deep%20Learning%20Fundamentals%20II.pdf#page=31).*

Early stopping normally selects a checkpoint using:

- A. The smallest training loss regardless of validation.
- B. Repeated test-set optimization.
- C. Held-out validation performance.
- D. Only the wall-clock time of an epoch.


### 3.4-M08 · MC

*Source: [PDF pp. 32, 34](../Lecture%20Slides/3.4.%20Deep%20Learning%20Fundamentals%20II.pdf#page=32).*

Standard dropout during training:

- A. Drops only incorrect training examples.
- B. Is normally applied unchanged during ordinary inference.
- C. Randomly suppresses some activations and uses an appropriate scaling convention.
- D. Permanently deletes a fixed subset of units.


### 3.4-M09 · MC

*Source: [PDF pp. 33–34](../Lecture%20Slides/3.4.%20Deep%20Learning%20Fundamentals%20II.pdf#page=33).*

A suitable supervised data augmentation should usually:

- A. Make every training example identical.
- B. Preserve the intended target meaning while varying the input.
- C. Change the true class arbitrarily.
- D. Use test labels to select transformations.


### 3.4-M10 · MC

*Source: [PDF pp. 37–38](../Lecture%20Slides/3.4.%20Deep%20Learning%20Fundamentals%20II.pdf#page=37).*

Double descent describes a possible pattern where test error:

- A. Is independent of model capacity.
- B. Always decreases monotonically with model capacity.
- C. Rises near an interpolation threshold and then falls again with further capacity.
- D. Equals training error throughout training.


## Short answers


### 3.4-S01 · Short

*Source: [PDF pp. 7–22](../Lecture%20Slides/3.4.%20Deep%20Learning%20Fundamentals%20II.pdf#page=7).*

Distinguish the forward pass, backward pass, and optimizer step. Which computes predictions and which changes weights?


### 3.4-S02 · Short

*Source: [PDF pp. 10–16](../Lecture%20Slides/3.4.%20Deep%20Learning%20Fundamentals%20II.pdf#page=10).*

Why does the chain rule make deep-network gradients tractable without expanding the entire network into one enormous formula?


### 3.4-S03 · Short

*Source: [PDF pp. 24–25](../Lecture%20Slides/3.4.%20Deep%20Learning%20Fundamentals%20II.pdf#page=24).*

What do vanishing and exploding gradients mean for learning in early layers?


### 3.4-S04 · Short

*Source: [PDF pp. 26–31](../Lecture%20Slides/3.4.%20Deep%20Learning%20Fundamentals%20II.pdf#page=26).*

Distinguish explicit regularization from an implicit regularizing effect of the training procedure. Give one example of each.


### 3.4-S05 · Short

*Source: [PDF pp. 32–34](../Lecture%20Slides/3.4.%20Deep%20Learning%20Fundamentals%20II.pdf#page=32).*

Why is dropout normally disabled during ordinary inference? What would happen to repeatability if random dropout masks remained active?


### 3.4-S06 · Short

*Source: [PDF pp. 33–34](../Lecture%20Slides/3.4.%20Deep%20Learning%20Fundamentals%20II.pdf#page=33).*

Give one label-preserving augmentation for an object-recognition task and one transformation that might change the label in a digit-recognition task.


### 3.4-S07 · Short

*Source: [PDF pp. 26, 31, 35–36](../Lecture%20Slides/3.4.%20Deep%20Learning%20Fundamentals%20II.pdf#page=26).*

Training loss decreases while validation loss rises. What does this suggest, and how would early stopping use these curves?


## Easy calculations


### 3.4-C01 · Calculation

*Source: [PDF pp. 10–16](../Lecture%20Slides/3.4.%20Deep%20Learning%20Fundamentals%20II.pdf#page=10).*

At a point in a graph, $\partial L/\partial h=3$ and $\partial h/\partial w=2$. There is no other path from $w$ to $L$. Compute $\partial L/\partial w$.


### 3.4-C02 · Calculation

*Source: [PDF pp. 16, 20–21](../Lecture%20Slides/3.4.%20Deep%20Learning%20Fundamentals%20II.pdf#page=16).*

A weight is $w=2$, its gradient is 3, and the learning rate is 0.1. Compute one gradient-descent update.


### 3.4-C03 · Calculation

*Source: [PDF pp. 27–29](../Lecture%20Slides/3.4.%20Deep%20Learning%20Fundamentals%20II.pdf#page=27).*

For $J=L+\lambda w^2$, the data-loss gradient is $\partial L/\partial w=3$, $w=2$, and $\lambda=0.1$. Using $\partial J/\partial w=\partial L/\partial w+2\lambda w$, compute the total gradient.


# 4.1. CNNs

**Slides:** [4.1. CNNs.pdf](../Lecture%20Slides/4.1.%20CNNs.pdf). **20 questions: 10 MC · 7 short answers · 3 easy calculations.**


## Multiple choice


### 4.1-M01 · MC

*Source: [PDF pp. 10–11](../Lecture%20Slides/4.1.%20CNNs.pdf#page=10).*

Which properties reduce a convolutional layer's parameter count relative to dense image connections?

- A. A separate filter for every pixel.
- B. Local connectivity and spatial weight sharing.
- C. Global connectivity without sharing.
- D. More image pixels and more class labels.


### 4.1-M02 · MC

*Source: [PDF pp. 19, 29–30](../Lecture%20Slides/4.1.%20CNNs.pdf#page=19).*

In a standard convolution, the output-channel count equals:

- A. The number of filters.
- B. The number of spatial output locations.
- C. The stride times the input width.
- D. The kernel width.


### 4.1-M03 · MC

*Source: [PDF pp. 15–17](../Lecture%20Slides/4.1.%20CNNs.pdf#page=15).*

Increasing convolution stride, with other settings fixed, generally:

- A. Increases spatial output resolution.
- B. Reduces spatial output resolution.
- C. Adds learned filter weights.
- D. Makes padding unnecessary for every input.


### 4.1-M04 · MC

*Source: [PDF pp. 15–16, 20–23](../Lecture%20Slides/4.1.%20CNNs.pdf#page=15).*

Increasing dilation while keeping the kernel's coefficient count fixed:

- A. Spreads sampled positions over a wider spatial region.
- B. Makes all coefficients identical.
- C. Changes only the output-channel count.
- D. Adds a new coefficient at every skipped location.


### 4.1-M05 · MC

*Source: [PDF pp. 32–35](../Lecture%20Slides/4.1.%20CNNs.pdf#page=32).*

An ordinary max-pooling layer:

- A. Always increases image resolution.
- B. Selects local maxima and has no learned filter weights.
- C. Learns a separate weight for every input pixel.
- D. Computes softmax class probabilities.


### 4.1-M06 · MC

*Source: [PDF pp. 36](../Lecture%20Slides/4.1.%20CNNs.pdf#page=36).*

A stride-1 $1\times1$ convolution primarily:

- A. Expands the spatial receptive field to $3\times3$.
- B. Mixes channels at each location and can change channel count.
- C. Removes all channel information.
- D. Pools neighbouring pixels.


### 4.1-M07 · MC

*Source: [PDF pp. 52–54](../Lecture%20Slides/4.1.%20CNNs.pdf#page=52).*

In $y=x+F(x)$, setting $F(x)=0$ gives:

- A. Twice the input.
- B. The identity mapping.
- C. Zero output.
- D. Half the input channels.


### 4.1-M08 · MC

*Source: [PDF pp. 55–59](../Lecture%20Slides/4.1.%20CNNs.pdf#page=55).*

Standard batch normalization with running statistics normally uses:

- A. The current evaluation batch for every deployment prediction.
- B. No learned scale or shift.
- C. Test-set statistics to fit its training parameters.
- D. Batch statistics during training and stored statistics during evaluation.


### 4.1-M09 · MC

*Source: [PDF pp. 67–73](../Lecture%20Slides/4.1.%20CNNs.pdf#page=67).*

For a small dataset similar to pretraining data, a sensible transfer-learning starting point is:

- A. Keep the old labels even when the task changes.
- B. Tune on the final test set.
- C. Discard all pretrained weights immediately.
- D. Freeze pretrained features and train a new task head.


### 4.1-M10 · MC

*Source: [PDF pp. 90–93](../Lecture%20Slides/4.1.%20CNNs.pdf#page=90).*

Instance segmentation differs from semantic segmentation by:

- A. Assigning no class labels to objects.
- B. Avoiding pixel-level outputs.
- C. Predicting only one class for the whole image.
- D. Separating distinct objects even when they have the same class.


## Short answers


### 4.1-S01 · Short

*Source: [PDF pp. 20–23](../Lecture%20Slides/4.1.%20CNNs.pdf#page=20).*

Define a unit's receptive field. Why can deeper convolutional layers use information from a larger input region?


### 4.1-S02 · Short

*Source: [PDF pp. 52–54, 61](../Lecture%20Slides/4.1.%20CNNs.pdf#page=52).*

What shape condition is needed to add a residual shortcut to a block output? How can a projection shortcut help when shapes differ?


### 4.1-S03 · Short

*Source: [PDF pp. 55–59](../Lecture%20Slides/4.1.%20CNNs.pdf#page=55).*

Contrast batch normalization and layer normalization in terms of which values contribute to their normalization statistics.


### 4.1-S04 · Short

*Source: [PDF pp. 64](../Lecture%20Slides/4.1.%20CNNs.pdf#page=64).*

What are the two operations in a depthwise-separable convolution? Which operation mixes channels?


### 4.1-S05 · Short

*Source: [PDF pp. 67–73](../Lecture%20Slides/4.1.%20CNNs.pdf#page=67).*

Distinguish frozen feature extraction from fine-tuning. Which weights change in each case?


### 4.1-S06 · Short

*Source: [PDF pp. 51–62, 75–79](../Lecture%20Slides/4.1.%20CNNs.pdf#page=51).*

A deeper plain CNN has higher training error than a shallower one. Why is this alone not evidence of overfitting? How can residual connections help?


### 4.1-S07 · Short

*Source: [PDF pp. 83–93](../Lecture%20Slides/4.1.%20CNNs.pdf#page=83).*

Distinguish the expected outputs of image classification, object detection, and semantic segmentation.


## Easy calculations


### 4.1-C01 · Calculation

*Source: [PDF pp. 15–17](../Lecture%20Slides/4.1.%20CNNs.pdf#page=15).*

A $7\times7$ input is convolved with a $3\times3$ kernel, stride 2, padding 1 per side, and dilation 1. Use $W_{out}=\lfloor(W-K+2P)/S\rfloor+1$ to compute output height and width.


### 4.1-C02 · Calculation

*Source: [PDF pp. 29–30](../Lecture%20Slides/4.1.%20CNNs.pdf#page=29).*

A standard $3\times3$ convolution has 2 input channels and 4 output channels, with one bias per output channel. Count the trainable scalar parameters.


### 4.1-C03 · Calculation

*Source: [PDF pp. 20–23](../Lecture%20Slides/4.1.%20CNNs.pdf#page=20).*

Two successive $3\times3$ convolutions both have stride 1 and dilation 1. For an interior output position, what is the receptive-field height and width in the original input?


# 5.1. Sequence Models

**Slides:** [5.1. Sequence Models.pdf](../Lecture%20Slides/5.1.%20Sequence%20Models.pdf). **20 questions: 10 MC · 7 short answers · 3 easy calculations.**


## Multiple choice


### 5.1-M01 · MC

*Source: [PDF pp. 4–6](../Lecture%20Slides/5.1.%20Sequence%20Models.pdf#page=4).*

What makes sequential data different from an unordered collection?

- A. Temporal dependencies are always absent.
- B. Ordering can change the meaning or prediction task.
- C. Sequence values must be categorical.
- D. Every sequence has the same length.


### 5.1-M02 · MC

*Source: [PDF pp. 6–9](../Lecture%20Slides/5.1.%20Sequence%20Models.pdf#page=6).*

As a trained RNN processes a sequence at inference time:

- A. It learns independent weights for each position.
- B. Its hidden state stays constant while weights change.
- C. Its hidden state changes while learned weights are shared across steps.
- D. Its hidden dimension grows with every token.


### 5.1-M03 · MC

*Source: [PDF pp. 7–9](../Lecture%20Slides/5.1.%20Sequence%20Models.pdf#page=7).*

The recurrent term involving $h_{t-1}$ allows the current computation to depend on:

- A. Only the current input.
- B. Only the future target label.
- C. Information carried from previous steps.
- D. A separate parameter file for every sequence.


### 5.1-M04 · MC

*Source: [PDF pp. 13–15](../Lecture%20Slides/5.1.%20Sequence%20Models.pdf#page=13).*

Vanishing gradients primarily make it difficult to:

- A. Learn dependencies spanning many recurrent steps.
- B. Calculate the number of tokens.
- C. Store the output vocabulary.
- D. Evaluate the current input's dimensions.


### 5.1-M05 · MC

*Source: [PDF pp. 16](../Lecture%20Slides/5.1.%20Sequence%20Models.pdf#page=16).*

Norm-based gradient clipping directly addresses:

- A. Every source of vanishing gradients.
- B. Excessively large gradient norms.
- C. Missing target labels.
- D. Insufficient vocabulary size.


### 5.1-M06 · MC

*Source: [PDF pp. 17–21](../Lecture%20Slides/5.1.%20Sequence%20Models.pdf#page=17).*

LSTM gating and its cell-state path help by:

- A. Making every hidden state equal to the input.
- B. Requiring an entire sequence to have one label.
- C. Controlling retention and updates through an additive memory path.
- D. Removing all trainable recurrent weights.


### 5.1-M07 · MC

*Source: [PDF pp. 21](../Lecture%20Slides/5.1.%20Sequence%20Models.pdf#page=21).*

Relative to an LSTM, the usual GRU:

- A. Has an additional separate cell state.
- B. Cannot process variable-length sequences.
- C. Has update/reset gates and no separate LSTM-style cell state.
- D. Uses no gates.


### 5.1-M08 · MC

*Source: [PDF pp. 22](../Lecture%20Slides/5.1.%20Sequence%20Models.pdf#page=22).*

A bidirectional RNN typically needs:

- A. Only previously observed inputs.
- B. A causal mask for its forward branch only.
- C. No recurrent state.
- D. Access to the sequence in both directions.


### 5.1-M09 · MC

*Source: [PDF pp. 28–29](../Lecture%20Slides/5.1.%20Sequence%20Models.pdf#page=28).*

Teacher forcing feeds the decoder:

- A. The final target sentence as a single class label.
- B. Only its own mistakes during training.
- C. The ground-truth next token at inference time.
- D. The ground-truth previous token during training.


### 5.1-M10 · MC

*Source: [PDF pp. 30](../Lecture%20Slides/5.1.%20Sequence%20Models.pdf#page=30).*

Attention addresses the basic seq2seq bottleneck by:

- A. Increasing the vocabulary indefinitely.
- B. Removing the input sequence.
- C. Forcing every decoder step to use identical context weights.
- D. Allowing output steps to access different weighted combinations of encoder states.


## Short answers


### 5.1-S01 · Short

*Source: [PDF pp. 6–9](../Lecture%20Slides/5.1.%20Sequence%20Models.pdf#page=6).*

Why does processing a longer sequence not by itself increase the number of trainable RNN parameters?


### 5.1-S02 · Short

*Source: [PDF pp. 14](../Lecture%20Slides/5.1.%20Sequence%20Models.pdf#page=14).*

What is backpropagation through time? What does truncating it trade away to save computation and memory?


### 5.1-S03 · Short

*Source: [PDF pp. 15–16](../Lecture%20Slides/5.1.%20Sequence%20Models.pdf#page=15).*

Why can repeated products of derivatives cause vanishing or exploding gradients? Does clipping large gradients fix the vanishing case?


### 5.1-S04 · Short

*Source: [PDF pp. 20–21](../Lecture%20Slides/5.1.%20Sequence%20Models.pdf#page=20).*

State the roles of the LSTM forget, input, and output gates in short phrases.


### 5.1-S05 · Short

*Source: [PDF pp. 25–27](../Lecture%20Slides/5.1.%20Sequence%20Models.pdf#page=25).*

What makes a temporal convolution causal? How can dilation expand access to earlier time steps?


### 5.1-S06 · Short

*Source: [PDF pp. 29](../Lecture%20Slides/5.1.%20Sequence%20Models.pdf#page=29).*

What is exposure bias in a teacher-forced decoder? Why can an early inference-time mistake affect later outputs?


### 5.1-S07 · Short

*Source: [PDF pp. 28–30](../Lecture%20Slides/5.1.%20Sequence%20Models.pdf#page=28).*

Why can a single fixed-size context vector become a bottleneck for long input sequences?


## Easy calculations


### 5.1-C01 · Calculation

*Source: [PDF pp. 6–9](../Lecture%20Slides/5.1.%20Sequence%20Models.pdf#page=6).*

A vanilla RNN has input dimension 2 and hidden dimension 3. Count parameters in $h_t=\tanh(W_xx_t+W_hh_{t-1}+b)$, using one hidden bias vector. Exclude any output layer.


### 5.1-C02 · Calculation

*Source: [PDF pp. 16](../Lecture%20Slides/5.1.%20Sequence%20Models.pdf#page=16).*

A gradient is $(3,4)$ with norm 5. Norm clipping limits it to norm 2. Compute the common rescaling factor and the clipped vector.


### 5.1-C03 · Calculation

*Source: [PDF pp. 25–27](../Lecture%20Slides/5.1.%20Sequence%20Models.pdf#page=25).*

A causal 1D convolution has kernel size 3, dilation 2, and stride 1. Using span $=1+(K-1)d$, how many time positions wide is its receptive field? How many positions are actually sampled by its three coefficients?


# 5.1. Extra Material

**Slides:** [5.1. Extra Material.pdf](../Lecture%20Slides/5.1.%20Extra%20Material.pdf). **20 questions: 10 MC · 7 short answers · 3 easy calculations.**


## Multiple choice


### 5.1E-M01 · MC

*Source: [PDF pp. 5–6](../Lecture%20Slides/5.1.%20Extra%20Material.pdf#page=5).*

In the tiny LSTM example, vocabulary size $V$ determines:

- A. The number of forget gates per hidden unit.
- B. The hidden-state size regardless of the architecture choice.
- C. The number of time steps in every sequence.
- D. The length of a one-hot input vector.


### 5.1E-M02 · MC

*Source: [PDF pp. 5–6](../Lecture%20Slides/5.1.%20Extra%20Material.pdf#page=5).*

With hidden size $H$, the LSTM cell state and hidden state have:

- A. $4H$ components each.
- B. $H$ components each.
- C. One component per vocabulary item.
- D. One component per training sequence.


### 5.1E-M03 · MC

*Source: [PDF pp. 5, 7](../Lecture%20Slides/5.1.%20Extra%20Material.pdf#page=5).*

For column-vector inputs, a single gate's input matrix $W_{xf}$ has shape:

- A. $V\times V$.
- B. $H\times V$.
- C. $H\times H$.
- D. $V\times H$ when used directly as $W_{xf}x$.


### 5.1E-M04 · MC

*Source: [PDF pp. 5, 7](../Lecture%20Slides/5.1.%20Extra%20Material.pdf#page=5).*

A single gate's recurrent matrix $W_{hf}$ has shape:

- A. $4V\times H$.
- B. $V\times H$.
- C. $V\times V$.
- D. $H\times H$.


### 5.1E-M05 · MC

*Source: [PDF pp. 6–7](../Lecture%20Slides/5.1.%20Extra%20Material.pdf#page=6).*

Multiplying an input matrix by the one-hot vector for letter b:

- A. Selects the column corresponding to b.
- B. Averages all vocabulary columns.
- C. Selects all recurrent weights at once.
- D. Selects the row for the predicted next letter.


### 5.1E-M06 · MC

*Source: [PDF pp. 2–4, 7](../Lecture%20Slides/5.1.%20Extra%20Material.pdf#page=2).*

If a forget-gate component is close to 0, it:

- A. Retains nearly all the previous cell component.
- B. Forces the output gate to 1.
- C. Suppresses that previous cell-state contribution.
- D. Removes the corresponding learned weights permanently.


### 5.1E-M07 · MC

*Source: [PDF pp. 2–4, 7](../Lecture%20Slides/5.1.%20Extra%20Material.pdf#page=2).*

If an input-gate component is zero, the candidate's contribution to that cell component is:

- A. Added without scaling.
- B. Doubled.
- C. Used as the output vocabulary size.
- D. Blocked.


### 5.1E-M08 · MC

*Source: [PDF pp. 2–4, 7](../Lecture%20Slides/5.1.%20Extra%20Material.pdf#page=2).*

The output gate primarily controls:

- A. The size of the vocabulary.
- B. The number of stored training sequences.
- C. How much of the transformed cell state is exposed as hidden output.
- D. Which input column is selected.


### 5.1E-M09 · MC

*Source: [PDF pp. 6](../Lecture%20Slides/5.1.%20Extra%20Material.pdf#page=6).*

Which quantities normally change while a trained LSTM reads a sequence without training updates?

- A. Vocabulary size at every step.
- B. All layer dimensions at every step.
- C. Only the weights.
- D. $c_t$ and $h_t$, while learned weights stay fixed.


### 5.1E-M10 · MC

*Source: [PDF pp. 5–7](../Lecture%20Slides/5.1.%20Extra%20Material.pdf#page=5).*

The next-token output matrix maps hidden size $H$ to vocabulary size $V$. Its output before softmax consists of:

- A. One probability automatically guaranteed to sum to 1.
- B. $V$ logits.
- C. $4H$ forget-gate values.
- D. $H$ independent cell memories.


## Short answers


### 5.1E-S01 · Short

*Source: [PDF pp. 2–6](../Lecture%20Slides/5.1.%20Extra%20Material.pdf#page=2).*

Distinguish the roles of cell state $c_t$ and hidden state $h_t$.


### 5.1E-S02 · Short

*Source: [PDF pp. 6](../Lecture%20Slides/5.1.%20Extra%20Material.pdf#page=6).*

Why is it incorrect to say that the cell state necessarily contains one entry per letter in the vocabulary?


### 5.1E-S03 · Short

*Source: [PDF pp. 5–6](../Lecture%20Slides/5.1.%20Extra%20Material.pdf#page=5).*

If a new vocabulary symbol is added while $H$ stays fixed, which input/output matrix dimensions change? Do $c_t$ and $h_t$ become longer?


### 5.1E-S04 · Short

*Source: [PDF pp. 5–6](../Lecture%20Slides/5.1.%20Extra%20Material.pdf#page=5).*

If $H$ increases while the vocabulary stays fixed, which families of parameters grow: input-gate matrices, recurrent matrices, output projection, or all three?


### 5.1E-S05 · Short

*Source: [PDF pp. 6–7](../Lecture%20Slides/5.1.%20Extra%20Material.pdf#page=6).*

Where is the learned input representation of a letter stored in a one-hot-input LSTM? Why can the same letter produce different hidden outputs in different contexts?


### 5.1E-S06 · Short

*Source: [PDF pp. 2–4, 7](../Lecture%20Slides/5.1.%20Extra%20Material.pdf#page=2).*

For $c_t=f_t\odot c_{t-1}+i_t\odot g_t$, what gate settings would approximately preserve the previous cell state without writing new content?


### 5.1E-S07 · Short

*Source: [PDF pp. 2–4, 7](../Lecture%20Slides/5.1.%20Extra%20Material.pdf#page=2).*

Why use sigmoid outputs for the forget/input/output gates, but allow the candidate update to contain negative as well as positive values?


## Easy calculations


### 5.1E-C01 · Calculation

*Source: [PDF pp. 5](../Lecture%20Slides/5.1.%20Extra%20Material.pdf#page=5).*

Count the parameters of an LSTM with input vocabulary size $V=3$ and hidden size $H=2$. Use four input matrices, four recurrent matrices, and one bias vector per gate: $4(HV+H^2+H)$. Exclude the output projection.


### 5.1E-C02 · Calculation

*Source: [PDF pp. 7](../Lecture%20Slides/5.1.%20Extra%20Material.pdf#page=7).*

For one cell component, $c_{t-1}=2$, $f_t=0.5$, $i_t=0.25$, and $g_t=0.8$. Compute $c_t=f_tc_{t-1}+i_tg_t$.


### 5.1E-C03 · Calculation

*Source: [PDF pp. 7](../Lecture%20Slides/5.1.%20Extra%20Material.pdf#page=7).*

For one hidden component, the output gate is $o_t=0.5$ and $\tanh(c_t)=0.8$. Compute $h_t=o_t\tanh(c_t)$. What would $h_t$ be if $o_t=0$?


# 5.2. Transformers

**Slides:** [5.2. Transformers.pdf](../Lecture%20Slides/5.2.%20Transformers.pdf). **20 questions: 10 MC · 7 short answers · 3 easy calculations.**


## Multiple choice


### 5.2-M01 · MC

*Source: [PDF pp. 8–13](../Lecture%20Slides/5.2.%20Transformers.pdf#page=8).*

Before softmax, attention scores are computed from:

- A. Ground-truth class labels.
- B. Only the value-vector norms.
- C. Only token indices, without content.
- D. Query–key similarities.


### 5.2-M02 · MC

*Source: [PDF pp. 9–13](../Lecture%20Slides/5.2.%20Transformers.pdf#page=9).*

The output for one query is:

- A. An unweighted sum of keys.
- B. A fixed learned vector independent of the inputs.
- C. The query with its largest component removed.
- D. A weighted sum of value vectors.


### 5.2-M03 · MC

*Source: [PDF pp. 13](../Lecture%20Slides/5.2.%20Transformers.pdf#page=13).*

Dividing dot products by $\sqrt{d_k}$ helps:

- A. Replace positional information.
- B. Reduce the number of tokens.
- C. Control score scale and avoid excessive softmax saturation.
- D. Make all attention weights equal.


### 5.2-M04 · MC

*Source: [PDF pp. 11, 15–17](../Lecture%20Slides/5.2.%20Transformers.pdf#page=11).*

Why supply positional information to self-attention?

- A. To remove all learned embeddings.
- B. To convert every token into a class label.
- C. Unmasked self-attention alone does not identify sequence positions.
- D. To prevent GPU parallelism.


### 5.2-M05 · MC

*Source: [PDF pp. 19–20](../Lecture%20Slides/5.2.%20Transformers.pdf#page=19).*

Subword tokenization is useful partly because it:

- A. Assigns a separate vocabulary to every sentence.
- B. Represents rare words using smaller reusable pieces.
- C. Requires each word to be a unique vocabulary entry.
- D. Eliminates all sequence-length limits.


### 5.2-M06 · MC

*Source: [PDF pp. 20–22](../Lecture%20Slides/5.2.%20Transformers.pdf#page=20).*

A contextual embedding differs from a basic token lookup because it:

- A. Is necessarily identical for every occurrence of a token.
- B. Can reflect the surrounding tokens available to the model.
- C. Has no learned parameters anywhere in its computation.
- D. Must always be one-hot.


### 5.2-M07 · MC

*Source: [PDF pp. 24](../Lecture%20Slides/5.2.%20Transformers.pdf#page=24).*

Multi-head attention uses:

- A. A separate target label for every head.
- B. Only one shared scalar weight for all token pairs.
- C. A different vocabulary for each head.
- D. Several learned projection sets to model relationships in parallel.


### 5.2-M08 · MC

*Source: [PDF pp. 30–31](../Lecture%20Slides/5.2.%20Transformers.pdf#page=30).*

At input position $t$ predicting token $t+1$, the usual causal mask permits attention to:

- A. Only position $t+1$.
- B. Only future positions.
- C. Input positions $1,\ldots,t$.
- D. Every position except $t$.


### 5.2-M09 · MC

*Source: [PDF pp. 32–35](../Lecture%20Slides/5.2.%20Transformers.pdf#page=32).*

In encoder–decoder cross-attention:

- A. Queries come from decoder representations; keys and values come from encoder output.
- B. Queries, keys, and values must all come from the same sequence.
- C. The encoder queries future decoder outputs.
- D. Keys are the future target labels.


### 5.2-M10 · MC

*Source: [PDF pp. 36](../Lecture%20Slides/5.2.%20Transformers.pdf#page=36).*

For fixed dimensions, doubling token count multiplies the number of entries in a full attention score matrix by:

- A. Two.
- B. One: it stays unchanged.
- C. Eight.
- D. Four.


## Short answers


### 5.2-S01 · Short

*Source: [PDF pp. 23–27](../Lecture%20Slides/5.2.%20Transformers.pdf#page=23).*

What different jobs are performed by self-attention and the per-token feed-forward MLP in a transformer block?


### 5.2-S02 · Short

*Source: [PDF pp. 25, 27](../Lecture%20Slides/5.2.%20Transformers.pdf#page=25).*

What do the residual connection and layer normalization contribute in an Add & Norm component?


### 5.2-S03 · Short

*Source: [PDF pp. 28–35](../Lecture%20Slides/5.2.%20Transformers.pdf#page=28).*

Contrast encoder-only, decoder-only, and encoder–decoder models by their attention access and one typical task each.


### 5.2-S04 · Short

*Source: [PDF pp. 30–31](../Lecture%20Slides/5.2.%20Transformers.pdf#page=30).*

Why can next-token training evaluate all known sequence positions in parallel while ordinary autoregressive generation produces new tokens sequentially?


### 5.2-S05 · Short

*Source: [PDF pp. 16–17](../Lecture%20Slides/5.2.%20Transformers.pdf#page=16).*

Contrast learned absolute position embeddings with RoPE in terms of where positional information is introduced.


### 5.2-S06 · Short

*Source: [PDF pp. 36](../Lecture%20Slides/5.2.%20Transformers.pdf#page=36).*

What does a KV cache store during autoregressive generation, and what repeated computation does it avoid?


### 5.2-S07 · Short

*Source: [PDF pp. 37–40](../Lecture%20Slides/5.2.%20Transformers.pdf#page=37).*

How does a Vision Transformer turn an image into a sequence? Why must spatial positions also be represented?


## Easy calculations


### 5.2-C01 · Calculation

*Source: [PDF pp. 9–13](../Lecture%20Slides/5.2.%20Transformers.pdf#page=9).*

Attention weights are $(0.25,0.75)$ over scalar values 2 and 6. Compute the attention output.


### 5.2-C02 · Calculation

*Source: [PDF pp. 13, 24](../Lecture%20Slides/5.2.%20Transformers.pdf#page=13).*

One attention head maps model dimension 4 into query, key, and value dimensions of 2 each. Count the parameters in its three projection matrices. Assume no biases and exclude the output projection.


### 5.2-C03 · Calculation

*Source: [PDF pp. 37–39](../Lecture%20Slides/5.2.%20Transformers.pdf#page=37).*

A $32\times32$ image is divided into non-overlapping $8\times8$ patches. How many patch tokens are produced? How many tokens are there after adding one CLS token?


# 5.3. Foundation models

**Slides:** [5.3. Foundation models.pdf](../Lecture%20Slides/5.3.%20Foundation%20models.pdf). **20 questions: 10 MC · 7 short answers · 3 easy calculations.**


## Multiple choice


### 5.3-M01 · MC

*Source: [PDF pp. 9–13](../Lecture%20Slides/5.3.%20Foundation%20models.pdf#page=9).*

A foundation model is primarily characterized by:

- A. A fixed minimum layer count.
- B. Broad pretraining and adaptability to many downstream tasks.
- C. Always using one particular architecture.
- D. Being trained separately from scratch for each input.


### 5.3-M02 · MC

*Source: [PDF pp. 13–15](../Lecture%20Slides/5.3.%20Foundation%20models.pdf#page=13).*

Self-supervised pretraining obtains targets:

- A. Only from interactive rewards.
- B. From the training data itself.
- C. From held-out test labels.
- D. Only from manually annotated classes.


### 5.3-M03 · MC

*Source: [PDF pp. 14](../Lecture%20Slides/5.3.%20Foundation%20models.pdf#page=14).*

Supervised fine-tuning primarily learns from:

- A. An automatic guarantee that responses are correct.
- B. Demonstrations or supplied input–target examples.
- C. Only the original pretraining vocabulary size.
- D. Random actions without targets.


### 5.3-M04 · MC

*Source: [PDF pp. 14](../Lecture%20Slides/5.3.%20Foundation%20models.pdf#page=14).*

Preference-based RL uses feedback that concerns:

- A. A required correct token label for every position.
- B. Only the number of network layers.
- C. Only how often a token occurs in raw text.
- D. Which sampled outputs are preferred or receive greater reward.


### 5.3-M05 · MC

*Source: [PDF pp. 14](../Lecture%20Slides/5.3.%20Foundation%20models.pdf#page=14).*

Which is an example of a verifiable reward?

- A. A random score independent of the output.
- B. The number of training parameters alone.
- C. Whether generated code passes specified unit tests.
- D. A manually supplied next-token label by definition.


### 5.3-M06 · MC

*Source: [PDF pp. 19–20](../Lecture%20Slides/5.3.%20Foundation%20models.pdf#page=19).*

CLIP learns:

- A. A separate encoder for every future class name.
- B. A transition model for an RL environment.
- C. A shared representation space for images and text.
- D. Only a pixel reconstruction model.


### 5.3-M07 · MC

*Source: [PDF pp. 19–20](../Lecture%20Slides/5.3.%20Foundation%20models.pdf#page=19).*

Zero-shot CLIP-style classification can compare an image with:

- A. Text embeddings of candidate class descriptions.
- B. Only its original image filename.
- C. Only classes represented by newly trained classifier weights.
- D. A table of true test labels.


### 5.3-M08 · MC

*Source: [PDF pp. 21](../Lecture%20Slides/5.3.%20Foundation%20models.pdf#page=21).*

DINOv2 is presented as learning visual representations through:

- A. Predicting text tokens only.
- B. Fully labelled segmentation masks for every image.
- C. Self-supervised teacher–student learning from image views.
- D. An image generator competing with a discriminator.


### 5.3-M09 · MC

*Source: [PDF pp. 22](../Lecture%20Slides/5.3.%20Foundation%20models.pdf#page=22).*

SAM is associated with:

- A. Segmentation.
- B. Document-topic discovery.
- C. Polynomial regression.
- D. Tabular Q-learning.


### 5.3-M10 · MC

*Source: [PDF pp. 14, 17, 19–25](../Lecture%20Slides/5.3.%20Foundation%20models.pdf#page=14).*

In this context, multimodal learning combines information from:

- A. Only different train/test splits.
- B. Different modalities, such as images and text.
- C. Only different learning rates.
- D. Multiple random seeds for the same model.


## Short answers


### 5.3-S01 · Short

*Source: [PDF pp. 10–14](../Lecture%20Slides/5.3.%20Foundation%20models.pdf#page=10).*

Distinguish broad pretraining from adaptation to a downstream task. Why can reusing pretrained features reduce the need for task-specific labelled data?


### 5.3-S02 · Short

*Source: [PDF pp. 12, 26](../Lecture%20Slides/5.3.%20Foundation%20models.pdf#page=12).*

Why can biases in a widely reused foundation model affect many downstream applications?


### 5.3-S03 · Short

*Source: [PDF pp. 12](../Lecture%20Slides/5.3.%20Foundation%20models.pdf#page=12).*

For a mixture-of-experts model, why can total parameter count differ from the number of parameters active for one token? Which count still matters for storing all experts?


### 5.3-S04 · Short

*Source: [PDF pp. 14](../Lecture%20Slides/5.3.%20Foundation%20models.pdf#page=14).*

Distinguish human demonstrations, preference rankings, and automatically verifiable rewards as training signals.


### 5.3-S05 · Short

*Source: [PDF pp. 19–20](../Lecture%20Slides/5.3.%20Foundation%20models.pdf#page=19).*

Explain CLIP-style zero-shot classification in two steps, from candidate class descriptions to a predicted class.


### 5.3-S06 · Short

*Source: [PDF pp. 21](../Lecture%20Slides/5.3.%20Foundation%20models.pdf#page=21).*

How can a visual encoder learn useful features without semantic class labels? Describe the role of different views of one image in teacher–student training.


### 5.3-S07 · Short

*Source: [PDF pp. 24–25](../Lecture%20Slides/5.3.%20Foundation%20models.pdf#page=24).*

In a text-conditioned image generator, distinguish the role of the text encoder from that of the image-generation model.


## Easy calculations


### 5.3-C01 · Calculation

*Source: [PDF pp. 12](../Lecture%20Slides/5.3.%20Foundation%20models.pdf#page=12).*

A toy model has 10 million parameters stored in FP32, using 4 bytes per parameter. Ignoring all other tensors and metadata, compute its weight storage in decimal MB ($1\,\mathrm{MB}=10^6$ bytes).


### 5.3-C02 · Calculation

*Source: [PDF pp. 19–20](../Lecture%20Slides/5.3.%20Foundation%20models.pdf#page=19).*

An image has unit embedding $(1,0)$. Two candidate descriptions have unit embeddings $t_A=(0.8,0.6)$ and $t_B=(0,1)$. Compute both dot-product similarities and select the higher-similarity description.


### 5.3-C03 · Calculation

*Source: [PDF pp. 12](../Lecture%20Slides/5.3.%20Foundation%20models.pdf#page=12).*

A toy mixture-of-experts contains 8 experts with 4 million parameters each and activates 2 experts per token. Ignore shared parameters. Compute the total expert parameters and the active expert parameters per token.


# 5.4. Unsupervised learning

**Slides:** [5.4. Unsupervised learning.pdf](../Lecture%20Slides/5.4.%20Unsupervised%20learning.pdf). **20 questions: 10 MC · 7 short answers · 3 easy calculations.**


## Multiple choice


### 5.4-M01 · MC

*Source: [PDF pp. 6–7](../Lecture%20Slides/5.4.%20Unsupervised%20learning.pdf#page=6).*

Semi-supervised learning uses:

- A. Only a smaller supervised learning rate.
- B. Only labels from the test set.
- C. Labelled examples together with relevant unlabelled examples.
- D. Only rewards from an interactive environment.


### 5.4-M02 · MC

*Source: [PDF pp. 9–11](../Lecture%20Slides/5.4.%20Unsupervised%20learning.pdf#page=9).*

For centred data, the first principal component is the unit direction that:

- A. Gives the greatest projected variance.
- B. Maximizes labelled classification accuracy by definition.
- C. Gives the smallest projected variance.
- D. Selects the feature with the shortest name.


### 5.4-M03 · MC

*Source: [PDF pp. 13–18, 36](../Lecture%20Slides/5.4.%20Unsupervised%20learning.pdf#page=13).*

A defensible interpretation of t-SNE is that it mainly aims to preserve:

- A. All pairwise distances exactly.
- B. Local neighbourhood structure in a low-dimensional visualization.
- C. Cluster sizes as exact population proportions.
- D. Only the covariance eigenvalues.


### 5.4-M04 · MC

*Source: [PDF pp. 15](../Lecture%20Slides/5.4.%20Unsupervised%20learning.pdf#page=15).*

The t-SNE perplexity hyperparameter is related to:

- A. The neural-network layer count.
- B. The effective neighbourhood scale used by the method.
- C. The number of labels per image.
- D. The number of semantic classes, fixed exactly.


### 5.4-M05 · MC

*Source: [PDF pp. 20](../Lecture%20Slides/5.4.%20Unsupervised%20learning.pdf#page=20).*

Standard k-means alternates:

- A. Maximizing variance and sorting eigenvectors.
- B. Class-label annotation and supervised backpropagation.
- C. Nearest-centre assignments and recomputation of centres as means.
- D. Only merging existing clusters, never moving centres.


### 5.4-M06 · MC

*Source: [PDF pp. 21](../Lecture%20Slides/5.4.%20Unsupervised%20learning.pdf#page=21).*

Agglomerative hierarchical clustering starts with:

- A. Individual points as clusters and progressively merges them.
- B. Exactly one cluster per known class label.
- C. A trained decoder generating new points.
- D. All points permanently in one cluster.


### 5.4-M07 · MC

*Source: [PDF pp. 22](../Lecture%20Slides/5.4.%20Unsupervised%20learning.pdf#page=22).*

Latent Dirichlet allocation models a document as:

- A. A single principal component.
- B. A mixture of topics.
- C. One mandatory hard cluster assignment only.
- D. A sequence of RL states.


### 5.4-M08 · MC

*Source: [PDF pp. 26–27](../Lecture%20Slides/5.4.%20Unsupervised%20learning.pdf#page=26).*

Which is a self-supervised pretext task?

- A. Predicting an image rotation that was applied automatically.
- B. Asking a human to label every object category.
- C. Learning solely from externally assigned rewards.
- D. Selecting a model using test labels.


### 5.4-M09 · MC

*Source: [PDF pp. 28–29](../Lecture%20Slides/5.4.%20Unsupervised%20learning.pdf#page=28).*

With positive and negative pairs, a contrastive objective generally encourages:

- A. Similar representations for positives and separation from negatives.
- B. Identical representations for every input.
- C. Greater distance between all positive pairs.
- D. Raw pixel reconstruction as its only objective.


### 5.4-M10 · MC

*Source: [PDF pp. 30–31](../Lecture%20Slides/5.4.%20Unsupervised%20learning.pdf#page=30).*

The basic BYOL approach is notable for:

- A. Needing a separate classifier for every image.
- B. Learning from two views using online/target networks without explicit negatives.
- C. Requiring manually labelled negative examples.
- D. Replacing the encoder with k-means.


## Short answers


### 5.4-S01 · Short

*Source: [PDF pp. 8–23](../Lecture%20Slides/5.4.%20Unsupervised%20learning.pdf#page=8).*

Distinguish dimensionality reduction from clustering. What is the output of each?


### 5.4-S02 · Short

*Source: [PDF pp. 10–11](../Lecture%20Slides/5.4.%20Unsupervised%20learning.pdf#page=10).*

What does retaining 90% of variance with PCA mean? Does it imply 90% classification accuracy?


### 5.4-S03 · Short

*Source: [PDF pp. 13–15](../Lecture%20Slides/5.4.%20Unsupervised%20learning.pdf#page=13).*

Why should a visible gap between groups in a t-SNE plot not automatically be interpreted as proof of separate true classes?


### 5.4-S04 · Short

*Source: [PDF pp. 20](../Lecture%20Slides/5.4.%20Unsupervised%20learning.pdf#page=20).*

Why can k-means results depend on the initial centres? Does one run guarantee the globally best clustering?


### 5.4-S05 · Short

*Source: [PDF pp. 25–28](../Lecture%20Slides/5.4.%20Unsupervised%20learning.pdf#page=25).*

Why can self-supervised learning have a supervised-looking loss even though semantic class labels are not manually supplied?


### 5.4-S06 · Short

*Source: [PDF pp. 28–31](../Lecture%20Slides/5.4.%20Unsupervised%20learning.pdf#page=28).*

What is representation collapse? Why would mapping every input to the same vector be unhelpful for downstream tasks?


### 5.4-S07 · Short

*Source: [PDF pp. 6–7, 33](../Lecture%20Slides/5.4.%20Unsupervised%20learning.pdf#page=6).*

Why might unlabelled examples from an unrelated distribution fail to help a semi-supervised task?


## Easy calculations


### 5.4-C01 · Calculation

*Source: [PDF pp. 10–11](../Lecture%20Slides/5.4.%20Unsupervised%20learning.pdf#page=10).*

Covariance eigenvalues are 6, 3, and 1. What fraction of total variance is retained by the first two principal components?


### 5.4-C02 · Calculation

*Source: [PDF pp. 20](../Lecture%20Slides/5.4.%20Unsupervised%20learning.pdf#page=20).*

Three 1D points, 2, 4, and 9, are assigned to the same k-means cluster. Compute its updated centre.


### 5.4-C03 · Calculation

*Source: [PDF pp. 20](../Lecture%20Slides/5.4.%20Unsupervised%20learning.pdf#page=20).*

Two 1D k-means centres are 0 and 10. For a point at 7, compute its distance to each centre and state its next assignment.


# 5.5. Generative Models

**Slides:** [5.5. Generative Models.pdf](../Lecture%20Slides/5.5.%20Generative%20Models.pdf). **20 questions: 10 MC · 7 short answers · 3 easy calculations.**


## Multiple choice


### 5.5-M01 · MC

*Source: [PDF pp. 3–6](../Lecture%20Slides/5.5.%20Generative%20Models.pdf#page=3).*

Generative modelling primarily aims to:

- A. Only select a class boundary.
- B. Store every possible input without a model.
- C. Remove all uncertainty from observed data.
- D. Learn a data distribution or sampling mechanism from examples.


### 5.5-M02 · MC

*Source: [PDF pp. 7](../Lecture%20Slides/5.5.%20Generative%20Models.pdf#page=7).*

A basic autoencoder is normally trained to:

- A. Sort examples by filename.
- B. Predict an unrelated class label.
- C. Reconstruct its input through an internal representation.
- D. Estimate a reward for an action.


### 5.5-M03 · MC

*Source: [PDF pp. 7–8](../Lecture%20Slides/5.5.%20Generative%20Models.pdf#page=7).*

The latent vector in a basic autoencoder is:

- A. Necessarily a one-hot vocabulary vector.
- B. The optimizer's learning-rate schedule.
- C. Necessarily the true semantic class label.
- D. An encoded representation used by the decoder.


### 5.5-M04 · MC

*Source: [PDF pp. 8](../Lecture%20Slides/5.5.%20Generative%20Models.pdf#page=8).*

Compared with a deterministic autoencoder, a VAE typically encodes:

- A. Parameters of a distribution over latent variables.
- B. Only an adversarial real/fake decision.
- C. Only one hard class index.
- D. Only the reconstruction error.


### 5.5-M05 · MC

*Source: [PDF pp. 8](../Lecture%20Slides/5.5.%20Generative%20Models.pdf#page=8).*

The KL regularization term in a VAE encourages:

- A. Removal of the reconstruction objective.
- B. Every reconstruction to be identical.
- C. Infinite latent variance for every input.
- D. The latent distribution to agree with a chosen prior.


### 5.5-M06 · MC

*Source: [PDF pp. 9–12](../Lecture%20Slides/5.5.%20Generative%20Models.pdf#page=9).*

In a GAN, the discriminator learns to:

- A. Distinguish real data from generated samples.
- B. Generate images from noise directly.
- C. Compute PCA directions.
- D. Assign a unique latent vector to every real image.


### 5.5-M07 · MC

*Source: [PDF pp. 11–12](../Lecture%20Slides/5.5.%20Generative%20Models.pdf#page=11).*

The GAN generator is trained to:

- A. Output only its noise input unchanged.
- B. Replace every real training example with a label.
- C. Produce samples the discriminator judges as real.
- D. Maximize the discriminator's ability to reject its samples.


### 5.5-M08 · MC

*Source: [PDF pp. 13](../Lecture%20Slides/5.5.%20Generative%20Models.pdf#page=13).*

A generator produces only a few similar outputs despite varied noise inputs. This is:

- A. Feature normalization.
- B. Gradient clipping.
- C. Teacher forcing.
- D. Mode collapse.


### 5.5-M09 · MC

*Source: [PDF pp. 17–18](../Lecture%20Slides/5.5.%20Generative%20Models.pdf#page=17).*

The forward process in a basic diffusion model:

- A. Removes all noise in one exact inverse operation.
- B. Progressively adds noise to data.
- C. Learns to classify data into semantic categories.
- D. Uses a discriminator to reject samples.


### 5.5-M10 · MC

*Source: [PDF pp. 18–21](../Lecture%20Slides/5.5.%20Generative%20Models.pdf#page=18).*

Sampling with a standard diffusion model starts from noise and uses:

- A. A fixed lookup table of training images.
- B. Only an image classifier's class index.
- C. Only the forward noise-addition process.
- D. A learned sequence of denoising steps.


## Short answers


### 5.5-S01 · Short

*Source: [PDF pp. 3–6](../Lecture%20Slides/5.5.%20Generative%20Models.pdf#page=3).*

Contrast learning $p(y\mid x)$ for classification with learning a model that can generate data. Can generative models be conditioned on labels or prompts?


### 5.5-S02 · Short

*Source: [PDF pp. 7–8](../Lecture%20Slides/5.5.%20Generative%20Models.pdf#page=7).*

Why can reconstructing inputs through a constrained latent representation encourage useful feature learning?


### 5.5-S03 · Short

*Source: [PDF pp. 8](../Lecture%20Slides/5.5.%20Generative%20Models.pdf#page=8).*

Why might a basic autoencoder decode an arbitrary random latent vector poorly? What changes in a VAE make sampling more structured?


### 5.5-S04 · Short

*Source: [PDF pp. 8](../Lecture%20Slides/5.5.%20Generative%20Models.pdf#page=8).*

What trade-off exists between reconstruction quality and latent-prior regularization in a VAE objective?


### 5.5-S05 · Short

*Source: [PDF pp. 11–13](../Lecture%20Slides/5.5.%20Generative%20Models.pdf#page=11).*

Why can GAN training be unstable when the generator and discriminator learn at different rates?


### 5.5-S06 · Short

*Source: [PDF pp. 17–18](../Lecture%20Slides/5.5.%20Generative%20Models.pdf#page=17).*

Distinguish the fixed forward noising process from the learned reverse process in diffusion.


### 5.5-S07 · Short

*Source: [PDF pp. 5, 21–22](../Lecture%20Slides/5.5.%20Generative%20Models.pdf#page=5).*

Contrast next-token prediction with diffusion denoising. Why can standard iterative diffusion sampling require many model evaluations per generated image?


## Easy calculations


### 5.5-C01 · Calculation

*Source: [PDF pp. 7](../Lecture%20Slides/5.5.%20Generative%20Models.pdf#page=7).*

An autoencoder reconstructs input $(1,3)$ as $(2,1)$. Compute the mean squared reconstruction error over these two components.


### 5.5-C02 · Calculation

*Source: [PDF pp. 8](../Lecture%20Slides/5.5.%20Generative%20Models.pdf#page=8).*

A toy VAE objective is $L=L_{recon}+\beta D_{KL}$. If $L_{recon}=3$, $D_{KL}=2$, and $\beta=0.5$, compute $L$. What happens to this fixed example's loss if $\beta$ increases?


### 5.5-C03 · Calculation

*Source: [PDF pp. 17](../Lecture%20Slides/5.5.%20Generative%20Models.pdf#page=17).*

For a toy scalar forward-noising step, use $x_t=0.8x_0+0.6\epsilon$. With clean value $x_0=2$ and sampled noise $\epsilon=-1$, compute $x_t$. The coefficients and sampled noise are supplied; no distribution calculation is needed.


# Lab 4. manolo_presentation — Explainability and model compression

**Slides:** [manolo_presentation.pdf](../Lab%20Sessions/Lab4/manolo_presentation.pdf). **20 questions: 10 MC · 7 short answers · 3 easy calculations.**


Supplement from the Lab 4 briefing. This is separate from the numbered lecture PDFs.


## Multiple choice


### L4-M01 · MC

*Source: [PDF pp. 2, 7](../Lab%20Sessions/Lab4/manolo_presentation.pdf#page=2).*

Grad-CAM highlights:

- A. Only the brightest input pixels.
- B. The ground-truth segmentation mask automatically.
- C. Regions supporting a selected class score according to a gradient-based attribution.
- D. The exact causal explanation for every decision.


### L4-M02 · MC

*Source: [PDF pp. 7](../Lab%20Sessions/Lab4/manolo_presentation.pdf#page=7).*

A plausible-looking attribution heatmap is:

- A. Proof that the model learned the intended causal mechanism.
- B. Evidence to investigate, with limitations and possible failure modes.
- C. A substitute for evaluating predictions.
- D. A guarantee of fairness across all groups.


### L4-M03 · MC

*Source: [PDF pp. 8–9](../Lab%20Sessions/Lab4/manolo_presentation.pdf#page=8).*

FP32-to-INT8 quantization primarily changes:

- A. The definition of the target labels.
- B. The number of output classes.
- C. Every convolution's spatial dimensions.
- D. The numerical representation and precision of model values.


### L4-M04 · MC

*Source: [PDF pp. 9](../Lab%20Sessions/Lab4/manolo_presentation.pdf#page=9).*

Calibration for post-training static quantization is used to:

- A. Delete the smallest weights.
- B. Learn a new semantic label for each neuron.
- C. Create new output classes.
- D. Estimate representative activation ranges for quantization settings.


### L4-M05 · MC

*Source: [PDF pp. 10](../Lab%20Sessions/Lab4/manolo_presentation.pdf#page=10).*

Magnitude-based pruning typically targets:

- A. All biases regardless of importance.
- B. Weights with small absolute values.
- C. Only the largest positive weights.
- D. Only the training examples with large loss.


### L4-M06 · MC

*Source: [PDF pp. 10](../Lab%20Sessions/Lab4/manolo_presentation.pdf#page=10).*

Unstructured pruning may give little speed-up with dense kernels because:

- A. Zero weights always use more storage than nonzero weights.
- B. The dense implementation may still store and process zero entries.
- C. It prevents the model from running on a CPU.
- D. It increases the number of channels by definition.


### L4-M07 · MC

*Source: [PDF pp. 10](../Lab%20Sessions/Lab4/manolo_presentation.pdf#page=10).*

Structured pruning can remove:

- A. Only the learned learning rate.
- B. Only the validation labels.
- C. Entire channels or filters, shrinking tensor dimensions.
- D. Only isolated scalar weights.


### L4-M08 · MC

*Source: [PDF pp. 8](../Lab%20Sessions/Lab4/manolo_presentation.pdf#page=8).*

Knowledge distillation trains:

- A. A new vocabulary for the teacher.
- B. A discriminator to reject synthetic images.
- C. A larger model to memorize every student error.
- D. A student to imitate a teacher's outputs or representations.


### L4-M09 · MC

*Source: [PDF pp. 5, 11](../Lab%20Sessions/Lab4/manolo_presentation.pdf#page=5).*

Unchanged average accuracy after compression:

- A. Establishes that latency improved.
- B. Proves unchanged explanations for every image.
- C. Can still hide deterioration for rare classes or subgroups.
- D. Guarantees unchanged performance for every subgroup.


### L4-M10 · MC

*Source: [PDF pp. 6](../Lab%20Sessions/Lab4/manolo_presentation.pdf#page=6).*

One reason to run a model on an edge device is:

- A. Guaranteed better accuracy than the same model on a server.
- B. Unlimited memory and energy.
- C. No need to measure inference latency.
- D. Reduced reliance on network connectivity and remote data transfer.


## Short answers


### L4-S01 · Short

*Source: [PDF pp. 2, 7](../Lab%20Sessions/Lab4/manolo_presentation.pdf#page=2).*

Why is Grad-CAM usually spatially coarse? How is this related to the resolution of the selected feature maps?


### L4-S02 · Short

*Source: [PDF pp. 5, 7](../Lab%20Sessions/Lab4/manolo_presentation.pdf#page=5).*

A classifier's heatmap focuses on a watermark rather than the object. What concern does this raise, and what targeted data check could you make?


### L4-S03 · Short

*Source: [PDF pp. 8–10](../Lab%20Sessions/Lab4/manolo_presentation.pdf#page=8).*

Distinguish quantization from pruning. What does each change in the model's numerical representation or structure?


### L4-S04 · Short

*Source: [PDF pp. 9](../Lab%20Sessions/Lab4/manolo_presentation.pdf#page=9).*

Why should quantization calibration inputs resemble the intended deployment data?


### L4-S05 · Short

*Source: [PDF pp. 10](../Lab%20Sessions/Lab4/manolo_presentation.pdf#page=10).*

Why can fine-tuning after pruning help recover performance? Does high sparsity alone guarantee a smaller dense model file?


### L4-S06 · Short

*Source: [PDF pp. 10–11](../Lab%20Sessions/Lab4/manolo_presentation.pdf#page=10).*

Name three measurements, besides overall accuracy, that help assess a compressed model's usefulness.


### L4-S07 · Short

*Source: [PDF pp. 5, 11](../Lab%20Sessions/Lab4/manolo_presentation.pdf#page=5).*

Why re-evaluate per-class performance and inspect explanations after compression, even if overall accuracy barely changes?


## Easy calculations


### L4-C01 · Calculation

*Source: [PDF pp. 9](../Lab%20Sessions/Lab4/manolo_presentation.pdf#page=9).*

One million weights are stored using either 32 or 8 bits per weight. Ignoring metadata, compute both storage sizes in decimal MB and the reduction factor.


### L4-C02 · Calculation

*Source: [PDF pp. 10](../Lab%20Sessions/Lab4/manolo_presentation.pdf#page=10).*

Pruning sets 600 of 1,000 weights to zero. Compute sparsity and the remaining nonzero-weight count.


### L4-C03 · Calculation

*Source: [PDF pp. 6, 11](../Lab%20Sessions/Lab4/manolo_presentation.pdf#page=6).*

Measured inference latency falls from 40 ms to 10 ms after compression. Compute the speed-up factor and the percentage reduction in latency.
