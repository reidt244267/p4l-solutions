import sys

# Please do not remove imports because these are used by the autograder.
# If you need additional imports, then you may declare them above.


def find_flanking_regions(text: str, pattern1: str, pattern2: str) -> list[str]:
    """
    Find all substrings of `text` that are flanked by `pattern1` on the left
    and `pattern2` on the right.

    Parameters
    ----------
    text : str
        The input string to search.
    pattern1 : str
        The left flanking pattern.
    pattern2 : str
        The right flanking pattern.

    Returns
    -------
    list[str]
        A list of substrings between pattern1 and pattern2. Can be empty if none found.
    """
    lst=[]
    for i in range(0, len(text)-len(pattern1)-len(pattern2)+1):
        p1segment=text[i:i+len(pattern1)]
        if p1segment==pattern1:
            for p in range(i+len(pattern1),len(text)-len(pattern2)+1):
                p2segment=text[p:p+len(pattern2)]
                if p2segment==pattern2:
                    lst.append(text[i:p+len(pattern2)])
    return lst

    # your code goes here
