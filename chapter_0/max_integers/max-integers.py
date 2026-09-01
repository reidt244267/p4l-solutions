# Provided for you (from an earlier exercise):
def max_integer_array(lst: list[int]) -> int:
    """
    Return the maximum integer in a non-empty list.
    Args:
        lst: A non-empty list of integers.
    Returns:
        The largest integer in lst.
    """
    if len(lst) == 0:
        raise ValueError("Error: Empty list given as input.")
    m = float('-inf')  # default value as negative infinity
    # iterate over list, updating m if we find a larger value
    for val in lst:
        if val > m:
            m = val
    return m


# Insert your max_integers() function here, along with any subroutines that you need.
def max_integers(*numbers: int) -> int:
    """
    Return the maximum integer among a variable number of inputs.
    Args:
        numbers: One or more integers.
    Returns:
        The largest integer in numbers.
    Raises:
        ValueError: If no numbers are provided.
    """
    return max_integer_array(list(numbers))
