import random # this should be helpful!

def estimate_first_roll_win(num_trials: int) -> float:
    """
    Simulate num_trials games of craps and return the probability that
    the player wins immediately on the first roll (sum of dice = 7 or 11).

    Parameters:
        num_trials (int): The number of games to simulate.

    Returns:
        float: An estimated probability between 0 and 1 that the player 
               wins on the first roll.
    """
    count_win=0
    for i in range(num_trials):
        roll_total=dice_roll()+dice_roll()
        if (roll_total==7) or (roll_total==11):
            count_win=count_win+1

    return count_win/num_trials

def dice_roll():
    return random.randint(1,6)
