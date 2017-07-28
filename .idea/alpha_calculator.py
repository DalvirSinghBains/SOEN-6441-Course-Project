"""Contains a module called pi_approximator that provides the approximate value of pi.Contains an external module called scipy.optimize.newton."""
import math

from scipy.optimize import newton

import pi_approximator

piObject = pi_approximator.PiApproximator()
piEstimate = piObject.pi_calculator()


# math module of Python is used to calculate the values of sin(x) and cos(x) functions
def f(x):
    return (x - math.sin(x) - (piEstimate / 2))


def df(x):
    return (1 - math.cos(x))

    # Newton's method from the SciPy package(scipy.optimize.newton) is used to calculate the value of alpha iteratively
    # the initial guess for the alpha is taken as 2
    # the initial guess is approximated from the intersection point of two graphs
    # y(x)=x-pi/2 and y[x]=sin(x)
    # Error tolerance is taken as 1.48e-08
    # Maximum iterations allowed in the loop are 50

alphaEstimateRadians = newton(f ,2, df, tol=1.48e-08, maxiter=50) #Newton's method shows the reuse of code from external Python libraries



