# Write your pattern_count() function here, along with any subroutines that you need.
def pattern_count(pattern: str, text: str) -> int:
    """
    pattern_count finds the number of occurences that a given substring occurs in
    a given text string. (Relies on starting_indices as a subroutine)

    Parameters:
    - pattern (str): The substring you search for in text.
    - text (str): The parent string you are using in your search.

    Returns:
    - int: The number of times that pattern occurs in text.
    """
    count = 0
    n = len(text)
    k = len(pattern)
    for i in range(0,n-k+1):
        if text[i: i + k] == pattern:
            count = count + 1
    return count
