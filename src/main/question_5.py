# src/main/question_5.py
import numpy as np

def solve_cubic_spline(data):
    # Set a values to y values
    a = np.array(data['y'])

    # Compute the hi values
    h = np.diff(data['x'])

    # Construct matrix A
    A = np.zeros((4, 4))
    A[0, 0] = 1
    A[1, 0] = h[0]
    A[1, 1] = 2 * (h[0] + h[1])
    A[1, 2] = h[1]
    A[2, 1] = h[1]
    A[2, 2] = 2 * (h[1] + h[2])
    A[2, 3] = h[2]
    A[3, 3] = 1

    # Construct vector b
    b = np.zeros((4, 1))
    b[1, 0] = 3 * (a[2] - a[1]) / h[1] - 3 * (a[1] - a[0]) / h[0]
    b[2, 0] = 3 * (a[3] - a[2]) / h[2] - 3 * (a[2] - a[1]) / h[1]

    # Solve for x
    x = np.linalg.solve(A, b)

    return A, b, x
