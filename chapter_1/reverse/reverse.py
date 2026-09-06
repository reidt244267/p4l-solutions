# Write your reverse() function here.
def reverse(s: str) -> str:
    """
    reverse returns the given string backwards.

    Parameters:
    - s (str): The given string to reverse.

    Returns:
    - str: The reverse of s.
    """
    lst=''
    for char in s:
        lst=char+lst


    return lst
