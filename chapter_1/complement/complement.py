# Insert your complement() function here.
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
