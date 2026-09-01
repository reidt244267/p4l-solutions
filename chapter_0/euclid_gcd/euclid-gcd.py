# Insert your euclid_gcd() function here.
def euclid_gcd(a: int, b: int) -> int:
    """
    Compute the greatest common divisor (GCD) of two integers using Euclid's algorithm.
    Args:
        a: First integer.
        b: Second integer.
    Returns:
        The non-negative GCD of a and b.

    Euclid's insight: assume WLOG a<b, then GCD(a,b)=GCD(a,a-d)
    GCD(273,378)    =GCD(273,105)
                    =GCD(168,105)
                    =GCD(63,105)
                    =GCD(63,42)
                    =GCD(21,42)
                    =GCD(21,21)
                    21
    
    EuclidGCD(a,b):
        while a!=b
            if a>b
                a=a-b
            else
                b=b-a
            return a (or b)
        """
    while a!=b:
        if a>b:
            a=a-b
        else:
            b=b-a
    return a

    """
    recursive:
    if a==b:
        return b
    else if a>b:
        euclid_gcd(a-b,b)
    else:
        euclid_gcd(a,b-a)
    """


