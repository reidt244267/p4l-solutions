# Insert your sum_even() function here.
def sum_even(k: int) -> int:
    """
    Return the sum of all positive even integers up to and including k.
    Args:
        k: Upper bound (integer). Only positive even numbers ≤ k are summed.
    Returns:
        The sum 2 + 4 + ... + (largest even ≤ k). Returns 0 if k < 2.
    """
    if k<2:
        return 0
    sum=0
    for i in range(k//2):
        sum=sum+((i+1)*2)
    return sum
