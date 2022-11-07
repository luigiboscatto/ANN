from methods import *

def f(x):
    return math.sin(math.sqrt(math.pi + x**2))

k = 4 # ordem da derivada
n = 8 # número de pontos

x0 = 3.4627
x = [3.2294, 3.3348, 3.3645, 3.4073, 3.482, 3.5516, 3.6464, 3.6979]

y = [f(xi) for xi in x]

coeffs = coeffs_dif_fin(x0, x, k)
aprox = dif_fin(coeffs, y)

print('Coefs:')
for i in coeffs:
    print(i,',')
print('Aproximacao:')
print(f'{aprox}')