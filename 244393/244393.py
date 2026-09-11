def rc_match_at(pattern: str, text: str, i: int) -> bool:
    """
    Return True if either the given DNA pattern or its reverse complement 
    occurs in the text starting at position i, otherwise return False.

    Parameters:
        pattern (str): A DNA string consisting of 'A', 'C', 'G', 'T'.
        text (str): The DNA text to search within.
        i (int): The starting index in text to check for the match.

    Returns:
        bool: True if pattern or its reverse complement matches text[i:],
              False otherwise.
    """
    rev=reverse_complement(pattern)
    if pattern==text[i:i+len(pattern)]:
        return True
    elif rev==text[i:i+len(pattern)]:
        return True
    else:
        return False



def reverse_complement(dna: str) -> str:
    """
    Compute the reverse complement of a DNA string.

    Args:
        dna: A DNA string.
    Returns:
        The reverse complement of the DNA string.
    """
    return reverse(complement(dna))

def complement(dna: str) -> str:
    """
    Finds the complementary strand of the given string.

    Parameters:
    - dna (str): A dna string.

    Returns:
    - str: the string whose i-th symbol is the complementary 
    nucleotide of the i-th symbol of the input string. (A-T, C-G, T-A, G-C).
    """
    lst=''
    for char in dna:
        if char=='A':
            lst=lst+'T'
        elif char=='T':
            lst=lst+'A'
        elif char=='G':
            lst=lst+'C'
        elif char=='C':
            lst=lst+'G'



    return lst

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
