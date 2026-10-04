# analysis.py
# -----------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


######################
# ANALYSIS QUESTIONS #
######################

# Set the given parameters to obtain the specified policies through
# value iteration.

def question2():
    answerDiscount = 0.9
    answerNoise = 0.01
    return answerDiscount, answerNoise

# 1. Prefer the close exit (+1), risking the cliff (-10)
def question3a():
    answerDiscount = 0.2       # Strong discounting favours the close +1 exit over the distant +10 exit.
    answerNoise = 0.001        # Almost no unintended movement makes the short route near the cliff preferable.
    answerLivingReward = -0.2  # A penalty for each step encourages reaching the exit sooner.
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

# 2. Prefer the close exit (+1), but avoiding the cliff (-10)
def question3b():
    answerDiscount = 0.2       # Strong discounting still favours the close exit.
    answerNoise = 0.1          # More unintended movement increases the risk of falling near the cliff.
    answerLivingReward = 0.1   # Rewards for non-exit steps make the longer safe route less costly.
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

# 3. Prefer the distant exit (+10), risking the cliff (-10)
def question3c():
    answerDiscount = 0.95      # Weak discounting preserves the value of the distant +10 exit.
    answerNoise = 0.001        # Almost no unintended movement makes the short route near the cliff preferable.
    answerLivingReward = -0.2  # A penalty for each step favours the shorter route to that exit.
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

# 4. Prefer the distant exit (+10), avoiding the cliff (-10)
def question3d():
    answerDiscount = 0.95      # Weak discounting favours the distant +10 exit.
    answerNoise = 0.1          # Risk of unintended movement towards the cliff favours the longer safe route.
    answerLivingReward = 0.2   # Rewards for non-exit steps support taking the longer route.
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

# 5. Avoid both exits and the cliff (so an episode should never terminate)
def question3e():
    answerDiscount = 0.01      # Very strong discounting makes distant exit rewards almost irrelevant.
    answerNoise = 0.2          # Transition risk discourages approaching the cliff.
    answerLivingReward = -0.2  # Penalizes each step; it does not itself encourage staying alive.
    # Together, these values produce a cycle between (0, 1) and (0, 2)
    # on the required noiseless path. With actual noise, survival is not guaranteed.
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question6():
    answerEpsilon = 0.1
    answerLearningRate = 0.5
    # return answerEpsilon, answerLearningRate
    return 'NOT POSSIBLE'
    # If not possible, return 'NOT POSSIBLE'

# Just in case we have to strictly follow the instructions of RL lap document. 
def question8():
    answerEpsilon = None
    answerLearningRate = None
    # return answerEpsilon, answerLearningRate
    return 'NOT POSSIBLE'
    # If not possible, return 'NOT POSSIBLE'

if __name__ == '__main__':
    print('Answers to analysis questions:')
    import analysis
    for q in [q for q in dir(analysis) if q.startswith('question')]:
        response = getattr(analysis, q)()
        print('  Question %s:\t%s' % (q, str(response)))
