"""
Timestep Loop - Core RL Environment Interaction Pattern

This module demonstrates the fundamental timestep-based interaction pattern
that forms the backbone of all reinforcement learning algorithms.

The basic RL loop:
1. Observe current state
2. Select action based on policy
3. Execute action in environment
4. Receive reward and next state
5. Update knowledge/policy
6. Repeat until episode ends
"""

import numpy as np
from typing import Tuple, Any, Optional


class SimpleEnvironment:
    """
    A minimal environment for demonstrating RL concepts.
    
    This environment represents a simple 1D grid world where an agent
    can move left or right to reach a goal position.
    """
    
    def __init__(self, grid_size: int = 5, goal_position: int = 4):
        self.grid_size = grid_size
        self.goal_position = goal_position
        self.current_position = 0
        self.max_steps = 20
        self.step_count = 0
        
    def reset(self) -> int:
        """Reset environment to initial state."""
        self.current_position = 0
        self.step_count = 0
        return self.current_position
    
    def step(self, action: int) -> Tuple[int, float, bool, dict]:
        """
        Execute one timestep in the environment.
        
        Args:
            action: 0 = move left, 1 = move right
            
        Returns:
            Tuple of (next_state, reward, done, info)
        """
        self.step_count += 1
        
        # Execute action
        if action == 0 and self.current_position > 0:  # Move left
            self.current_position -= 1
        elif action == 1 and self.current_position < self.grid_size - 1:  # Move right
            self.current_position += 1
        
        # Calculate reward
        if self.current_position == self.goal_position:
            reward = 10.0  # Goal reached
            done = True
        elif self.step_count >= self.max_steps:
            reward = -1.0  # Time penalty
            done = True
        else:
            reward = -0.1  # Step penalty
            done = False
        
        info = {
            'step_count': self.step_count,
            'position': self.current_position,
            'goal_position': self.goal_position
        }
        
        return self.current_position, reward, done, info
    
    def render(self) -> str:
        """Visualize current environment state."""
        grid = ['-'] * self.grid_size
        grid[self.current_position] = 'A'  # Agent
        grid[self.goal_position] = 'G' if self.current_position != self.goal_position else 'X'  # Goal or Success
        return ' '.join(grid)


class RandomAgent:
    """A simple agent that selects actions randomly."""
    
    def __init__(self, action_space_size: int):
        self.action_space_size = action_space_size
    
    def select_action(self, state: int) -> int:
        """Select a random action."""
        return np.random.randint(0, self.action_space_size)


def run_timestep_loop(env: SimpleEnvironment, agent: RandomAgent, 
                     max_episodes: int = 5, verbose: bool = True) -> dict:
    """
    Run the basic RL timestep loop for multiple episodes.
    
    Args:
        env: The environment to interact with
        agent: The agent making decisions
        max_episodes: Number of episodes to run
        verbose: Whether to print detailed output
        
    Returns:
        Dictionary with episode statistics
    """
    episode_rewards = []
    episode_lengths = []
    
    for episode in range(max_episodes):
        # Reset environment for new episode
        state = env.reset()
        episode_reward = 0
        episode_length = 0
        
        if verbose:
            print(f"\n=== Episode {episode + 1} ===")
            print(f"Initial state: {env.render()}")
        
        # Run timestep loop until episode ends
        while True:
            # Agent selects action based on current state
            action = agent.select_action(state)
            
            # Environment processes action and returns consequences
            next_state, reward, done, info = env.step(action)
            
            # Accumulate episode statistics
            episode_reward += reward
            episode_length += 1
            
            if verbose:
                action_name = "LEFT" if action == 0 else "RIGHT"
                print(f"Step {episode_length}: Action={action_name}, "
                      f"Reward={reward:.1f}, State: {env.render()}")
            
            # Update state for next iteration
            state = next_state
            
            # Check if episode is complete
            if done:
                if verbose:
                    if next_state == env.goal_position:
                        print("🎉 Goal reached!")
                    else:
                        print("⏰ Episode ended (max steps reached)")
                    print(f"Episode reward: {episode_reward:.1f}")
                break
        
        episode_rewards.append(episode_reward)
        episode_lengths.append(episode_length)
    
    # Calculate and return statistics
    stats = {
        'episode_rewards': episode_rewards,
        'episode_lengths': episode_lengths,
        'mean_reward': np.mean(episode_rewards),
        'mean_length': np.mean(episode_lengths),
        'total_episodes': max_episodes
    }
    
    if verbose:
        print(f"\n=== Summary ===")
        print(f"Average reward per episode: {stats['mean_reward']:.2f}")
        print(f"Average episode length: {stats['mean_length']:.2f}")
    
    return stats


if __name__ == "__main__":
    print("Reinforcement Learning: Timestep Loop Demonstration")
    print("=" * 50)
    
    # Create environment and agent
    env = SimpleEnvironment(grid_size=5, goal_position=4)
    agent = RandomAgent(action_space_size=2)
    
    # Run the timestep loop
    stats = run_timestep_loop(env, agent, max_episodes=3, verbose=True)
    
    print("\nThis demonstrates the core RL interaction pattern:")
    print("1. Agent observes state")
    print("2. Agent selects action") 
    print("3. Environment returns reward and next state")
    print("4. Process repeats until episode ends")
