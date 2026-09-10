import math
import random # this should be helpful!

# Write your sum_dice() function here along with any subroutines that you need.
def sum_dice(num_dice : int) -> int:
    """
    Simulate the roll of num_dice dice.

    Returns:
    int: The sum of num_dice pseudorandom integers between 1 and 6 inclusively.
    """
    return random.randint(1,6)+random.randint(1,6)
