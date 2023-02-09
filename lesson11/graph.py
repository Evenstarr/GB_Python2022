from sympy import *
from sympy.plotting import plot


def f(x):
    return x - 12 * x ** 4 * sin(cos(x)) - 18 * x ** 3 + 5 * x ** 2 + 10 * x - 30


def g(x):
    return 3 * x + 2


x = symbols('x', real=True)
plot(f(x), (x, -11, 0))

