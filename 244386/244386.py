import math
# Insert your bacteria_hours() function here.
def bacteria_hours(n: int) -> int:
    """
    Calculate the number of hours required for a bacteria population 
    (starting at size 1 and doubling every hour) to reach at least size n.

    Parameters: n (int) - The target population size (must be >= 1).



    Returns: time (int) - The number of hours until the population is at least size n.
    """
    

    return math.ceil(math.log(n,2))
