GameBoard = list[list[bool]]

def is_two_cycle(board: GameBoard) -> bool:
    """
    Determine whether a Game of Life configuration is a two-cycle oscillator.

    Input:
        board (GameBoard): A rectangular grid representing the initial Game of Life 
                           configuration, where True indicates a live cell and False 
                           indicates a dead cell.

    Output:
        bool: True if the configuration oscillates with a period of 2 
              (returns to its original state after two generations but is 
              not already stable), and False otherwise.
    """
    first_state=update_board(board)
    second_state=update_board(first_state)
    if first_state==board:
        return False
    elif board==second_state:
        return True
    return False
