import numpy as np
from math import sqrt
from math import exp, cos, sin



"""
This method solves the system to get the particular solutions for this particular case of the forced harmonic oscillator.
Since we make use of the fact that the evaluation of u(t) at 0 has to equal 0, and the evaluation of u'(t) has to equal 
the velocity at which the bicycle impacts the surface from a certain height, the expressions are greatly simplified
"""


def check_repeated(func):
    def inner(*args,**kwargs):
        results = args[0]
        if results[0] == results[1]:
            # flag for repeated roots passed so that it is handled in the appropriate separate case in the solver
            sol = func(*args, True,** kwargs)
        else:
            sol = func(*args, **kwargs)
        return sol
    return inner


@check_repeated
def solve(results: tuple, height: float, particular: float, *args) -> list:
    # results -> result from solving characteristic polynomial
    # height -> height from which the fall is considered
    # particular -> value of the particular solution

    velocity = sqrt(2 * 9.8 * height)
    b = np.array([-particular, -velocity])
    if len(args) == 0:
        # depending on the whether the results are real or not the resulting system to be solved will be different
        if results[0].imag == 0:
            # real distinct roots
            A = np.array([[1,1],[results[0].real, results[1].real]])
            solution = np.linalg.solve(A,b)
            return solution
        else:
            # complex roots of the characteristic polynomial
            A = np.array([[1,0],[results[0], 1]])
            solution = np.linalg.solve(A,b)
            return solution
    else:
        # double real roots
        D = (-velocity + particular*(results[0].real))
        return [-particular, D]




