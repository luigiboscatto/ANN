from methods import *

def f(x):
    return math.sin(math.cos(math.exp(-x)))

k = 1 # ordem da derivada
n = 5 # número de pontos

x0 = -0.6005
x = [-0.7759, -0.6686, -0.5535, -0.5444, -0.3975]

y = [f(xi) for xi in x]

coeffs = coeffs_dif_fin(x0, x, k)
aprox = dif_fin(coeffs, y)

print('Coefs:')
for i in coeffs:
    print(i,',')
print('Aproximacao:')
print(f'{aprox}')