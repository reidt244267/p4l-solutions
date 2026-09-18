# Write your has_repeat() function here along with any subroutines that you need
def has_repeat(a: list[int]) -> bool:
    """
    Check if a list has repeat elements.

    Parameters:
    - a: a list of integers

    Returns:
    bool: True if a has repeat elements, False otherwise
    """
    for key,value1 in enumerate(a):
        for i in range(key+1,len(a)):
            if value1==a[i]:
                return True

    return False
