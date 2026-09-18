# Write your count_num_digits() function here along with any subroutines that you need.
def count_num_digits(x: int) -> int:
    """
    Count the number of digits in a positive integer x.

    Parameters:
    - x (int): a positive integer

    Returns:
    int: the number of digits in x
    """
    if x>=0:
        return len(str(x))
    elif x<0:
        return len(str(x))-1

