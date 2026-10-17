
# DistanceMatrix is a 2D list of floats
DistanceMatrix = list[list[float]]


# Insert your delete_row_col() function here, along with any subroutines that you need.
def delete_row_col(mtx: DistanceMatrix, row: int, col: int) -> DistanceMatrix:
    """
    Delete two rows and two columns (row/col) from the matrix.

    This is used after appending the new merged cluster at the end.

    Args:
        mtx (DistanceMatrix): The distance matrix.
        row (int): The first row/column index to delete (row < col).
        col (int): The second row/column index to delete.

    Returns:
        DistanceMatrix: The matrix with the specified rows/columns removed.
    """
    new_mat=[[0.0 for _ in range(len(mtx)-2)] for _ in range(len(mtx[0])-2)]
    
    row_count=0
    col_count=0

    for rrow in range(len(mtx)):
        if rrow!=row and rrow!=col:
            for ccol in range(len(mtx[row])):
                if ccol!=row and ccol!=col:
                    new_mat[row_count][col_count]=mtx[rrow][ccol]

                    col_count+=1
            row_count+=1
            col_count=0

    return new_mat





