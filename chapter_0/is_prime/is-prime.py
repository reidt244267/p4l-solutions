import math
# Insert your is_prime() function here, along with any subroutines that you need.
def is_prime(k: int) -> bool:
    """
    Determine whether an integer is prime.
    Args:
        p: Integer to test (may be negative or zero).
    Returns:
        True if p is prime, False otherwise.
    """

    if k<0:
        raise ValueError("Error: k must be nonnegative")

    if k<2:
        return False

    #try every number between 2 and k-1
    #if it's a disvior, return False
    #can stop range at sqrt(k)
    for i in range (2,math.isqrt(k)+1):
        if k%i==0:
            return False

    return True
