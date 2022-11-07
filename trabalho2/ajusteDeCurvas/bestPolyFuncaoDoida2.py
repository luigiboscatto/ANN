from methods import *
import matplotlib.pyplot as plt
from math import *

#funções do tipo y = ((a+sqrt(x))/b*sqrt(x))²



x = [0.9586, 1.8647, 2.7763, 3.542, 3.7145, 4.9872, 5.6227, 6.5357, 7.4222, 7.9729, 8.9424, 9.3401]
y = [15.1734, 8.9807, 6.5341, 5.5805, 5.2902, 4.3472, 4.0019, 3.6629, 3.3982, 3.2452, 3.0023, 3.0516]
values = [1.3654, 3.2668, 7.262]

#linearização, transformando x em sqrt(x)

for i in range(0, len(x)):
    x[i] = 1/sqrt(x[i])

for i in range(0, len(y)):
    y[i] = sqrt(y[i])

    

w, z = best_poly(x,y, 1) 

b = 1/w
a = z*b


print('Coefs:\n',f'{a}, {b}', end=',')

def p(x, a, b):
	return pow((a+sqrt(x))/(b*sqrt(x)),2)

print()
print('Values:\n')
for value in values:
    print(f'{(p(value, a, b))}', end=", ")
print("")