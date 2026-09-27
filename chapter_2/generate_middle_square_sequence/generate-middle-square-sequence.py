# Write your generate_middle_square_sequence() function here along with any subroutines that you need.
def generate_middle_square_sequence(seed: int, num_digits: int) -> list[int]:
    """
    Generate a middle square sequence.

    Parameters:
    - seed (int): the first value in the sequence
    - num_digits (int): the number of digits in the middle of each squared value to add to the sequence

    Returns:
    list: a middle-square sequence
    """
    seq = {}
    seq[seed]=1
    lstt=[seed]
    keep_going=True
    while(keep_going):
        new_seed = square_middle(lstt[len(lstt)-1], num_digits)
        if seq.get(new_seed)==1:
            keep_going=False
        seq[new_seed]=1
        lstt.append(new_seed)
        

    return lstt




# Write your square_middle() function here along with any subroutines that you need.
def square_middle(x, num_digits):
    """
    Get the middle digits of x squared.

    Parameters:
    - x (int): a positive integer
    - num_digits (int): the number of digits in the middle of x squared to return

    Returns:
    int: the middle digits of x squared
    """
    if (num_digits%2==1) or (x<0) or (num_digits<0) or (count_num_digits(x)>num_digits):
        return -1


    sqaured=x**2
        
    digits_rem=num_digits/2
    sqaured=remove_start(sqaured,num_digits,digits_rem)
    return int(remove_end(sqaured,digits_rem))

    
def remove_start(x, num_digits,digits_rem):
    return x%(10**(2*num_digits-digits_rem))

def remove_end(x,digits_rem):
    return x//(10**digits_rem)

# Write your count_num_digits() function here along with any subroutines that you need.
def count_num_digits(x: int) -> int:
    """
    Count the number of digits in a positive integer x.

    Parameters:
    - x (int): a positive integer

    Returns:
    int: the number of digits in x
    """
    if x>=0:
        return len(str(x))
    elif x<0:
        return len(str(x))-1


