# src/main/assignment_2.py
from src.main import question_1, question_2, question_3, question_4, question_5
import numpy as np

def main():
    # Example data points for question 1
    x_list_q1 = [3.6, 3.8, 3.9]
    y_list_q1 = [1.675, 1.436, 1.318]
    x_input_q1 = 3.7

    # Example data points for question 2
    x_list_q2 = [7.2, 7.4, 7.5, 7.6]
    y_list_q2 = [23.5492, 25.3913, 26.8224, 27.4589]

    data_q4 = np.array([[3.6, 1.675, -1.195],
                        [3.8, 1.436, -1.188],
                        [3.9, 1.318, -1.182]])

    # Example data points for question 5
    data_q5 = {'x': [2, 5, 8, 10], 'y': [3, 5, 7, 9]}

    # Call functions from question_1.py
    result_q1, full_table_q1 = question_1.neville_copy(x_input_q1, x_list_q1, y_list_q1)

    print(f"Q1. The approximated value for f(3.7) using Neville's Method is: {result_q1}")
    print("Full table: ")
    for row in full_table_q1:
        print(row)

    # Call function from question_2.py
    interpolant_q2 = question_2.newtdd(x_list_q2, y_list_q2)
    print("\nQ2. Interpolant coefficients for Question 2:", interpolant_q2)

    #Call function from question_3.py
    # Approximate f(7.3) using the formula

    x_value = 7.3

    approximation = question_3.interpolate_newton(x_list_q2, interpolant_q2, x_value)

    print("\nQ3. Approximation of f(7.3):", approximation)

    # Call function from question_4.py
    result_matrix_q4 = question_4.hermite_polynomial_matrix(data_q4)
    print("\nQ4. Hermite polynomial approximation matrix for Question 4:")
    for row in result_matrix_q4:
        print('[', end=' ')
        for val in row:
            print(f'{val:.7f}', end=' ')
        print(']')

    # Call function from question_5.py
    A_q5, b_q5, x_q5 = question_5.solve_cubic_spline(data_q5)
    print("\nQ5. Matrix A for Question 5:")
    print(A_q5)
    print("\nVector b for Question 5:")
    print(b_q5)
    print("\nVector x for Question 5:")
    print(x_q5)




if __name__ == "__main__":
    main()




