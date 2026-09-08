 

# Insert your starting_indices() function here.
def starting_indices(pattern: str, text: str) -> list:
    """
    starting_indices returns the list containing all the starting positions of 
    pattern in text.

    Parameters:
    - pattern (str): A given substring.
    - text (str): A given superstring.

    Returns:
    - list: A list containing the starting positions of pattern in text (indices).
    """

    positions = []
    n = len(text)
    k = len(pattern)
    for i in range(0,n-k+1):
        if text[i: i + k] == pattern:
            positions.append(i)
    return positions
