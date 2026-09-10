import math
# Provided for you (from an earlier exercise):
def max_integer_array(lst: list[int]) -> int:
    """
    Return the maximum integer in a non-empty list.
    Args:
        lst: A non-empty list of integers.
    Returns:
        The largest integer in lst.
    """
    if len(lst) == 0:
        raise ValueError("Error: Empty list given as input.")
    m = float('-inf')  # default value as negative infinity
    # iterate over list, updating m if we find a larger value
    for val in lst:
        if val > m:
            m = val
    return m


# Provided for you (from an earlier exercise):
def divides_all(a: list[int], d: int) -> bool:
    """
    Determine whether d divides every element of a.
    Args:
        a: A list of integers.
        d: The candidate divisor.
    Returns:
        True if every element x in a satisfies x % d == 0.
        False immediately if d == 0, since zero is not a divisor of any number.
    """
    if d == 0:
        return False
    for val in a:
        if val % d != 0:
            return False
    return True


# Insert your gcd_array() function here, along with any subroutines that you need.
def gcd_array(a: list[int]) -> int:
    """
    Return the greatest common divisor (GCD) of all integers in the list.
    Args:
        a: A non-empty list of integers (values may be negative or zero).
    Returns:
        The non-negative GCD of all numbers in `a`. 
    """
    max_int=max_integer_array(a)
    max_GCD=1
    for i in range(1,max_int+1):
        if divides_all(a,i):
            max_GCD=i



    return max_GCD
