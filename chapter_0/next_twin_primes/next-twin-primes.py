# Provided for you (from an earlier exercise):
def is_prime(p: int) -> bool:
    """
    Determine whether an integer is prime.
    Args:
        p: Integer to test (may be negative or zero).
    Returns:
        True if p is prime, False otherwise.
    """
    if p == 1:
        return False  # base case: p is not prime

    # iterate over potential divisors up to the square root of p
    for k in range(2, int(p ** 0.5 + 1)):
        if p % k == 0:
            return False  # k is a divisor of p, so p is not prime

    # if no divisors are found, p is prime
    return True


# Insert your next_twin_primes() function here, along with any subroutines that you need.
def next_twin_primes(n: int) -> tuple[int, int]:
    """
    Return the smallest pair of twin primes (p, p+2) such that both p and p+2 are > n.
    Args:
        n: Integer threshold.
    Returns:
        A tuple (p, q) where q = p + 2 are twin primes and p > n.
    """
    keep_goin=True
    p=n
    while keep_goin==True:
        p=p+1
        if (is_prime(p))and(is_prime(p+2)):
            keep_goin=False

    return (p, p+2)
