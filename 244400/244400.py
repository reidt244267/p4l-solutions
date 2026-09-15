def at_skew_array(genome: str) -> list[int]:
    """
    Compute the AT skew array of a genome string.

    Parameters:
        genome (str): A DNA string consisting of 'A', 'C', 'G', 'T' (case-insensitive).

    Returns:
        list[int]: The AT skew array, starting with 0, where each subsequent
                   value is the previous value plus +1 for 'A', -1 for 'T',
                   and 0 otherwise.
    """
    lst=[0]
    dictt={
        "A":1,
        "T":-1,
        "C":0,
        "G":0
    }
    count=0
    for index,char in enumerate(genome):
        lst.append(lst[count]+dictt[char])
        count=count+1
    return lst
