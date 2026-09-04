# Insert your fibonacci_array() function here, along with any subroutines that you need.
def fibonacci_array(n: int) -> list[int]:
    """
    Return an array of Fibonacci numbers from F₀ through Fₙ.
    Args:
        n: A non-negative integer.
    Returns:
        A list F of length n + 1 such that F[k] is the k-th Fibonacci number.
    """
    lst=[]
    lst.append(1)
    if n==0:
        return lst
    else:
        lst.append(1)
    for i in range(0,n-1):
        lst.append(lst[i]+lst[i+1])


    return lst
