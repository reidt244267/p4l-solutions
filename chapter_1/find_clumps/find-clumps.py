# Insert your find_clumps() function here, along with any subroutines that you need.

def find_clumps(text: str, k: int, window_length: int, t: int) -> list[str]:
    """
    Finds a list of strings representing all k-mers that appear at least t times in a window of         given length in the string.
    Parameters:
    - text (str): An input string.
    - k (int): k-mer's of size k.
    - window_length (int): the size of substrings of text in which we are looking for clumps
    - t (int): The k-mers must appear at least t amount of times.
    Output:
    - list: A list of k-mers that occur at least t times in a window of length window_length in
    text.
    """
    n=len(text)

    if len(text)==0:
        raise ValueError("Error: text must be nonempty")

    if k>window_length:
        raise ValueError("Error: k must be less than or equal to window_length")

    if t<0 or k<0 or n<0:
        raise ValueError("Error: k, t, and window_length must be nonnegative")

    patterns: list[str] = [] #will store our frequent k-mers

    #range over all the windows
    #number of possible substrings: n-window_length+1
    for i in range(0,n-window_length+1):
        window=text[i:i+window_length]
        freq_map=frequency_table(window,k)

        #what patterns appear at least t times in freq_map?
        for s,val in freq_map.items():
            if val>=t and (not(s in patterns)):
                patterns.append(s)


    return patterns

def frequency_table(text: str, k: int) -> dict:
    """
    frequency_table finds the frequencies of each k-mer occuring in a given text, 
    including overlaps.

    Parameters:
    - text (str): The string text to search for kmers.
    - k (int): The size of the kmers.

    Returns:
    - dict (str : int): The dictionary of kmers to their frequencies in the given
    text string, including overlaps.
    """
    freqMap = {}
    n = len(text)
    for i in range (0,n-k+1):
        pattern = text[i: i + k]
        if freqMap.get(pattern)==None:
            freqMap[pattern] = 1
        else:
            freqMap[pattern]+=1
    return freqMap
