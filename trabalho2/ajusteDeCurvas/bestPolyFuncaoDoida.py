from methods import *
import matplotlib.pyplot as plt
from math import *

#funções do tipo x = e^((y-b)/a)

x = [1.174, 2.101, 2.6848, 3.5679, 4.7284, 5.0791, 5.9655, 6.8215, 7.5463, 8.0089, 8.987, 9.8178]
y = [4.3062, 6.1571, 6.833, 7.6992, 8.5365, 8.7252, 9.182, 9.6372, 9.9979, 10.2877, 10.5436, 10.6881]
values = [2.0007, 4.874, 6.7976]

#linearização, transformando x em ln(x)

for i in range(0, len(x)):
    x[i] = log(x[i])

b, a = best_poly(x,y, 1) 

print('Coefs:\n',f'{a}, {b}', end=',')

def p(x, a, b):
	return a * log(x) + b

print()
print('Values:\n')
for value in values:
    print(f'{(p(value, a, b))}', end=", ")
print("")