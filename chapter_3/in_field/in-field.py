# import necessary libraries
import sys
# Please do not remove package declarations because these are used by the autograder. If you need additional packages, then you may declare them above.

# GameBoard is a two-dimensional list of boolean variables
# representing a single generation of a Game of Life board.
GameBoard = list[list[bool]]  

# write your in_field() function here along with any subroutines that you need. count_rows and count_cols have been provided for your convenience.
def in_field(board: GameBoard, i: int, j: int) -> bool:
    """
    Check if the given (i, j) indices are within the boundaries of the board.
    Args:
        board (GameBoard): The current game board.
        i (int): Row index.
        j (int): Column index.
    Returns:
        bool: True if (i, j) is inside the board, False otherwise.
    """
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
            
