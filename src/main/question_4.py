# src/main/question_4.py
import numpy as np

def hermite_polynomial_matrix(data):
    n = len(data)
    matrix = np.zeros((2 * n, 2 * n + 1))

    # Initialize the matrix with the given data
    matrix[:n, 0] = data[:, 0]
    matrix[:n, 1] = data[:, 1]
    matrix[:n, 2] = data[:, 2]

    # Populate the remaining columns using the divided difference method
    for i in range(1, 2 * n):
        for j in range(n - 1, i - 1, -1):
            matrix[j, i + 2] = (matrix[j, i + 1] - matrix[j - 1, i + 1]) / (matrix[j, 0] - matrix[j - i, 0])

    return matrix
