# Provided for you (from an earlier exercise):
def sum_proper_divisors(n: int) -> int:
    """
    Return the sum of all proper (positive) divisors of n, i.e., divisors strictly less than n.
    Args:
        n: Integer input.
    Returns:
        The sum of all positive divisors of n that are < n.
        Returns 0 for n <= 1.
    """
    # sum all divisors of n
    divisors_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisors_sum += i
    return divisors_sum


# Insert your is_perfect() function here, along with any subroutines that you need.
def is_perfect(n: int) -> bool:
    """
    Determine whether an integer n is a perfect number.
    Args:
        n: Integer to test.
    Returns:
        True if n is perfect, False otherwise.
    """
    if n==sum_proper_divisors(n):
        return True
    else:
       return False
