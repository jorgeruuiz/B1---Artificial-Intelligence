"""Search epsilon/learning-rate combinations for noiseless BridgeGrid."""

import csv
import json
import random
from pathlib import Path

import gridworld
import qlearningAgents


DISCOUNT = 0.9
EPISODES = 500
EVALUATION_EPISODES = 100
TRIALS = 100
EPSILONS = (0.0, 0.05, 0.1, 0.2, 0.3, 0.5, 0.75, 1.0)
LEARNING_RATES = (0.1, 0.25, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0)
OUTPUT_DIRECTORY = Path(__file__).resolve().parent
OUTPUT_JSON = OUTPUT_DIRECTORY / "bridgegrid_parameter_search.json"
OUTPUT_CSV = OUTPUT_DIRECTORY / "bridgegrid_parameter_search.csv"
BRIDGE_SUCCESS_THRESHOLD = 5.0


def run_episode(agent, environment, discount):
    """Run one silent episode and return its discounted reward."""
    return gridworld.runEpisode(
        agent,
        environment,
        discount,
        agent.getAction,
        lambda state: None,
        lambda message: None,
        lambda: None,
        0,
    )


def train_and_evaluate(epsilon, learning_rate, seed):
    random.seed(seed)
    mdp = gridworld.getBridgeGrid()
    mdp.setNoise(0.0)
    environment = gridworld.GridworldEnvironment(mdp)
    agent = qlearningAgents.QLearningAgent(
        gamma=DISCOUNT,
        alpha=learning_rate,
        epsilon=epsilon,
        actionFn=mdp.getPossibleActions,
    )

    for _ in range(EPISODES):
        run_episode(agent, environment, DISCOUNT)

    # Evaluate the learned policy without changing it through exploration.
    agent.epsilon = 0.0
    agent.alpha = 0.0
    successful_episodes = sum(
        run_episode(agent, environment, DISCOUNT) >= BRIDGE_SUCCESS_THRESHOLD
        for _ in range(EVALUATION_EPISODES)
    )
    return successful_episodes / EVALUATION_EPISODES


def main():
    results = []
    for epsilon in EPSILONS:
        for learning_rate in LEARNING_RATES:
            scores = [
                train_and_evaluate(epsilon, learning_rate, seed)
                for seed in range(TRIALS)
            ]
            results.append({
                "epsilon": epsilon,
                "learning_rate": learning_rate,
                "mean_success_rate": sum(scores) / len(scores),
                "best_success_rate": max(scores),
                "trials_above_99_percent": sum(score > 0.99 for score in scores),
            })

    results.sort(
        key=lambda result: (
            result["mean_success_rate"],
            result["best_success_rate"],
        ),
        reverse=True,
    )
    top_results = results[:10]

    OUTPUT_JSON.write_text(json.dumps(top_results, indent=2) + "\n")
    with OUTPUT_CSV.open("w", newline="") as output_file:
        writer = csv.DictWriter(output_file, fieldnames=top_results[0].keys())
        writer.writeheader()
        writer.writerows(top_results)

    print("Top 10 parameter combinations:")
    for rank, result in enumerate(top_results, start=1):
        print(
            f"{rank:2}. epsilon={result['epsilon']:<4} "
            f"learning_rate={result['learning_rate']:<4} "
            f"mean_success={result['mean_success_rate']:.3f} "
            f"best_success={result['best_success_rate']:.3f}"
        )
    print(f"Saved results to {OUTPUT_JSON} and {OUTPUT_CSV}")


if __name__ == "__main__":
    main()