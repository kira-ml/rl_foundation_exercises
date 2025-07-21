"""
05_looping_agent_states.py

In this implementation, I demonstrate the use of nested loops to simulate multiple episodes of agent-environment interaction—a foundational pattern in reinforcement learning (RL) research and engineering. This script is designed to teach the structure and rationale behind episode-based simulation, which is central to RL pipelines for both training and evaluation.

The code is documented to highlight best practices in loop design, state tracking, and output reporting, as expected in high-quality ML codebases.
"""

def run_simulation():
    """
    Simulate a fixed number of RL episodes, each with a fixed number of steps.

    In this function, I use a nested loop structure:
        - The outer loop iterates over episodes (analogous to independent trials or episodes in RL).
        - The inner loop iterates over steps within each episode (analogous to timesteps or agent-environment interactions).
    
    This pattern is ubiquitous in RL research and production systems, as it mirrors the episodic nature of most RL tasks and enables clear separation of per-episode and per-step logic.
    
    Returns
    -------
    None
        This function prints progress and summary information to the console.
    """
    num_episodes = 3
    steps_per_episodes = 5
    total_steps_taken = 0  # Aggregate step counter across all episodes

    for episodes_index in range(1, num_episodes + 1):
        print(f"Starting Episode {episodes_index}")

        step_count = 1  # Reset step counter for each episode

        while step_count <= steps_per_episodes:
            print(f"Step {step_count}")
            total_steps_taken += 1  # Track total steps for reporting
            step_count += 1

    # Summary output is a best practice for experiment tracking
    print(f"\nSimulation complete. Total steps taken: {total_steps_taken}")

if __name__ == "__main__":
    # Entry point for standalone script execution.
    run_simulation()