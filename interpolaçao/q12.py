def dif_div(x, y):
    num = len(x)
    Y = [yi for yi in y]
    coefs = [y[0]]
    for j in range(num -1):
        for i in range(num - 1 - j):
            numerador = Y[i + 1] - Y[i]
            denominador = x[i + 1 + j] - x[i]
            div = numerador / denominador
            Y[i] = div
        coefs.append(Y[0])
    return coefs

def poly(t, x, coefs):
    val = 0
    num = len(coefs)
    for i in range(num):
        prod = 1
        for j in range(i):
            prod *= (t - x[j])
        val += coefs[i] * prod
    return val

def build_func(x, coefs):
    def temp(t):
        return poly(t, x, coefs)
    return temp


if __name__ == '__main__':

    #ex
    x = [1.76, 2.2, 2.706, 3.033, 3.846, 4.283, 4.793]
    y = [-0.95, -0.951, -0.561, -0.189, 0.7, 0.957, 0.961]
    coefs = dif_div(x, y)

    #polinomio interpolador da lista de pontos
    p = build_func(x, coefs)

    print(coefs)

    #print(p(1), p(3), p(3), p(4))
   # print(f'{p(0.97244)}')


    #visu
    #import matplotlib.pyplot as plt
    #import numpy as np

    #t = np.linspace(min(x), max(x), 100)
    #pt = [p(ti) for ti in t]

    #plt.scatter(x, y)
    #plt.plot(t, pt)

    #plt.savefig('dif_div.png')