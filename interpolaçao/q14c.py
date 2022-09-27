import numpy as np
import math 

def dif_div(x, y):
    Y = [yi for yi in y]
    coefs = [y[0]]
    for j in range(len(x)-1):
        for i in range(len(x)-1-j):
            number = Y[i+1]-Y[i]
            denom = x[i+1+j]-x[i]
            div = number/denom
            Y[i] = div
        coefs.append(Y[0])
    return coefs


def poly(t, x, coefs):
    val = 0
    for i in range(len(coefs)):
        prod = 1
        for j in range(i):
            prod *= (t-x[j])
        val += coefs[i]*prod
    return val


def build_func(x, coefs):
    def temp(t):
        return poly(t, x, coefs)
    return temp


if __name__ == '__main__':
    x = [1.512, 1.763, 1.948, 2.289, 2.459, 2.658, 2.873, 3.114, 3.512, 3.695, 3.875, 4.17, 4.314, 4.605, 4.87]
    y = []

    def f(x):
        #return np.cos(np.sin(np.log(x**2)))
        return np.cos(x+math.sqrt(np.log(pow(x,2))))

    for i in x:
        y.append(f(i))

    coefs = dif_div(x, y)
    p = build_func(x, coefs)
    print(coefs)