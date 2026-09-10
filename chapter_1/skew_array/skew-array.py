# Insert your skew_array() function here, along with any subroutines that you need.
def skew_array(genome: str) -> list[int]:
    """
    skew_array returns the list that represents the skew at each position of the genome. That is,       the i-th position in the list is the skew at the i-th position of the genome.
    Parameters:
    - genome (str): A genome string.
    Returns:
    - list[int]: A list representing the skew of the genome string.
    """
    n=len(genome)

    if n==0:
        raise ValueError("Empty genome given")

    skew_array=[0]*(n+1)
    #use a dictionrary instead of writing big elif
    skew: dict[str,int]={
        "A":0,
        "C":-1,
        "G":1,
        "T":0
    }

    #range over the genome and set skew_array[k]
    for i in range(1, n+1):
        symbol=genome[i-1]

        if symbol in skew:
            skew_array[i]=skew_array[i-1]+skew[symbol]
        else:
            raise ValueError("Invalid letter in DNA string.")
    return skew_array
    
