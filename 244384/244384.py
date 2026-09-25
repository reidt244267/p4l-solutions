# Please do not remove package declarations because these are used by the autograder.
# You may declare additional packages above if needed.


# optional helper function that can make solving many_copies simpler        
def replicate_dna(s: str) -> str:
    return s+s

# Insert your many_copies(a, b) function here, along with any helper functions that you need.
# The function should return a new string that is the result of the input string concatenated 64 times.
def many_copies(s: str) -> str:
    for i in range(6):
        s=replicate_dna(s)
    return s
