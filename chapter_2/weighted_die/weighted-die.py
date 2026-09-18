import random # this should be helpful!

# Write your weighted_die() function here along with any subroutines that you need.
def weighted_die() -> int:
    """
    Simulate a weighted die that has a 10% chance of rolling a 1, a 10% chance of rolling a 2, a 50% chance of rolling a
    3, a 10% chance of rolling a 4, a 10% chance of rolling a 5, and a 10% chance of rolling a 6.

    Returns:
    int: a random integer between 1 and 6, inclusive, with the above probabilities
    """
    die=random.randint(1,10)
    if die in (1,2,3,4,5):
        return 3
    elif die==6:
        return 1
    elif die==7:
        return 2
    elif die==8:
        return 4
    elif die==9:
        return 5
    elif die==10:
        return 6
