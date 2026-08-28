# Insert your same_sign() function here.
def same_sign(x: int, y: int) -> bool:
    """
    Determine whether two integers have the same sign.
    Args:
        x: First integer.
        y: Second integer.
    Returns:
        True if x and y share the same sign (including both zero), False otherwise.
    """
    if ((x>=0) and (y>=0))or ((x<=0) and (y<=0)):
        return True
    else:
        return False
