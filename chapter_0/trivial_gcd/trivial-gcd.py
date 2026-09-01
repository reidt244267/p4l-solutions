def trivial_gcd(a: int, b: int) -> int:
    """
    Compute the greatest common divisor (GCD) of two integers using the "trivial" (brute-force) algorithm.
    Args:
        a: First integer.
        b: Second integer.
    Returns:
        The non-negative GCD of a and b. 
    """
    """
    Trivial GCD(a,b)
    d=1
    m=min(a,b)
    for every integer p between 1 and m
        if p is divisor of both a and b
            d=p
        return d
    """

    d=1
    m=min(a,b)
    for i in range (1,m+1):
        if (a%(i)==0) and (b%(i)==0):
            d=i

    return d

# Place your min_2() subroutine here.
