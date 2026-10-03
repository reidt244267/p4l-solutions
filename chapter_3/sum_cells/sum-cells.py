import sys
import math
# Cell contains two attributes corresponding to
# the concentration of predator (0-th element) and prey (1-th element) in the cell
Cell = tuple[float, float]

# Board is a two-dimensional slice of Cells
Board = list[list[Cell]]

# Insert your sum_cells() function here, along with any subroutines that you need.
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
