# This function is already written for you, and it is WRONG.
# Find the input it fails on, then repair it. Change as little as you can.
def count_digits(n: int) -> int:
    """
    Count the digits used to write a non-negative integer.

    Parameters:
        n (int) - A non-negative integer.

    Returns:
        count (int) - The number of digits used to write n.
                      count_digits(0) is 1, because 0 is written
                      with a single digit.
    """
    count = 0
    if n==0:
        return 1

    while n > 0:
        n = n // 10
        count += 1
    return count
