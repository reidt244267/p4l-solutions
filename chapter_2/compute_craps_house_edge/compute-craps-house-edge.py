import random # this should be helpful!

# Write your compute_craps_house_edge() function here along with any subroutines that you need.
def compute_craps_house_edge(num_trials: int) -> float:
    """
    Estimate the house edge of craps based on simulations.

    This function simulates the specified number of craps games and calculates the
    average money won or lost over those games to estimate the house edge.

    Parameters:
    - num_trials (int): The number of simulated games to play.

    Returns:
    float: The estimated house edge, representing the average money won or lost per game.
    """

    count = 0
    for i in range(num_trials):
        outcome = play_craps_once()
        if outcome == True:
            count = count + 1
        else:
            count = count - 1
    return count/num_trials


# Provided for you (from an earlier exercise):
def sum_two_dice() -> int:
    """
    Return the sum of rolling two dice.
    """
    return random.randint(1,6) + random.randint(1,6)


# Write your play_craps_once() function here along with any subroutines that you need.
def play_craps_once() -> bool:
    """
    Simulate a single game of craps and determine the outcome.

    This function simulates a single game of craps by rolling two dice.
    The outcome is determined based on the rules of craps:

    - If the first roll is 7 or 11, the player wins.
    - If the first roll is 2, 3, or 12, the player loses.
    - Otherwise, the player continues rolling until they either roll a 7 (losing)
      or match their original roll (winning).

    Returns:
    bool: True if the player wins, False if the player loses.
    """
    firstRoll = sum_two_dice()
    if (firstRoll == 2) or (firstRoll == 3) or (firstRoll == 12):
        return False
    elif (firstRoll == 7) or (firstRoll == 11):
        return True
    else:
        while True:
            newRoll = sum_two_dice()
            if newRoll == firstRoll:
               return True
            elif newRoll == 7:
                return False
