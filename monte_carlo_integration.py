import numpy as np
import scipy.integrate as spi

# calculate x^2 function results
def f(x):
    return x**2

def monte_carlo_integration():
    # Limits of integral x^2
    a = 0
    b = 2
    N = 1000 # number of random values for x

    x_values = np.zeros(N)

    # list of x values for evaluating the integral
    for i in range(len(x_values)):
        x_values[i] = np.random.uniform(a, b)

    # sum of calculated integral values
    function_sum = 0

    # calculate function sum
    for i in x_values:
        function_sum += f(i)

    integral = (b - a) / float(N) * function_sum
    print(f'Integral value is: {integral}')

def integration_check():
    a = 0
    b = 2
    result, error = spi.quad(f, a, b)
    print("Integral: ", result)

monte_carlo_integration()
integration_check()
