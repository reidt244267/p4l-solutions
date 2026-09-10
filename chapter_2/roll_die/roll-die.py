import random # this should be helpful!

# Write your roll_die() function here along with any subroutines that you need.
def roll_die() -> int:
    """
    Simulate the roll of a die.

    Returns:
    int: A pseudorandom integer between 1 and 6 inclusively.
    """
    return random.randint(1, 6)
