import random # this should be helpful!

# Write your simulate_one_birthday_trial() function here along with any subroutines that you need
def simulate_one_birthday_trial(num_people: int) -> bool:
    """
    Simulate one trial of the birthday game with num_people people.

    Parameters:
    - num_people (int): the number of people in the group

    Returns:
    bool: True if there is a collision, False otherwise
    """
    bday_list=[]
    for i in range(num_people):
        bday_list.append(random.randint(1,365))
    
    return has_repeat(bday_list)


# Write your has_repeat() function here along with any subroutines that you need
def has_repeat(a: list[int]) -> bool:
    """
    Check if a list has repeat elements.

    Parameters:
    - a: a list of integers

    Returns:
    bool: True if a has repeat elements, False otherwise
    """
    for key,value1 in enumerate(a):
        for i in range(key+1,len(a)):
            if value1==a[i]:
                return True

    return False
