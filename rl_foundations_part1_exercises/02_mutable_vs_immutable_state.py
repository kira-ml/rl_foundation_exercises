"""
mutable_vs_immutable_state.py

This demonstration explores the behavioral differences between mutable and immutable data types
in Python functions—specifically in the context of modeling agent state transitions in reinforcement learning (RL).
Understanding how data types propagate through function calls is critical when designing stateful agents or
environment interactions, as subtle issues with mutability can introduce bugs or unintended side effects.

This script provides two function implementations:
    - One that attempts to modify an immutable tuple.
    - One that modifies a mutable list.

Both serve as instructive, minimal examples for beginners to grasp Python’s function-scoping behavior
and data mutability model, which are foundational in ML system design.
"""

def update_state_immutable(state):
    """
    Attempt to update a state represented as an immutable tuple.

    This function takes a tuple `(x, y)` as input and computes a new tuple 
    with each coordinate incremented by 1. However, this reassignment only affects
    the local variable inside the function scope—it does not mutate the original tuple
    passed to the function.

    Parameters
    ----------
    state : tuple of int
        A 2-element tuple representing a 2D grid agent state.

    Returns
    -------
    None
        This function prints the updated state but does not return it or affect the input.
    """
    # Reassignment to a new tuple — the original input is untouched outside this scope.
    state = (state[0] + 1, state[1] + 1)
    print("[Inside function] Updated state:", state)


# Example usage with an immutable tuple.
agent_state = (0, 0)

print("[Before function] Original state:", agent_state)
update_state_immutable(agent_state)
print("[After function] State remains unchanged:", agent_state)


def update_state_mutable(state):
    """
    Mutate a state represented as a mutable list in-place.

    This function directly modifies the elements of the list passed in,
    incrementing both coordinates by 1. Since lists are mutable and passed
    by reference in Python, the caller will observe the change.

    Parameters
    ----------
    state : list of int
        A 2-element list representing a 2D grid agent state.

    Returns
    -------
    None
        The mutation is applied in-place and observable by the caller.
    """
    # In-place mutation — the caller's copy of `state` is changed.
    state[0] += 1
    state[1] += 1
    print("[Inside function] Updated state:", state)


# Example usage with a mutable list.
agent_state = [0, 0]

print("[Before function] Original state:", agent_state)
update_state_mutable(agent_state)
print("[After function] State was mutated:", agent_state)
