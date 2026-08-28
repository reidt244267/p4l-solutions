# Insert your another_factorial() function here.
def another_factorial(n: int) -> int:
    """
    Compute n! (factorial) using a for loop.
    Args:
        n: A non-negative integer.
    Returns:
        The factorial of n.
    Raises:
        ValueError: If n is negative.
    """
    if n<0:
        raise ValueError("n cannot be negative.")
    sum=1
    for i in range(n):
        sum=sum*(i+1)
    return sum
