import sys
import math

# Please do not remove package declarations because these are used by the autograder. If you need additional packages, then you may declare them above.
# Cell contains two attributes corresponding to
# the concentration of predator (0-th element) and prey (1-th element) in the cell
Cell = tuple[float, float]

# Board is a two-dimensional slice of Cells
Board = list[list[Cell]]

# Insert your update_board() function here, along with any subroutines that you need.
def update_board(
    currentBoard: Board,
    feedRate: float,
    killRate: float,
    preyDiffusionRate: float,
    predatorDiffusionRate: float,
    kernel: list[list[float]]
) -> Board:
    """
    Update a Gray-Scott reaction-diffusion board by one time step.

    Args:
        current_board: A 2D list of Cells, where each Cell is a list of two floats.
        feed_rate: Feed reaction rate.
        kill_rate: Kill reaction rate.
        prey_diffusion_rate: Diffusion rate for the prey component.
        predator_diffusion_rate: Diffusion rate for the predator component.
        kernel: A 3x3 diffusion kernel.
    Returns:
        A new Board representing the next time step after applying the
        Gray-Scott reaction-diffusion update rules.
    """

    numRows = count_rows(currentBoard)
    numCols = count_rows(currentBoard)
    newBoard = initialize_board(numRows, numCols)
    for row in range(numRows):
        for col in range(numCols):
            newBoard[row][col] = UpdateCell(currentBoard, row, col, feedRate, killRate, preyDiffusionRate, predatorDiffusionRate, kernel)
    return newBoard

def UpdateCell(currentBoard, row, col, feedRate, killRate, preyDiffusionRate, predatorDiffusionRate, kernel):
    currentCell = currentBoard[row][col]
    diffusionValues = change_due_to_diffusion(currentBoard, row, col, preyDiffusionRate, predatorDiffusionRate, kernel)
    reactionValues = change_due_to_reactions(currentCell, feedRate, killRate)
    return sum_cells(currentCell, diffusionValues, reactionValues)


def sum_cells(*cells: Cell) -> list[float]:
    """
    Sum corresponding elements of multiple cells.

    Args:
        *cells: An arbitrary number of Cell values, where each Cell is
            a tuple of two floats.
    Returns:
        A single Cell representing the element-wise sum of all input cells.
    """
    first_lst=[]
    second_lst=[]

    for (x,y) in cells:
        first_lst.append(x)
        second_lst.append(y)


    return (sum_lst(first_lst),sum_lst(second_lst))

def sum_lst(lst) -> int:
    summ=0
    for val in lst:
        summ += val
    return summ

def change_due_to_reactions(
    current_cell: Cell,
    feed_rate: float,
    kill_rate: float
) -> Cell:
    """
    Compute the change in a cell due to Gray-Scott reactions.

    Args:
        current_cell: The current cell.
        feed_rate: The feed reaction rate.
        kill_rate: The kill reaction rate.
    Returns:
        A Cell representing the change in current_cell due to reactions.
    """
    #[A]new =   f(1-[A]) - r · [A] · [B]2
    #[B]new =  - k · [B] + r · [A] · [B]2 .

    new_A=(feed_rate*(1-current_cell[0]))-(current_cell[0]*(current_cell[1]**2))
    new_B=(-kill_rate*current_cell[1])+(current_cell[0]*(current_cell[1]**2))
    return (new_A,new_B)

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

def initialize_board(num_rows, num_cols):
    board: GameBoard=[]

    for _ in range(num_rows):
         current_row=[0.0]*num_cols
         board.append(current_row)
    return board
    
