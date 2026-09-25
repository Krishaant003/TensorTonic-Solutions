import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # Write code here
    row = len(A)
    column = len(A[0])
    B = []
    for i in range(column):
        rows = []
        for j in range(row):
            rows.append(A[j][i])
        B.append(rows)
    return np.array(B)
    pass
