# Insert your which_is_greater() function here.
def which_is_greater(x: int, y: int) -> int:
    """
    Compare two integers and indicate which is greater.
    Args:
        x: First integer.
        y: Second integer.
    Returns:
        0 if they're equal
        1 if x is greater than y
       -1 if x is less than y
    """
    if x>y:
        return 1
    elif x==y:
        return 0
    else:
        return -1
