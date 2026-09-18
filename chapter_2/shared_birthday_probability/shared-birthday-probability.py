import random # this should be helpful!

# Write your shared_birthday_probability() function here along with any subroutines that you need
def shared_birthday_probability(num_people: int, num_trials: int) -> float:
    """
    Compute the probability that two people in a group of num_people have the same birthday, after running
    num_trials trials.

    Parameters:
    - num_people (int): the number of people in the group
    - num_trials (int): the number of trials to run

    Returns:
    float: the average probability that two people in a group of num_people have the same birthday
    """

    count_collision=0
    for i in range(num_trials):
        if simulate_one_birthday_trial(num_people)==True:
            count_collision=count_collision+1
    
    return count_collision/num_trials


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
