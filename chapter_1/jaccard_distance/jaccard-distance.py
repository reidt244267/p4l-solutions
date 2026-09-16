import sys
# Please do not remove package declarations because these are used by the autograder. If you need additional packages, then you may declare them above.

# Insert your jaccard_distance() function here, along with any subroutines that you need.
def jaccard_distance(sample1: dict[str, int], sample2: dict[str, int]) -> float:
    """
    Compute the Jaccard distance between two frequency tables.

    Args:
        sample1: A frequency table mapping strings to integers.
        sample2: A frequency table mapping strings to integers.
    Returns:
        The Jaccard distance between the two samples.
    """
    sumMin = sum_of_minima(sample1, sample2)
    sumMax = sum_of_maxima(sample1, sample2)
    return 1-sumMin/sumMax


def sum_of_maxima(sample1: dict, sample2: dict) -> int:
    """
    sum_of_maxima returns the sum of the maxima of the values for shared keys
    across two samples. If a key is not shared it is still added to the sum.

    Parameters:
    - sample1 (dict): A given input sample.
    - sample2 (dict): Another given input sample.

    Returns:
    - int: The sum of the minima of all values for shared keys.  
    If a key is not shared it is still added to the sum.
    """
    summ=0
    for key,value in sample1.items():
        if sample2.get(key)!=None:
            summ=summ+max2(value,sample2.get(key))
        else:
            summ=summ+value
    return summ

def sum_of_minima(sample1: dict, sample2: dict) -> int:
    """
    sum_of_minima returns the sum of the minima of the values for shared keys
    across two samples.

    Parameters:
    - sample1 (dict): A given input sample.
    - sample2 (dict): Another given input sample.

    Returns:
    - int: The sum of the minima of all values for shared keys. 
    """
    summ=0
    for key,value in sample1.items():
        if sample2.get(key)!=None:
            summ=summ+min2(value,sample2.get(key))
    return summ

# Note: for the sake of convenience, we are providing min2() and max2() functions below.
def min2(x: int, y: int) -> int:
    """
    Return the minimum of two integers.

    Args:
        x: An integer.
        y: An integer.
    Returns:
        The smaller of x and y.
    """
    if x < y:
        return x
    return y

def max2(x: int, y: int) -> int:
    """
    Return the maximum of two integers.

    Args:
        x: An integer.
        y: An integer.
    Returns:
        The larger of x and y.
    """
    if x > y:
        return x
    return y
