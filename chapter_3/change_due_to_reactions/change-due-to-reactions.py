import sys
import math

# Please do not remove package declarations because these are used by the autograder. If you need additional packages, then you may declare them above.


# Cell contains two attributes corresponding to
# the concentration of predator (0-th element) and prey (1-th element) in the cell
Cell = tuple[float, float]

# Board is a two-dimensional slice of Cells
Board = list[list[Cell]]

# Insert your change_due_to_reactions() function here, along with any subroutines that you need.
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
