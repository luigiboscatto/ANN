from methods import *
from math import *

x = [0.528, 0.5765, 0.6499, 0.7344, 0.755, 0.8306, 0.9051, 0.9244, 0.9788, 1.0855, 1.1163, 1.2142, 1.2649, 1.3033, 1.3712, 1.4305, 1.4621, 1.5351, 1.603, 1.6372, 1.7159, 1.7871, 1.8422, 1.892, 1.9813, 2.0279, 2.061, 2.1105, 2.2228, 2.2832, 2.3228, 2.3649, 2.4632, 2.4653, 2.5711, 2.5999, 2.6778, 2.7472, 2.7657, 2.8409, 2.9372, 2.9487]
y = [0.3842, 0.5735, 0.7857, 0.9149, 1.1616, 1.6859, 1.8124, 2.3639, 1.5362, 3.4619, 5.7739, 5.9385, 6.5134, 7.6117, 8.653, 10.9987, 10.8513, 13.0801, 15.476, 16.5322, 20.4724, 22.9589, 25.8032, 28.8103, 34.2737, 38.2026, 39.3987, 43.2982, 52.5633, 58.0707, 62.1144, 66.1225, 78.9189, 78.4453, 93.0788, 94.6547, 106.2693, 116.4326, 118.2487, 132.9077, 150.9828, 151.9896]
values = [1.1117, 1.3384, 1.906, 2.2806, 2.3311]

#linearização, transformando y em ln(y) e x em ln(x)
for i in range(0, len(y)):
    y[i] = log(y[i])

for i in range(0, len(x)):
    x[i] = log(x[i])

matrizA = []
matrizB = []
listPol = []
matrizA, matrizB, listPol = best_poly(x, y, 1) 
z, b = listPol

a = exp(z) # a função te retorna um valor z = ln(a), então isola a e obtém a = exp(z)

print('Coefs:\n',f'{a}, {b}', end=',')

def p(x, a, b):
	return a * pow(x, b)

print()
print('Values:\n')
for value in values:
    print(f'{(p(value, a, b))}', end=", ")
print("")

print("\n\nPARA INSERIR\n")
print(f'{a}, {b}', end=', ')
for value in values:
    print(f'{(p(value, a, b))}', end=", ")
print("")