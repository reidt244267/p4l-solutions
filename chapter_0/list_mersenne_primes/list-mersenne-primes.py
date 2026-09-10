import math

# Insert your list_mersenne_primes() function here, along with any subroutines that you need.
def list_mersenne_primes(n: int) -> list[int]:
    """
    List all Mersenne primes of the form 2^p - 1 with p ≤ n.
    Args:
        n: Upper bound on the exponent p (non-negative integer).
    Returns:
        A list of all primes of the form 2^p - 1 where p is prime and p ≤ n,
        in increasing order of p.
    """
    lst=[]
    lst_primes=list_primes(n)
    for item in lst_primes:
        if is_prime((2**item)-1):
            lst.append((2**item)-1)

    return lst

# Provided for you (from an earlier exercise):
def sieve_of_eratosthenes(n: int) -> list[bool]:
    """
    Returns a list of boolean variables storing the primality of each nonnegative integer up to and including n,
    implementing the "sieve of Eratosthenes" algorithm.

    Parameters:
    - n (int): an integer

    Returns:
    list (bool): a list of boolean variables storing the primality of each nonnegative integer up to and including n.
    """
    prime_booleans = [False] * (n + 1)
    # set everything to prime other than prime_booleans[0] and prime_booleans[1]
    for k in range(2, n + 1):
        prime_booleans[k] = True
    # now, iterate over prime_booleans, and cross off multiples of the first prime we see, iterating this process.
    for p in range(2, int(n**0.5) + 1):
        if prime_booleans[p] == True:
            prime_booleans = cross_off_multiples(prime_booleans, p)
    return prime_booleans

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


# Insert your list_primes() function here, along with any subroutines that you need.
def list_primes(n: int) -> list[int]:
    """
    List all prime numbers up to and (possibly) including n.
    Parameters:
    - n (int): an integer
    Returns:
    list (int): a list containing all prime numbers up to and (possibly) including n.
    """
    lst=sieve_of_eratosthenes(n)
    finallst=[]
    for i in range(0,n+1):
        if lst[i]==True:
            finallst.append(i)

    return finallst

# Hint: insert your sieve_of_eratosthenes() and cross_off_multiples functions here

# Insert your is_prime() function here, along with any subroutines that you need.
def is_prime(k: int) -> bool:
    """
    Determine whether an integer is prime.
    Args:
        p: Integer to test (may be negative or zero).
    Returns:
        True if p is prime, False otherwise.
    """

    if k<0:
        raise ValueError("Error: k must be nonnegative")

    if k<2:
        return False

    #try every number between 2 and k-1
    #if it's a disvior, return False
    #can stop range at sqrt(k)
    for i in range (2,math.isqrt(k)+1):
        if k%i==0:
            return False

    return True
