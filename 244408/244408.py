def diagonal_sum(matrix: list[list[int]]) -> int:
    """
    Compute the sum of the main diagonal entries in a square matrix.

    Parameters:
        matrix (list[list[int]]): A square integer matrix.

    Returns:
        int: The sum of the numbers on the main diagonal (top-left to bottom-right).
    """
    sum=0
    for i in range(len(matrix)):
        sum=sum+matrix[i][i]

    return sum
