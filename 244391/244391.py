import sys

# Please do not remove package declarations because these are used by the autograder. 
# If you need additional packages, then you may declare them above.


# Insert your collatz(n) function here, along with any subroutines that you need.
# The function should return a list of the terms in a collatz sequence from n to 1.

def collatz(n: int) -> list:
    
    lst=[]
    lst.append(n)
    onee=False
    if n==1:
        onee=True
    while onee==False:
        
        if n%2==0:
            n=n//2
            lst.append(n)
        else:
            n=3*n+1
            lst.append(n)
        if n==1:
            onee=True
        
    
    return lst #placeholder
