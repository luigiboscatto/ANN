import math
from numpy import double

# Usado para aproximar o valor de uma integral
def trapz(f, a, b, n):
    h = (b-a) / n
    soma = 0
    for k in range(1, n):
        soma += f(a + k*h)
    soma *= 2
    soma += (f(a) + f(b))
    return (h/2) * soma


def f(x):
    return math.sin(x/math.sqrt(x**2 + 1)) + 1

intervalo = [-1.405, 1.6]
subintervalos = [5, 21, 25, 53, 79, 143, 198, 422, 678, 860, 4490, 7355]
for i in range(len(subintervalos)):
    r = trapz(f, intervalo[0], intervalo[1], subintervalos[i])
    print(r,',')