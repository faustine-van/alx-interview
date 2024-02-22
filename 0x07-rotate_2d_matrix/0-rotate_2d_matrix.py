#!/usr/bin/python3
"""2D matrix, rotate it 90 degrees
   clockwise
"""


def rotate_2d_matrix(matrix):
    """Rotate 2d matrix 90 degrees
    Args:
        matrix: 2d
    Returns:
        nothing
    """
    rows = len(matrix)
    cols = len(matrix[0])
    matrix.reverse()
    # create matrix
    for i in range(rows):
        for j in range(i, cols):
            # Assign matrix element to the transposed position
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
