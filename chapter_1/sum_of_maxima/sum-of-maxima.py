import sys
# Please do not remove package declarations because these are used by the autograder. If you need additional packages, then you may declare them above.


# Insert your sum_of_maxima() function here.
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

    for key,value in sample2.items():
        if sample1.get(key)==None:
            summ=summ+value
    
    return summ


   

# Note: for the sake of convenience, we are providing a max2() function below.
def max2(x:int, y:int) -> int:
    """
    max_2 returns whatever value is larger, x or y, or the arguments to the function.

    Parameters:
    - x (int): A given integer.
    - y (int): A second integer.

    Returns:
    - int: The larger of the two, x or y.
    """
    if x > y:
        return x
    return y
