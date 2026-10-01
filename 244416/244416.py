def boards_equal(board1: list[list[bool]], board2: list[list[bool]]) -> bool:
    """
    Check if two Game of Life boards are exactly the same.

    Parameters:
        board1 (list[list[bool]]): The first Game of Life board.
        board2 (list[list[bool]]): The second Game of Life board.

    Returns:
        bool: True if the boards have the same dimensions and identical values 
              in every position, False otherwise.
    """
    if(len(board1)==0) and (len(board2)==0):
        return True


    if (len(board1)==len(board2))and(len(board1[0])==len(board2[0])):

        for i in range(len(board1)):
            for p in range(len(board1[i])):
                if not(board1[i][p]==board2[i][p]):
                    return False
        return True


    return False
