import numpy as np
import scipy.integrate as spi

def f(x):
    return x**2

def is_inside_integral_area(a, b, x, y):
    return y <= x ** 2

def monte_carlo_integration():
    num_experiments = 100
    avarage_integral = 0

    for _ in range(num_experiments):
        a = 2
        b = 4

        points = [(np.random.uniform(0, a), np.random.uniform(0, b)) for _ in range(15000)]
        inside_points = [point for point in points if is_inside_integral_area(a, b, point[0], point[1])]

        N = len(points)
        M = len(inside_points)

        integral = (M / N) * (a * b)
        avarage_integral += integral
    
    avarage_integral /= num_experiments
    print(f"Integral value with Monte Carlo algorithm: {avarage_integral}")

def integration_check():
    a = 0
    b = 2
    result, error = spi.quad(f, a, b)
    print("Integral with SciPy quad: ", result)

monte_carlo_integration()
integration_check()
