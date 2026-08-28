# Insert your factorial() function here.
def factorial(n: int) -> int:
    """
    Compute n! (factorial) using a while loop.
    Args:
        n: A non-negative integer.
    Returns:
        The factorial of n.
    """

    fact=1
    for i in range(n):
        fact=fact*(i+1)
    return fact
