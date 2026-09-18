import random # this should be helpful!

def average_game_length(num_trials: int) -> float:
    """
    Simulate num_trials games of craps and estimate the average number 
    of dice rolls per game.

    Parameters:
        num_trials (int): The number of games to simulate.

    Returns:
        float: The estimated average number of dice rolls per game.
    """
    sum_rolls=0
    for i in range(num_trials):
        sum_rolls=sum_rolls+play_craps()

    return sum_rolls/num_trials

def play_craps():
    roll=dice_roll()
    num_rolls=1
    if roll in (7,11,2,3,12):
        return num_rolls
    else:
        while(True):
            num_rolls=num_rolls+1
            if dice_roll()==7 or dice_roll()==roll:
                return num_rolls


    

def dice_roll():
    return random.randint(1,6)+random.randint(1,6)
