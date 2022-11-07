from methods import *
import matplotlib.pyplot as plt
from math import *


#Para linearizarmos a função, precisamos chegar em ln(y) - ln(x) = ln(a) + b * x



x = [0.3048, 0.421, 0.6672, 0.9169, 1.2913, 1.4127, 1.6568, 1.8352, 2.1981, 2.4761, 2.6822, 2.937, 2.9982, 3.3118, 3.4704, 3.846, 3.9574, 4.2083, 4.5713, 4.7713, 4.9078, 5.2877, 5.3276, 5.5782, 5.9921, 6.0871, 6.3769, 6.619, 6.9251, 7.1124, 7.2584, 7.4701, 7.7418, 7.9538, 8.3091, 8.5377, 8.7709, 8.8929, 9.0962, 9.3889, 9.7481, 9.8248]
y = [1.1939, 1.5404, 2.1301, 2.6229, 3.1101, 3.2929, 3.5627, 3.4772, 3.526, 3.498, 3.4926, 3.4538, 3.384, 3.2436, 3.1348, 2.9292, 2.8828, 2.7669, 2.5989, 2.4272, 2.3575, 2.2689, 2.1067, 2.0758, 1.734, 1.7303, 1.5996, 1.5306, 1.3579, 1.2967, 1.2131, 1.1111, 1.1044, 0.9738, 0.8639, 0.8272, 0.7584, 0.8109, 0.6622, 0.6154, 0.5569, 0.5081]
values = [1.0246, 2.7351, 4.1971, 5.6274, 7.2795]

logxy = list()


#linearização, obtendo ln(y) - ln(x), isso é o que vai entrar no lugar de y no best_poly
for i in range(0, len(x)):
    logxy.append(log(y[i]) - log(x[i]))
    

z, b = best_poly(x,logxy, 1) 

a = exp(z) # a função te retorna um valor z = ln(a), então isola a e obtém a = exp(z)

print('Coefs:\n',f'{a}, {b}', end=',')

def p(x, a, b):
	return a * x * exp(b*x)

print()
print('Values:\n')
for value in values:
    print(f'{(p(value, a, b))}', end=", ")
print("")
