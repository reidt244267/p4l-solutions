import random # this should be helpful!

# Write your relatively_prime_probability() function here along with any subroutines that you need
# Hint: include your relatively_prime() function and any subroutines that it calls.
def relatively_prime_probability(
    lower_bound: int,
    upper_bound: int,
    num_pairs: int
) -> float:    
    """
    Compute the probability that two randomly chosen integers in the range [lower_bound, upper_bound] are
    relatively prime.

    Parameters:
    - lower_bound (int): the lower bound of the range
    - upper_bound (int): the upper bound of the range
    - num_pairs (int): the number of pairs to trial

    Returns:
    float: the probability that two randomly chosen integers in the range [lower_bound, upper_bound] are
    relatively prime
    """
    summ=0
    for i in range(num_pairs):
        if one_trial(lower_bound,upper_bound):
            summ=summ+1
    return summ/num_pairs

def one_trial(lower_bound: int, upper_bound: int):
    rand1=random.randint(lower_bound,upper_bound)
    rand2=random.randint(lower_bound,upper_bound)
    return relatively_prime(rand1,rand2)
    

def euclid_gcd(a: int, b: int) -> int:
    """
    Compute the greatest common divisor of two integers using Euclid's algorithm.

    Args:
        a: A positive integer.
        b: A positive integer.
    Returns:
        The greatest common divisor of a and b.
    """
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

# Write your improved relatively_prime() function here. Use euclid_gcd!
def relatively_prime(a: int, b: int) -> bool:
    """
    Check if a and b are relatively prime.

    Parameters:
    - a (int): an integer
    - b (int): an integer

    Returns:
    bool: True if a and b are relatively prime, False otherwise
    """
    if euclid_gcd(a,b)==1:
        return True
    return False
