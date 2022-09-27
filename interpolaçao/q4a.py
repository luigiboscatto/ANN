from re import S
import numpy as np
from math import sqrt


def f(x):
    return np.sin(sqrt(1+np.tan(x)))


def poly(x, y):
    n = len(x) - 1
    A = []
    for xi in x:
        row = [1]
        for j in range(1, n + 1):
            row.append(xi**j)
        A.append(row)
    return np.linalg.solve(A, y)


def p(x, coefs):
    first = coefs[0]
    return first + sum([ai*x**j for j, ai in enumerate(coefs[1:], 1)])


if __name__ == '__main__':
    x = [2.68, 3.635, 4.447]
    y = []

    for i in x:
        y.append(f(i))

    np.set_printoptions(suppress=True)
    coefs = poly(x, y)
    print(coefs)
    print(abs(f(3.884) - p(3.884, coefs)))
    print(abs(f(7.971) - p(7.971, coefs)))
    print(abs(f(8.586) - p(8.586, coefs))) #pontos