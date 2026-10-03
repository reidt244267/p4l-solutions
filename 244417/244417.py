def change_mask(board: list[list[bool]]) -> list[list[bool]]:
    """
    Given a Game of Life board, return a mask grid of the same size whose entries
    are True exactly at cells that will change state in the next generation.
    Args:
        board (GameBoard = list[list[bool]] ): A rectangular Game of Life board.

    Returns:
        list[list[bool]]: A grid of the same dimensions, where mask[r][c] is True
                          if and only if update_cell(board, r, c) != board[r][c].
    """
    rows=len(board)
    cols=len(board[0])
    final_board=[[False] * cols for _ in range(rows)]

    for p in range(rows):
        for i in range(cols):
            if board[p][i]!=update_cell(board,p,i):
                final_board[p][i]=True



    return final_board
