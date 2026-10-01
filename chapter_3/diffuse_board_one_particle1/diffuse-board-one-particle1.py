import sys
import math

# Please do not remove package declarations because these are used by the autograder. If you need additional packages, then you may declare them above.

# Insert your diffuse_board_one_particle() function here, along with any subroutines that you need.
def diffuse_board_one_particle(
    current_board: list[list[float]],
    kernel: list[list[float]]
) -> list[list[float]]:
    """
    Apply one diffusion time step to a board using a 3x3 kernel.

    Args:
        current_board: A 2D list of decimals representing current concentrations.
        kernel: A 3x3 list of decimals representing the diffusion kernel.
    Returns:
        A new 2D list of decimals representing the board after one diffusion step.
    """
    num_rows=count_rows(current_board)
    num_cols=count_cols(current_board)

    new_board=initialize_board(num_rows,num_cols)

    for p in range(num_rows):
        for i in range(num_cols):
            summ=0
            for k in range(-1,2):
                for l in range(-1,2):
                    if (in_field(current_board,p+k,i+l)):
                        summ+=current_board[p+k][i+l]*kernel[1+k][1+l]
            new_board[p][i]=current_board[p][i]+summ
            
    return new_board


def initialize_board(num_rows, num_cols):
    board: GameBoard=[]

    for _ in range(num_rows):
         current_row=[0.0]*num_cols
         board.append(current_row)
    return board

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

def assert_rectangular(board: GameBoard) -> None:
    """
    Check whether a GameBoard is rectangular.
    Args:
        board (GameBoard): The game board.
    Raises:
        ValueError: If the board has no rows or if its rows are not the same length.
    """
    if len(board) == 0:
        raise ValueError("Error: no rows in GameBoard.")
    first_row_length = len(board[0])
    
    # range over rows and make sure that they have the same length as first row
    for row in board:
        if len(row) != first_row_length:
            raise ValueError("Error: GameBoard is not rectangular.")
            
