# Insert your factorial_array() function here, along with any subroutines that you need.
def factorial_array(n: int) -> list[int]:
    """
    Return a list of factorials from 0! through n!.
    Args:
        n: A non-negative integer.
    Returns:
        A list L of length n + 1 where L[k] == k! for k in [0, n].
    """
    list=[]
    for i in range(n+1):
        list.append(factorial(i))
    return list

def factorial(n):
    sum=1
    for i in range(n):
        sum=sum*(i+1)
    return sum
