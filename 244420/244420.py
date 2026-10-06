def state_histogram(board: list[list[int]]) -> list[int]:
    """
    Compute a histogram of state frequencies in a board.

    Input:
        board (list[list[int]]): A rectangular board of integer states.

    Output:
        list[int]: A histogram list where hist[s] is the count of cells in state s,
                   for s = 0..max_state(board).
    """
    hist=[0]*(max_state(board)+1)
    for i in range(len(board)):
        for p in range(len(board[0])):
            hist[board[i][p]]+=1


    return hist

def max_state(board):
    maxx=0
    for i in range(len(board)):
        for p in range(len(board[0])):
            if board[i][p]>maxx:
                maxx=board[i][p]
    return maxx
