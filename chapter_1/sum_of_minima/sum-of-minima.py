import sys
# Please do not remove package declarations because these are used by the autograder. If you need additional packages, then you may declare them above.


# Insert your sum_of_minima() function here, along with any subroutines that you need.
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

def min_dict(dict_values):
    m = 0
    firstTime = True
    for pattern,value in dict_values.items():
        if (firstTime == True) or (dict_values[pattern] < m):
            firstTime= False
            m = dict_values[pattern]
    return m

# Note: for the sake of convenience, we are providing a min2() function below.
def min2(x:int, y:int) -> int:
    """
    min_2 returns whatever value is smaller, x or y, or the arguments to the function.

    Parameters:
    - x (int): A given integer.
    - y (int): A second integer.

    Returns:
    - int: The smaller of the two, x or y.
    """

    if x < y:
        return x
    return y
