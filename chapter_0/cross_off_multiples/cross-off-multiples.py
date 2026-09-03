# Insert your cross_off_multiples() function here, along with any subroutines that you need.
def cross_off_multiples(prime_booleans: list[bool], p:int) -> list[bool]:
    """
    Takes as input a list of booleans representing the primality of all integers
    up to some point.

    Also takes as input an integer p

    Updates the list by setting to False all multiples of p (starting at 2*p)
    """
    #range over multiples
    for i in range(p+p, len(prime_booleans),p):
        #cross off the current number cuz we know i is a multiple of p
        prime_booleans[i]=False

    return prime_booleans
