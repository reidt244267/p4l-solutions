# import necessary libraries
import sys

# Please do not remove package declarations because these are used by the autograder. If you need additional packages, then you may declare them above.

# GameBoard is a two-dimensional list of boolean variables
# representing a single generation of a Game of Life board.
GameBoard = list[list[bool]]  

# write your play_game_of_life() function here along with any subroutines that you need.
# The AutoGrader will only analyze the final step of your solution. If you want to see the output of your intermediate steps, then you may print them to stdout.
def play_game_of_life(initial_board: GameBoard, num_gens: int) -> list[GameBoard]:
    """
    Simulate the Game of Life for a number of generations.

    Args:
        board: A 2D list of booleans representing the initial Game of Life board.
        num_gens: Number of generations to simulate.
    Returns:
        A list of GameBoard states of length num_gens + 1, starting with
        the initial board and followed by each successive generation.
    """
    boards: list[GameBoard]=[]
    boards.append(initial_board)
    for i in range(num_gens):
        prev_board=boards[i]
        new_board=update_board(prev_board)
        boards.append(new_board)


    return boards

def update_board(current_board: GameBoard) -> GameBoard:
    """
    update_board takes as input a GameBoard and returns the board resulting
    from playing the Game of Life for one generation.
    Args:
        current_board (GameBoard): The current game board.
    Returns:
        GameBoard: A new board representing the next generation.
    """
    num_rows=count_rows(current_board)
    num_cols=count_cols(current_board)

    new_board=initialize_board(num_rows,num_cols)

    for p in range(num_rows):
        for i in range(num_cols):
            new_board[p][i]=update_cell(current_board, p, i)
    return new_board

def update_cell(board: GameBoard, r: int, c: int):
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

def initialize_board(num_rows: int, num_cols: int) -> list[list[bool]]:
    """
    Initialize a board with all cells set to False.

    Args:
        num_rows: Number of rows in the board.
        num_cols: Number of columns in the board.
    Returns:
        A 2D list representing the board, initialized to False.
    """
    b = [[False] * num_cols for _ in range(num_rows)]
    return b

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
