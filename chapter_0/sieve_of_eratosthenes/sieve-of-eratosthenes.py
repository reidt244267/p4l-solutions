import math
# Provided for you (from an earlier exercise):
def cross_off_multiples(prime_booleans: list[bool], p:int) -> list[bool]:
    """
    Returns an updated list in which all variables in the array whose indices are multiples of p (greater than p) have
    been set to false.
    Parameters:
    - prime_booleans (list): a list of boolean variables storing the primality of each nonnegative integer
    - p (int): an integer
    Returns:
    list (bool): a list of boolean variables storing the primality of each nonnegative integer up to and including n with
    multiples of p (greater than p) set to false.
    """
    n = len(prime_booleans) - 1
    for k in range(2 * p, n + 1, p):
        prime_booleans[k] = False  # k is composite
    return prime_booleans


# Insert your sieve_of_eratosthenes() function here, along with any subroutines that you need.
def sieve_of_eratosthenes(n: int) -> list[bool]:
    """
    Returns a list of boolean variables storing the primality of each nonnegative integer up to and including n,
    implementing the "sieve of Eratosthenes" algorithm.
    Parameters:
    - n (int): an integer
    Returns:
    list (bool): a list of boolean variables storing the primality of each nonnegative integer up to and including n.
    """
    #assume that everything is prime
    prime_booleans=[True]*(n+1)
    prime_booleans[0]=False
    prime_booleans[1]=False
    #range over all integers between 2 and sqrt(n) and 
    # cross off their multiples if they're prime
    for p in range(2,math.isqrt(n)+1):
        #is the current number gray?
        if prime_booleans[p]==True:
            prime_booleans=cross_off_multiples(prime_booleans, p)

    return prime_booleans

# Hint: insert your cross_off_multiples() function here
