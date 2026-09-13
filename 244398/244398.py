def min_window_skew(genome: str, window_len: int) -> list[int]:
    """
    Return all start indices of windows of length window_len in genome
    that achieve the minimum GC-skew.

    Parameters:
        genome (str): A nonempty DNA string consisting of 'A', 'C', 'G', 'T'.
        window_len (int): The length of the window (1 ≤ window_len ≤ len(genome)).

    Returns:
        (list[int]): A list of start indices (0-based) in increasing order 
                   where the window skew is minimal.
                   If window_len > len(genome), return [].
    """
    if window_len>len(genome):
        return []
    
    if window_len==len(genome):
        return [0]

    lst_skew=[]
    for i in range(0, len(genome)-window_len+1):
        lst_skew.append(local_skew(genome[i:i+window_len]))

    min_in_lst=min_list(lst_skew)
    min_lst=[]
    for index, item in enumerate(lst_skew):
        if item==min_in_lst:
            min_lst.append(index)
        

    return min_lst

def local_skew(wind):  #count(G)-count(C)
    count_G=0
    count_C=0
    for char in wind:
        if char=='G':
            count_G=count_G+1
        if char=='C':
            count_C=count_C+1
    return count_G-count_C

def min_list(lst: list): #smallest int in the list
    minn=lst[0]
    for item in lst:
        if item<minn:
            minn=item
    
    return minn

