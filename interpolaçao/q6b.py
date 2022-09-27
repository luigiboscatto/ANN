from cmath import sin
import numpy as np



def f(x):
    return np.sin(x)**3- 3*np.sin(x)**2+np.sin(pow(x,2)) + 4


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
    x = [-2.945, -2.237, 0.517, 2.073, 2.69]
    y = []

    for i in x:
        y.append(f(i))

    np.set_printoptions(suppress=True)
    coefs = poly(x, y)
    print(coefs)
print(abs(f(-3.008) - p(-3.008, coefs)))
print(abs(f(2.568) - p(2.568, coefs)))
print(abs(f(2.907) - p(2.907, coefs))) #pontos