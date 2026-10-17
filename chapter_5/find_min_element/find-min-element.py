# DistanceMatrix is a 2D list of floats
DistanceMatrix = list[list[float]]


# Insert your find_min_element() function here, along with any subroutines that you need.
def find_min_element(mtx: DistanceMatrix) -> tuple[int, int, float]:
    """
    Find the indices (i, j) of the smallest strictly upper-triangular entry.

    Args:
        mtx (DistanceMatrix): A square matrix with size >= 2.

    Returns:
        tuple[int, int, float]: (row_index, col_index, min_value) with col_index > row_index.

    Raises:
        ValueError: If the matrix is smaller than 2x2.
    """
    if len(mtx)<2 and len(mtx[0])<2:
        raise ValueError("matrix is smaller than 2x2")


    minn=mtx[0][1]
    stored_row=0
    stored_col=1
    for row in range(len(mtx)):
        for col in range(len(mtx[row])):
            if mtx[row][col]<minn and row!=col:
                minn=mtx[row][col]
                stored_col=col
                stored_row=row


    return (stored_row,stored_col,minn)
