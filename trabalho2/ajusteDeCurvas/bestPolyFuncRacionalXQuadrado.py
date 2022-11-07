from re import X
from methods import *
import matplotlib.pyplot as plt
from math import *





x = [1.8454, 2.4544, 3.0986, 4.2592, 4.9097, 5.8262, 7.0155, 7.9802, 8.8846, 9.9222, 10.7682, 11.4343]
y = [1.6329, 2.2971, 2.7133, 3.4181, 3.5075, 3.9109, 4.1107, 4.2759, 4.3096, 4.4256, 4.4717, 4.4821]
values = [3.7225, 4.0218, 4.7645]

#linearização, transformando y em 1/y e x em 1/x**2
for i in range(0, len(y)):
    y[i] = 1/y[i]

for i in range(0, len(x)):
    x[i] = pow(1/x[i],2)

    

z, w = best_poly(x,y, 1) 

a = 1/z # a função te retorna um valor z = ln(a), então isola a e obtém a = exp(z)
b = a * w
print('Coefs:\n',f'{a}, {b}', end=',')

def p(x, a, b):
	return a * (x**2/(x**2+b))

print()
print('Values:\n')
for value in values:
    print(f'{(p(value, a, b))}', end=", ")
print("")
