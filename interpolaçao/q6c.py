import numpy as np


def f(x):
    return (np.cos(x)**3)+(2*np.cos(x)**2)+1


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
    x = [-2.857, -1.721, -1.216, -0.132, 0.751, 1.796, 2.142, 3.583, 3.801]
    y = []

    for i in x:
        y.append(f(i))

    np.set_printoptions(suppress=True)
    coefs = poly(x, y)
    print(coefs)

print(abs(f(-1.302) - p(-1.302, coefs)))
print(abs(f(-1.235) - p(-1.235, coefs)))
print(abs(f(-0.08) - p(-0.08, coefs)))
print(abs(f(0.332) - p(0.332, coefs)))
print(abs(f(0.721) - p( 0.721, coefs)))#pontos