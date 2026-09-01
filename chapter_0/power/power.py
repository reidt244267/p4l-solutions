# Insert your power() function here, along with any subroutines that you need.
def power(a: int, b: int) -> int:
    """
    Compute a raised to the b-th power.
    Args:
        a: Base integer (can be negative, zero, or positive).
        b: Exponent integer (must be non-negative).
    Returns:
        The integer value of a^b. By convention, 0^0 returns 1.
    """
    return a ** b
