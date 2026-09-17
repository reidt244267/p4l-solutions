import random # this should be helpful!

# Write your add_noise() function here along with any subroutines that you need.
def add_noise(polling_value: float, margin_of_error: float) -> float:
    """
    Add noise to a polling value.

    Simulates polling data by introducing random noise to the provided polling value.
    The noise is generated from a normal distribution with a mean of 0 and a standard
    deviation equal to half the specified margin of error.

    Parameters:
    - polling_value (float): The original polling value.
    - margin_of_error (float): The margin of error for the polling value.

    Returns:
    float: The polling value with added noise.
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
