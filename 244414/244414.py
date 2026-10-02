import random

def dice_outcome_matrix(trials: int, seed: int) -> list[list[int]]:
    """
    Simulate rolling two fair six-sided dice `trials` times and return a 6×6 matrix
    of counts. Entry [i][j] is the number of times die1 showed (i+1) and die2 showed (j+1).

    Parameters:
        trials (int): The number of dice rolls to simulate (≥ 1).
        seed (int): random seed for reproducibility.

    Returns:
        list[list[int]]: A 6×6 matrix of counts.
    """
    random.seed(seed)
    matrix = [[0] * 6 for _ in range(6)]
    for i in range(trials):
        dice1=random.randint(1,6)
        dice2=random.randint(1,6)
        matrix[dice1-1][dice2-1]+=1

    return matrix
