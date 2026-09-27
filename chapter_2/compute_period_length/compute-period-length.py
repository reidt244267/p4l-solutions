# Write your compute_period_length() function here along with any subroutines that you need
def compute_period_length(a: list[int]) -> int:
    """
    Compute the period length of a list of integers.

    Parameters:
    - a: a list of integers

    Returns:
    int: the length of the period of a
    """
    hstt={}
    count=0
    for index,value in enumerate(a):
        if not (hstt.get(value)==None):
            count=index-hstt[value]
            break
        else:
            hstt[value]=index

    return count
