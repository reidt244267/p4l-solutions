# Insert your find_frequent_words() function here, along with any subroutines that you need.
def find_frequent_words(text: str, k: int) -> list[str]:
    """
    find_frequent_words returns a list containing the most frequent k-mers occurring in text,           including overlaps.
    Parameters:
    - text (str): A given text for the function.
    - k (int): The size of the k-mers.
    Returns:
    - The list of the most frequent k-mers occurring in text, including overlaps.
    """
    frequentPatterns = []
    freqMap = frequency_table(text, k)
    maxx = max_map_value(freqMap)
    for pattern, value in freqMap.items():
        if freqMap[pattern] == maxx:
            frequentPatterns.append(pattern)
    return frequentPatterns


    
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
def max_map_value(dict_values: dict) -> int:
    """
    max_map_value finds the maximum value of a given dictionary.

    Parameters:
    - dict_values (dict): A dictionary that has integers as values.

    Retursn:
    - int: The highest value key in the given dictionary.
    """

    m = 0
    firstTime = True
    for pattern,value in dict_values.items():
        if (firstTime == True) or (dict_values[pattern] > m):
            firstTime= False
            m = dict_values[pattern]
    return m
