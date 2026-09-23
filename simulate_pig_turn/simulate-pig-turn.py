import random # this should be helpful!


# roll_die() is provided for you. You do not need to write it, and you should not change it.
def roll_die() -> int:
    """
    Simulates the roll of a die.
    Returns:
    - int: A pseudorandom integer between 1 and 6, inclusively.
    """
    return random.randrange(1, 7)


# Write your estimate_turn_score() function here along with any subroutines that you need.
def estimate_turn_score(hold_at: int, num_trials: int) -> float:
    """
    Estimate the average score of a single turn of the dice game Pig.

    A turn works as follows. The player starts with a running total of 0 and
    rolls one die at a time.

    - If the die shows a 1, the turn ends immediately and the turn scores 0.
    - Otherwise, the die is added to the running total.
    - As soon as the running total is greater than or equal to hold_at, the
      player stops rolling, and the turn scores the running total.

    Parameters:
    - hold_at (int): The running total at which the player stops rolling.
    - num_trials (int): The number of turns to simulate.

    Returns:
    float: The average turn score over num_trials simulated turns.
    """
    score=0
    for i in range(num_trials):
        score=score+one_round(hold_at)

    return score/num_trials

def one_round(hold_at:int)->int:
    total=0
    while(total<hold_at):
        roll=roll_die()
        if roll==1:
            return 0
        else:
            total=total+roll
    return total
