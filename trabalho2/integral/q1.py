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

intervalo = [-1.536, 1.806]
subintervalos = [4, 20, 41, 62, 92, 105, 217, 278, 697, 829, 1357, 5654]
for i in range(len(subintervalos)):
    r = trapz(f, intervalo[0], intervalo[1], subintervalos[i])
    print(r,',')