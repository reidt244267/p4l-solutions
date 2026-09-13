# Insert your minimum_skew() function here, along with any subroutines that you need.
def minimum_skew(genome: str) -> list[int]:
    """
    minimum_skew finds the list of integers representing all integer indices that minimizes the skew     of the genome text.
    Parameters:
    - genome (str): A genome string.
    Returns:
    - list[int]: A list of indices that minimize the skew value of the genome text.
    """
    if len(genome)==0:
        return []
    """
    lst_skew=[0]
    for index, charr in enumerate(genome):
        lst_skew.append(skew_array(charr)+lst_skew[index-1])
        """
    
    lst_skew=skew_array(genome)
    
    min_in_lst=min_list(lst_skew)
    min_lst=[]
    for index, item in enumerate(lst_skew):
        if item==min_in_lst:
            min_lst.append(index)


    return min_lst

def skew_array(genome: str) -> list[int]:
    """
    skew returns 1 or -1 if the given single character string is either
    G or C respectively, otherwise returns zero. (Throws error if the 
    given string does not have a length of one).

    Parameters:
    - symbol (str): A given one character string.

    Returns:
    - int: The symbol's respective skew score.
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

def min_list(lst: list): #smallest int in the list
    minn=lst[0]
    for item in lst:
        if item<minn:
            minn=item
    
    return minn
