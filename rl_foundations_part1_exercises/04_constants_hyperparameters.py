"""
04_constants_hyperparameters.py

In this implementation, I demonstrate the use of module-level constants to define key hyperparameters for a Q-learning update rule. This script is designed to teach the importance of clear, centralized hyperparameter management and the mechanics of the Q-value update equation, which is foundational in reinforcement learning (RL).

The code structure and documentation follow best practices for clarity, maintainability, and pedagogical value, as expected in high-quality ML research and production codebases.
"""

# --- Hyperparameters ---
# These constants are defined at the module level for clarity and ease of tuning.
LEARNING_RATE = 0.1           # Step size for Q-value updates (alpha)
DISCOUNT_FACTOR = 0.95        # Discount factor for future rewards (gamma)
MAX_EPISODES = 500            # Maximum number of training episodes (not used directly here)


def update_q_value(current_q: float, reward: float, max_future_q: float) -> float:
    """
    Compute the updated Q-value using the Q-learning update rule.

    In this function, I apply the canonical Q-learning update equation:
        Q(s, a) <- Q(s, a) + alpha * (reward + gamma * max(Q(s', a')) - Q(s, a))
    where:
        - current_q: The current Q-value estimate for state-action pair (s, a)
        - reward: The immediate reward received after taking action a in state s
        - max_future_q: The maximum Q-value estimate for the next state s'
        - LEARNING_RATE (alpha): Controls the step size of the update
        - DISCOUNT_FACTOR (gamma): Weighs the importance of future rewards

    This function is intentionally stateless and functional, which is a best practice for testability and composability in ML pipelines.

    Parameters
    ----------
    current_q : float
        The current Q-value for the (state, action) pair.
    reward : float
        The immediate reward received after taking the action.
    max_future_q : float
        The maximum Q-value for the next state (used for bootstrapping).

    Returns
    -------
    float
        The updated Q-value after applying the Q-learning update.
    """
    # Q-learning update: blend old value with new estimate
    updated_q = current_q + LEARNING_RATE * (reward + DISCOUNT_FACTOR * max_future_q - current_q)
    return updated_q


# --- Example usage: single Q-value update ---
# In a full RL pipeline, these values would be dynamically computed during agent-environment interaction.
initial_q_value = 0.5
received_reward = 1.0
estimated_max_future_q = 0.8

# Perform the Q-value update using the defined function and hyperparameters.
new_q_value = update_q_value(initial_q_value, received_reward, estimated_max_future_q)

# Output the result for demonstration purposes.
print("Updated Q-value:", new_q_value)