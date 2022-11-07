from methods import *

def func(x):
    return x**2 * math.exp(-x) * math.cos(x) + 1

h = 0.38943
x0 = 1.02683
orders = [4, 5, 6, 7, 8]


def F1(h):
    return (func(x0 + h) - func(x0)) / h

for j in orders:
    col_F1 = [F1(h/2**i) for i in range(j)]
    aprox = richardson(col_F1)
    print(f'{aprox}', end=", ")
print("")