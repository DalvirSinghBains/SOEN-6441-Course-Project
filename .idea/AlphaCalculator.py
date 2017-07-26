from scipy.optimize import newton
import math
import PiApproximatorSecond

piObject = PiApproximatorSecond.PiApproximatorSecond()
piEstimate = piObject.piCalculator()


# math module of Python is used to calculate the values of sin(x) and cos(x) functions
def f(x):
    return (x - math.sin(x) - (piEstimate / 2))


def df(x):
    return (1 - math.cos(x))

    # newton's method from the SciPy package is used to calculate the value of alpha iteratively
    # the initial guess for the alpha is taken as 2
    # the initial guess is approximated from the intersection point of two graphs
    # y(x)=x-pi/2 and y[x]=sin(x)

alphaEstimateRadians = newton(f ,2, df, tol=1.48e-08, maxiter=50)
alphaEstimateDegrees = (alphaEstimateRadians * (180 / piEstimate))

