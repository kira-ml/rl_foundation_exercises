"""
03_type_annotations_rewards.py

This module demonstrates the use of Python type annotations and clean function design 
in the context of reinforcement learning (RL), focusing on reward calculation logic.

The purpose of this script is to show how to define and document a simple reward function
that assigns scalar rewards based on the current environment state and agent action.

While the example is simplified, the structure models how reward functions are typically 
used in RL pipelines: as part of the environment’s feedback loop to guide agent learning.

This script is designed for pedagogical clarity and aligns with best practices in 
production-grade ML engineering — emphasizing type safety, modularity, and explainability.
"""

from typing import Tuple


def compute_reward(state: Tuple[str, str], action: str) -> float:
    """
    Computes a simple scalar reward based on the environment state and the action taken.

    This reward function assumes that the environment's state is represented as a tuple 
    of two strings. The second element of the state is used as a flag to determine if 
    the environment is in a terminal state (i.e., the episode is done).

    The logic is as follows:
    - If the agent chooses to "move" and the environment is still active, it receives +1.0.
    - If the agent chooses to "stay" while the environment is still active, it receives -1.0.
    - Any action in a terminal state results in a neutral reward (0.0).

    This mirrors a common pattern in RL reward design: incentivizing exploration or 
    progression in non-terminal states, and discouraging stagnation.

    Args:
        state (Tuple[str, str]): A tuple representing the environment's current state. 
            The second element should indicate whether the environment is "done".
        action (str): The action taken by the agent. Expected values are "move" or "stay".

    Returns:
        float: The computed reward value, ranging from -1.0 to +1.0.

    Example:
        >>> compute_reward(("x1", "running"), "move")
        1.0
        >>> compute_reward(("x1", "done"), "stay")
        0.0
    """
    # We assume the second element of the state tuple signals whether the episode is done.
    is_terminal = state[-1] == "done"

    # Positive reward for taking action in a live environment
    if action == "move" and not is_terminal:
        return 1.0

    # Negative reward for inaction in a live environment (discourages passivity)
    elif action == "stay" and not is_terminal:
        return -1.0

    # Neutral reward for any action in a terminal state (no learning incentive)
    else:
        return 0.0


# Below are test cases to demonstrate the behavior of the reward function.
# These help validate the reward logic and are useful for quick debugging or 
# during unit test development in a more structured ML codebase.

print("Test 1:", compute_reward(("position_1", "running"), "move"))   # Expected: 1.0
print("Test 2:", compute_reward(("position_2", "running"), "stay"))   # Expected: -1.0
print("Test 3:", compute_reward(("position_3", "done"), "move"))      # Expected: 0.0
print("Test 4:", compute_reward(("position_4", "done"), "stay"))      # Expected: 0.0
