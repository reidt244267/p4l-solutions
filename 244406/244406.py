import random # this should be helpful!

def monty_hall(num_trials: int, switch: bool) -> float:
    """
    Simulate the Monty Hall game show problem.

    Parameters:
        num_trials (int): The number of games to simulate.
        switch (bool): True if the contestant always switches,
                       False if the contestant always stays.

    Returns:
        float: The estimated probability of winning the prize.
    """
    win_count=0
    for i in range(num_trials):
        if one_round(switch)==True:
            win_count=win_count+1

    return win_count/num_trials

def one_round(switch:bool):
    options=[1,2,3]
    correct_door=random.choice(options)
    first_pick=random.choice(options)
    if switch==False:
        if first_pick==correct_door:
            return True
        else:
            return False
    elif switch==True:
        if first_pick==correct_door:
            return False
        else:
            return True
        
    


        


