import sys
import math

# Please do not remove package declarations because these are used by the autograder. 
# If you need additional packages, then you may declare them above.


# Insert your triandsq(n) function here, along with any subroutines that you need.
# The function should return a list of triangular and square numbers under n.
def triandsq(n: int) -> list:
    lst=[]
    for i in range(1,n):
        print(i)
        print(perfect_sq(i))
        print(tri(i))
        if (perfect_sq(i) and tri(i)):
            lst.append(i)
    
    return lst  # placeholder


def perfect_sq(n: int) -> bool:
    if (math.isqrt(n)*math.isqrt(n))==n:
        return True
    else:
        return False

def tri(n):
    summ=0
    for i in range(1,n+1):
        summ=summ+i
        if summ==n:
            return True
        elif summ>n:
            return False
        
    
    return False
