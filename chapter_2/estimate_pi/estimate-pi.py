import random # this should be helpful!

# Write your estimate_pi() function here along with any subroutines that you need.
def estimate_pi(num_points: int) -> float:
    """
    Estimate pi using a Monte Carlo method.

    Parameters:
    - num_points (int): the number of points to use in the Monte Carlo method

    Returns:
    float: an estimate of pi
    """
    on_board=0
    for i in range(num_points):
        if one_round()==True:
            on_board=on_board+1
    return (on_board/num_points)*4

def one_round():
    x=random.random()*2-1
    y=random.random()*2-1
    return dart_in_circle(x,y)

def dart_in_circle(x,y):
    if (x**2)+(y**2)<=1:
        return True
    else:
        return False
