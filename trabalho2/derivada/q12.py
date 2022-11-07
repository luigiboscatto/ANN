from methods import *

def func(x):
    return x**2 * math.tan(math.sin(x/math.pi))

h = 0.42766
x0 = -1.91225
orders = [2, 3, 4, 5, 6]

def F1(h):
    return (func(x0 + h) - func(x0)) / h

for j in orders:
    col_F1 = [F1(h/2**i) for i in range(j)]
    aprox = richardson(col_F1)
    print(f'{aprox}', end=", ")
print("")