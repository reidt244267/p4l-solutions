import sys
import math

# Please do not remove package declarations because these are used by the autograder. If you need additional packages, then you may declare them above.

# Cell contains two attributes corresponding to
# the concentration of predator (0-th element) and prey (1-th element) in the cell
Cell = tuple[float, float]

# Board is a two-dimensional slice of Cells
Board = list[list[Cell]]

# Insert your change_due_to_diffusion() function here, along with any subroutines that you need.
def change_due_to_diffusion(
    current_board: Board,
    row: int,
    col: int,
    prey_diffusion_rate: float,
    predator_diffusion_rate: float,
    kernel: list[list[float]]
) -> Cell:
    """
    Compute the change in a cell due to diffusion.

    Args:
        current_board: A 2D list of Cells, where each Cell is a tuple of two floats.
        row: Row index of the cell.
        col: Column index of the cell.
        prey_diffusion_rate: Diffusion rate for the prey component.
        predator_diffusion_rate: Diffusion rate for the predator component.
        kernel: A 3x3 diffusion kernel.
    Returns:
        A Cell representing the change in the cell at (row, col) due to diffusion.
    """

    prey_sum=0
    pred_sum=0
    p=row
    i=col
    for k in range(-1,2):
        for l in range(-1,2):
            if (in_field(current_board,p+k,i+l)):
                prey_sum+=current_board[p+k][i+l][0]*kernel[1+k][1+l]*prey_diffusion_rate
                pred_sum+=current_board[p+k][i+l][1]*kernel[1+k][1+l]*predator_diffusion_rate
    return (prey_sum,pred_sum)

def in_field(board,i,j):
    #check if not in field-> return false
    num_rows=count_rows(board)
    num_cols=count_cols(board)
    if i<0 or j<0 or i>=num_rows or j>= num_cols:
        return False


    return True

def count_rows(board: GameBoard) -> int:
    """
    Count the number of rows in a game board.

    Args:
        board: A two-dimensional array of boolean values.
    Returns:
        The number of rows in the board.
    """
    return len(board)


def count_cols(board: GameBoard) -> int:
    """
    Count the number of columns in a game board.

    Args:
        board: A two-dimensional array of boolean values.
    Returns:
        The number of columns in the board.
    """
    # assume that we have a rectangular board
    if count_rows(board) == 0:
        raise Exception("Error: empty board given to count_cols")
    # give # of elements in 0-th row
    return len(board[0])
    
