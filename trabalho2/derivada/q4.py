from methods import *

def f(x):
    return math.sin(x)**3 - 3*math.sin(x)**2 + math.sin(x**2) + 4

k = 2 # ordem da derivada
n = 9 # número de pontos

x0 = -0.4891
x = [-0.7238, -0.5293, -0.4112, -0.2861]

y = [f(xi) for xi in x]

coeffs = coeffs_dif_fin(x0, x, k)
aprox = dif_fin(coeffs, y)

print('Coefs:')
for i in coeffs:
    print(i,',')
print('Aproximacao:')
print(f'{aprox}')