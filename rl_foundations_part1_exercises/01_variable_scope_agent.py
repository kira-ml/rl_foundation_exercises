"""
RL Agent State Simulation

This script simulates the state transitions of a simple agent in a reinforcement learning (RL)-inspired environment.
At each step, the agent selects an action from a fixed set (`explore`, `exploit`, or `rest`), and its internal state
is updated based on the chosen action.

In this implementation, I demonstrate how variable scope, randomness, and action logic interact in agent simulations.
This foundational pattern — step-wise simulation using discrete action policies — serves as a precursor to more
complex RL systems involving Q-learning, policy gradients, or environment modeling.

This example is particularly useful for beginners who are learning how agent-environment interactions can be
modeled procedurally with basic control flow and state variables.
"""

import random
from typing import List

# Global variable representing the agent's current internal state.
agent_state: int = 0

# Action space available to the agent at each time step.
available_actions: List[str] = ["explore", "exploit", "rest"]

# Number of steps (time horizon) over which to simulate agent behavior.
MAX_STEPS: int = 5


def simulate_action() -> None:
    """
    Simulates a single agent action and updates the global `agent_state`.

    The action is selected randomly from a predefined list. Each action results in
    a deterministic state transition:
    
    - 'explore' increases state by 2 (more effort, greater payoff).
    - 'exploit' increases state by 1 (safer, consistent strategy).
    - 'rest' decreases state by 1, but never below 0 (recovering or idling).

    This structure mimics simplified decision trade-offs common in reinforcement learning.
    """
    global agent_state

    action = random.choice(available_actions)
    print(f"Selected action: {action}")

    # Apply deterministic transition based on the selected action
    if action == "explore":
        agent_state += 2
    elif action == "exploit":
        agent_state += 1
    else:  # 'rest'
        # Ensure the agent state does not go negative
        agent_state = max(0, agent_state - 1)


def run_simulation() -> None:
    """
    Runs a step-wise simulation of the agent's behavior over a fixed number of steps.

    At each step, the current state is printed, an action is simulated, and the
    state is updated accordingly. This is a stand-in for an episode in RL.
    """
    print("Starting simulation...")

    # Simulate the agent's behavior over the defined time horizon
    for step in range(1, MAX_STEPS + 1):
        print(f"\nStep {step}: Current state = {agent_state}")
        simulate_action()

    print("\nSimulation complete!")


if __name__ == "__main__":
    # Entry point for standalone script execution.
    run_simulation()
    print(f"Final agent state: {agent_state}")
