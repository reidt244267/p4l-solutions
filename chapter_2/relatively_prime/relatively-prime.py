def euclid_gcd(a: int, b: int) -> int:
    """
    Compute the greatest common divisor of two integers using Euclid's algorithm.

    Args:
        a: A positive integer.
        b: A positive integer.
    Returns:
        The greatest common divisor of a and b.
    """
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

# Write your improved relatively_prime() function here. Use euclid_gcd!
def relatively_prime(a: int, b: int) -> bool:
    """
    Check if a and b are relatively prime.

    Parameters:
    - a (int): an integer
    - b (int): an integer

    Returns:
    bool: True if a and b are relatively prime, False otherwise
    """
    if euclid_gcd(a,b)==1:
        return True
    return False
