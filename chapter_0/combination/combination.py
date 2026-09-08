# Insert your combination() function here, along with any subroutines that you need.
def combination(n: int, k: int) -> int:
    """
    Compute the combination statistic C(n, k) = n! / ((n - k)! * k!).
    Args:
        n: Total number of distinct objects (non-negative).
        k: Size of the subset to choose (non-negative).
    Returns:
        The number of ways to choose k items from n without order (the binomial coefficient).
    """
    return Fractorial(n)//(Fractorial(n-k)*Fractorial(k))

def Fractorial(n):
    result=1
    while n>0:
        result=result*(n)
        n=n-1
    return result
