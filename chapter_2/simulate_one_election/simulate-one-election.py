import random # this should be helpful!

# Write your simulate_one_election() function here along with any subroutines that you need.
def simulate_one_election(polling_data: dict[str, float],
    electoral_votes: dict[str, int],
    margin_of_error: float
) -> tuple[int, int]:    
    """
    Simulate one election.

    Parameters:
    - polls (dict): A dictionary mapping states to polling percentages.
    - electoral_votes (dict): A dictionary mapping states to electoral votes.
    - margin_of_error (float): The margin of error for the polling data.

    Returns:
    tuple: A tuple of two ints representing the number of electoral votes won by candidate 1 and candidate 2.
    """

    if margin_of_error<0:
        raise ValueError("MOE should be positive")

    #basic checks

    college_votes_1=0
    college_votes_2=0

    #rangle over all the states

    for state,polling_value in polling_data.items():
        #figure out the simulation for each given state
        num_votes=electoral_votes[state]

        adjusted_polling_value=add_noise(polling_value, margin_of_error)

        #who won? adding # of votes from this state to candidate total
        if adjusted_polling_value>=0.5:
            college_votes_1+=num_votes
        else:
            college_votes_2+=num_votes


    return college_votes_1, college_votes_2

def add_noise(polling_value: float, margin_of_error: float)-> float:
    """
    Takes a polling value and margin of error
    Returns adjusted polling value based on some randomness
    """

    #do some checks

    #what is the stdev and mean that we care about?
    #margin of error = 2 * stdev
    #can grab num from "standard normal" distribution (mean=0,stdev=1)

    x=random.gauss(0,1)
    #x has a 95% chance of being between -2 and 2

    x/=2.0
    #x now has a 95% chance of being between -1 and 1

    x*=margin_of_error
    #x now has a 95% chance of being between -margin of error and +margin of error

    return x+polling_value
