# src/main/question_2.py
from numpy import zeros

def newtdd(x, y):
    n = len(x)
    v = zeros((n, n))

    # Fill in first column with y values
    for j in range(n):
        v[j, 0] = y[j]
    for i in range(1, n):  # For column i,
        for j in range(n - i):  # 1:n+1-i        # fill in column from top to bottom
            v[j, i] = (v[j + 1, i - 1] - v[j, i - 1]) / (x[j + i] - x[j])

    # Read along top of triangle for coefficients
    c = v[0, :].copy()
    return c
