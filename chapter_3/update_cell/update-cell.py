import sys

# Please do not remove package declarations because these are used by the autograder. If you need additional packages, then you may declare them above.

# GameBoard is a two-dimensional list of boolean variables
# representing a single generation of a Game of Life board.
GameBoard = list[list[bool]]  

# write your update_cell() function here along with any subroutines that you need.
def update_cell(board: GameBoard, r: int, c: int) -> bool:
    """
    Determine the next state of the cell at (r, c) in the Game of Life.
    Args:
        board (GameBoard): The current game board.
        r (int): Row index.
        c (int): Column index.
    Returns:
        bool: True if the cell is alive in the next generation, False otherwise.
    """
    if not isinstance(board,list) or len(board)==0:
        raise ValueError("board must be a non-empty GameBoard")
    if not isinstance(r,int) or not isinstance(c,int):
        raise ValueError("r and c must be integers")

    num_neighbors=count_live_neighbors(board,r,c)

    #if alive
    if board[r][c]:
        if num_neighbors==2 or num_neighbors==3:
            return True
        else:
            return False

    else: #dead
        if num_neighbors==3:
            return True
        else:
            return False


def count_live_neighbors(board: GameBoard, r, c):
    num_live_neighbors=0

    for i in range(r-1,r+2):
        for j in range(c-1,c+2):
            if ((i!=r) or (j!=c)) and in_field(board,i,j):
                if board[i][j]:
                    num_live_neighbors+=1

    return num_live_neighbors

def in_field(board,i,j):
    #check if not in field-> return false
    num_rows=count_rows(board)
    num_cols=count_cols(board)
    if i<0 or j<0 or i>=num_rows or j>= num_cols:
        return False


    return True

def count_rows(board: list[list[bool]]) -> int:
    """
    Count the number of rows in a game board.

    Args:
        board: A two-dimensional array of boolean values.
    Returns:
        The number of rows in the board.
    """
    return len(board)


def count_cols(board: list[list[bool]]) -> int:
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
