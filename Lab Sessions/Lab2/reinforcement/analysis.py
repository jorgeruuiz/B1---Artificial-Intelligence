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
    answerDiscount = 0.2 # The model gives much more value to the immediate cells, as the forward rewards lose 80% of its value with each step. This way, it prefers to stay on the first end besides having a more valuable one 2 steps aside.  
    answerNoise = 0.001 # Having a small noise allows the model to go through a more risky path, having a fewer probability of stepping into the cliff with an error. 
    answerLivingReward = -0.2 # Having a negative living reward makes the model try the shortest paths in order to achieve the objective. This is due to the decrease of it's reward with each step, which promotes arriveng earlier. 
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

# 2. Prefer the close exit (+1), but avoiding the cliff (-10)
def question3b():
    answerDiscount = 0.2
    answerNoise = 0.1 # Having higher noise makes it less probable to achieve crossing the cliff. 
    answerLivingReward = 0.1 # The positive living reward makes choosing a longer path a better idea, as it'll be rewarded as long as it keeps alive. 
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

# 3. Prefer the distant exit (+10), risking the cliff (-10)
def question3c():
    answerDiscount = 0.95 # With a higher discount, we give more importance to the cells which are further, so in this case, it'll try to arrive to the most rewarding ending besides it being further. 
    answerNoise = 0.001 # Allows the model to cross the cliff with a tiny probability of falling. 
    answerLivingReward = -0.2 # Encourages to take the shortest path (cliff), as the model is penaliced for each step it takes. 
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

# 4. Prefer the distant exit (+10), avoiding the cliff (-10)
def question3d():
    answerDiscount = 0.95           # High discount factor to make the agent "ambitious" and value more future rewards
    answerNoise = 0.1               # Low noise to make the agent more confident to cross the bridge
    answerLivingReward = 0.2        # Slightly positive living reward to encourage the agent to continue moving
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

# 5. Avoid both exits and the cliff (so an episode should never terminate)
def question3e():
    answerDiscount = 0.01           # Very low discount factor so the agent values inmediate rewards versus future ones
    answerNoise = 0.2               # Standard value for noise
    answerLivingReward = -0.2       # Negative living reward to make the agent prefer to stay alive and avoid exits
                                    # and the cliff (better to keep moving and getting "free" rewards than to take risk)
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
