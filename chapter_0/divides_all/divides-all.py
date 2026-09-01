# Insert your divides_all() function here, along with any subroutines that you need.
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
    if d==0:
        return False

    placeholder=True
    for item in a:
        if not (item%d==0):
            placeholder=False


    return placeholder
