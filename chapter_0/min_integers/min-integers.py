# Provided for you (from an earlier exercise):
def min_integer_array(lst: list[int]) -> int:
    """
    Return the minimum integer in a non-empty list.
    Args:
        lst: A non-empty list of integers.
    Returns:
        The smallest integer in lst.
    Raises:
        ValueError: If lst is empty.
    """
    if len(lst) == 0:
        raise ValueError("Error: Empty list given as input.")

    m = lst[0]
    # iterate over the list, updating m if a smaller value is found
    for val in lst:
        if val < m:
            m = val
    return m


# Insert your min_integers() function here, along with any subroutines that you need.
def min_integers(*numbers: int) -> int:
    """
    Return the minimum integer among a variable number of inputs.
    Args:
        numbers: One or more integers.
    Returns:
        The smallest integer in numbers.
    Raises:
        ValueError: If no numbers are provided.
    """
    if len(numbers)==0:
        raise ValueError("Error: no numbers are provided")
    
    return min(numbers)
