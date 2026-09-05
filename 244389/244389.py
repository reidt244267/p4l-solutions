import sys

# Please do not remove package declarations because these are used by the autograder.
# You may declare additional packages above if needed.


# Insert your isAmicable(a, b) function here, along with any subroutines that you need.
# The function should return a boolean: True if (a, b) are amicable, otherwise False.
def isAmicable(a: int, b: int) -> bool:
    if (sum_proper_divisors(a)==b) and (a==sum_proper_divisors(b)):
        return True
    return False


def sum_proper_divisors(n: int) -> int:
    """
    Return the sum of all proper (positive) divisors of n, i.e., divisors strictly less than n.
    Args:
        n: Integer input.
    Returns:
        The sum of all positive divisors of n that are < n.
        Returns 0 for n <= 1.
    """

    d=0
    for i in range (1,n):
        if (n%(i)==0):
            d=d+i

    return d
