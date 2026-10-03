# Revision of the REINFORCE experiment

This review covers the final experiment cell of
`lab_2_policy_search_pytorch.ipynb`, which trains a linear policy on
`CartPole-v1`.

## Current configuration

```python
policy_name = 'linear'
env_name = 'CartPole-v1'
learning_rate = 0.01
discount_factor = 0.99
num_episodes = 1000
eval_freq = 100
render_mode = 'final'
```

The choice of a linear softmax policy is appropriate for the exercise: it
keeps the model simple and makes the REINFORCE update easy to inspect. The
discount factor `gamma = 0.99` is also reasonable for CartPole because the
objective is to survive for as many time steps as possible.

## Code improvements

### 1. Evaluation should use a separate environment

The current code evaluates the policy using the same wrapped environment used
for training. Since that environment is wrapped with `RecordVideo`, evaluation
can create unnecessary video files and mix training and evaluation state.

Use one environment for training and another for evaluation. Only wrap the
evaluation environment when a video is requested.

### 2. Logging fails for non-linear policies

`reinforce()` initializes `optimizer` and `scheduler` to `None`, but the
logging block always evaluates:

```python
current_lr = scheduler.get_last_lr()[0]
loss.item()
```

If `policy_name` is `naive` or `random`, `scheduler` and `loss` do not exist in
that execution path. Logging should either be conditional on the policy being
trained or use values that are defined for every policy.

### 3. The video wrapper is always enabled

`wrap_env()` always creates a `RecordVideo` wrapper, even when
`render_mode='none'`. This adds overhead and can fill the video directory
during a normal training run. Create the wrapper only for an experiment that
actually needs recorded frames.

### 4. The policy gradient has high variance

The loss uses the raw return-to-go. This is mathematically valid, but vanilla
REINFORCE can be unstable. Useful improvements are:

- normalize the returns within each episode or batch;
- subtract a baseline, such as the mean return or a learned value estimate;
- collect several episodes before performing one optimizer update.

These changes do not alter the policy-gradient objective; they reduce the
variance of its estimate.

### 5. Reproducibility is missing

The experiment does not set seeds for Python, NumPy, PyTorch, or the Gymnasium
environment. A single successful run is therefore not enough to call the
parameters "best". Run several seeds and report the mean and standard
deviation of the evaluation score.

### 6. `run_episode()` stores log probabilities during evaluation

When `train=False`, actions are selected greedily, but log probabilities are
still appended. They are not used during evaluation. Returning an empty list
for evaluation would make the intent clearer and avoid unnecessary tensor
creation.

### 7. The random policy class has a separate bug

`RandomPolicy.__init__()` does not store `n_actions`, although `forward()` uses
`self.n_actions`. It should contain:

```python
self.n_actions = n_actions
```

Without this assignment, selecting the random policy raises an
`AttributeError`.

## Parameter assessment

### Learning rate: `0.01`

`0.01` can work with Adam, but it is relatively aggressive for vanilla
REINFORCE because the return estimates are noisy. It may produce fast initial
progress followed by oscillations. A better starting search is:

```python
[1e-4, 3e-4, 1e-3, 3e-3, 1e-2]
```

For a linear policy, `1e-3` or `3e-3` is usually a more conservative first
choice. The final value should be selected from repeated runs, not from one
training curve.

### Discount factor: `0.99`

`0.99` is a good choice for CartPole. Since future survival rewards matter,
using a very small value such as `0.5` would make the agent too short-sighted.
Possible comparison values are `0.95`, `0.99`, and `0.995`, but `0.99` should
remain the baseline.

### Number of episodes: `1000`

This is a reasonable minimum for a simple linear REINFORCE policy, but it may
not be enough for stable learning across seeds. Use 2000 to 5000 episodes when
comparing parameters, or stop early when the moving-average score reaches a
chosen threshold.

### Evaluation frequency and size

Evaluating every 100 episodes is fine for a quick experiment, but five
evaluation episodes are too few to make a reliable claim. Use at least 20
episodes for a report, and evaluate with `train=False` so no gradients or
updates are performed.

### Scheduler

The current `StepLR(step_size=100, gamma=0.9)` reduces the learning rate every
100 episodes. It is a defensible baseline, but the schedule is arbitrary and
is coupled to the total number of episodes. First compare a constant learning
rate against the scheduler. If the scheduler is retained, log the learning
rate and compare the same schedule across all candidate configurations.

### Rendering

Use `render_mode='none'` while searching parameters. Rendering and video
recording make experiments slower and do not improve learning. Use
`render_mode='final'` only after choosing the parameters, to produce one final
demonstration.

## Recommended baseline

For a clean baseline experiment, use:

```python
policy_name = 'linear'
env_name = 'CartPole-v1'
learning_rate = 0.003
discount_factor = 0.99
num_episodes = 2000
eval_freq = 100
render_mode = 'none'
```

Then repeat the experiment with at least five different seeds. If the score is
unstable, normalize returns or add a baseline before increasing model size.

## Recommended conclusion

The selected parameters are plausible, but they should not be presented as
optimal without repeated-seed evaluation. The strongest immediate changes are
to use a separate evaluation environment, avoid recording video during
training, fix the logging path for non-linear policies, add reproducibility,
and compare `0.001`, `0.003`, and `0.01` for the learning rate. Keep
`gamma=0.99` as the reference value.