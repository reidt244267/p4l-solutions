import random # this should be helpful!

def simulate_state_once(poll: float, margin_of_error: float) -> bool:
    """
    Decide the winner of one state by adding random noise to the polling result.

    Parameters:
        poll (float): Candidate 1’s polling share in the state, between 0 and 1.
        margin_of_error (float): Non-negative margin of error.

    Returns:
        bool: True if candidate 1 wins the state (adjusted poll ≥ 0.5),
              otherwise False.
    """
    x=random.gauss(0,1)
    #x has a 95% chance of being between -2 and 2

    x/=2.0
    #x now has a 95% chance of being between -1 and 1

    x*=margin_of_error
    if (x+poll)>=0.5:
        return True
    else:
        return False


