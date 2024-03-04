def interpolate_newton(x, coefficients, x_value):
    result = coefficients[0]
    term = 1
    h = x[1] - x[0]
    s = (x_value - x[0]) / h
    alt_result = coefficients[0]
    alt_result_2 = coefficients[0] + s*h*coefficients[1] + s*(s - 1)*h**2*coefficients[2] + s*(s-1)*(s-2)*h**3*coefficients[3]


    for i in range(1, len(coefficients)):
        term *= (x_value - x[i - 1])
        result += coefficients[i] * term
        alt_result = coefficients[0] + s*h*coefficients[1]

    return alt_result