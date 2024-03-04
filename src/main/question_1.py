# src/main/question_1.py

def neville_copy(x, x_list, y_list):
    n = len(x_list)

    Q = [[0] * n for _ in range(n)]

    for i in range(n):
        Q[i][0] = y_list[i]

    for i in range(1, n):
        for j in range(1, i + 1):
            Q[i][j] = ((x - x_list[i - j]) * Q[i][j - 1] - (x - x_list[i]) * Q[i - 1][j - 1]) / (
                    x_list[i] - x_list[i - j])

    result = Q[n - 1][n - 1]
    return result, Q
