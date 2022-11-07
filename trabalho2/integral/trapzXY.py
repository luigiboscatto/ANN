import math
from numpy import double

# Usado para aproximar o valor de uma integral


def trapz(g, a1, b1, a2, b2, n1, n2):
    h1 = (b1-a1) / n1
    h2 = (b2-a2)/n2
    r = 0
    for k1 in range(0, n1+1):
        soma = 0
        for k2 in range(1, n2):
            soma += g(a1 + k1*h1, a2+k2*h2)
        soma *= 2
        soma += (g(a1+k1*h1, a2) + g(a1+k1*h1, b2))
        if((k1!=0)&(k1!=n1)):
            r += (h2) * soma
        else:
            r+=h2/2*soma
    r = h1/2*r
    return r


def g(x, y):
    return math.sqrt(math.e**(-x**2*y**2)+1)


intervalo1 = [-1.686, 1.656]
intervalo2 = [-1.367, 1.964]
n1 = 256
n2 = 128
print(trapz(g,intervalo1[0],intervalo1[1],intervalo2[0],intervalo2[1],n1,n2))
