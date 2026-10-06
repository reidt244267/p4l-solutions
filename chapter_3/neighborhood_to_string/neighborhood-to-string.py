# import necessary libraries
import sys

# Please do not remove package declarations because these are used by the autograder. If you need additional packages, then you may declare them above.

# GameBoard is a two-dimensional list of boolean variables
# representing a single generation of a Game of Life board.
GameBoard = list[list[int]]  

# write your neighborhood_to_string() function here along with any subroutines that you need.
def neighborhood_to_string(board: GameBoard, r: int, c: int, neighborhood_type: str) -> str:
    """
    Construct the neighborhood string for a given cell in a GameBoard.
    Args:
        current_board (GameBoard): The current game board.
        r (int): The row index of the cell.
        c (int): The column index of the cell.
        neighborhood_type (str): The type of neighborhood ("Moore" or "vonNeumann").
    Returns:
        str: A string formed of the central square followed by its neighbors
        according to the neighborhood type indicated.
    """
    neighborhood=board[r][c]

    neighborhood_cells=[()]
    if neighborhood_type=="Moore":
        neighborhood_cells=[(r-1,c-1),(r-1,c),(r-1,c+1),(r,c+1),(r+1,c+1),(r+1,c),(r+1,c-1),(r,c-1)]
    elif neighborhood_type=="vonNeumann":
        neighborhood_cells=[(r-1,c),(r,c+1),(r+1,c),(r,c-1)]
    else:
        raise ValueError("We really can't get here")

    for (x,y) in neighborhood_cells:
        if in_field(board,x,y):
            neighborhood+=str(board[x][y])
        else:
            neighborhood+=str(0)

        
    return neighborhood

def count_rows(board: list[list[bool]]) -> int:
    """
    Count the number of rows in a game board.

    Args:
        board: A two-dimensional array of boolean values.
    Returns:
        The number of rows in the board.
    """
    return len(board)


def count_columns(board: list[list[bool]]) -> int:
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
            
def in_field(board: GameBoard, i: int, j: int) -> bool:
    """
    Check if the indices (i, j) are within the bounds of the board.
    Args:
        board (GameBoard): The game board (2D list of ints).
        i (int): Row index.
        j (int): Column index.
    Returns:
        bool: True if (i, j) is inside the board, False otherwise.
    """
    # parameter checks
    if not isinstance(board, list) or len(board) == 0:
        raise ValueError("board must be a non-empty GameBoard.")
    if not isinstance(i, int) or not isinstance(j, int):
        raise ValueError("i and j must be integers.")
    if i < 0 or j < 0:
        return False
    if i >= count_rows(board) or j >= count_columns(board):
        return False
    # if we survive to here, then we are on the board
    return True
