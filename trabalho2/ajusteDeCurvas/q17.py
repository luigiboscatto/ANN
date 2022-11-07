from methods import *
from math import *

x = [1.2525, 1.4961, 1.9934, 2.5475, 3.1092, 3.523, 4.1167, 4.5431, 4.9052, 5.103, 5.6158, 6.4001, 6.4807, 7.2536, 7.5596, 7.8358, 8.5469, 8.8179, 9.2731, 10.0166, 10.2865, 10.8939, 11.224, 11.5368, 11.8973, 12.3147, 12.9587, 13.4027, 14.0059, 14.4383, 14.9183, 15.1215, 15.7956, 16.2888, 16.7773, 17.1143, 17.4429, 17.8533, 18.3061, 19.0124, 19.303, 19.8516]
y = [1.8973, 2.0603, 2.3393, 2.5192, 2.7665, 2.8994, 3.0076, 3.1058, 3.1607, 3.2157, 3.2791, 3.3464, 3.3448, 3.444, 3.465, 3.4683, 3.4978, 3.5005, 3.5615, 3.6019, 3.6303, 3.6437, 3.6589, 3.6759, 3.6722, 3.6767, 3.7072, 3.736, 3.7155, 3.7406, 3.7423, 3.747, 3.7282, 3.7978, 3.8058, 3.732, 3.8091, 3.827, 3.8134, 3.8586, 3.8082, 3.8226]
values = [3.9827, 5.7241, 8.525, 10.2347, 15.6378]

#linearização, transformando y em 1/y e x em 1/x
for i in range(0, len(y)):
    y[i] = 1/y[i]

for i in range(0, len(x)):
    x[i] = 1/x[i]

matrizA = []
matrizB = []
listPol = []
matrizA, matrizB, listPol = best_poly(x, y, 1)
z, w = listPol

a = 1/z # a função te retorna um valor z = ln(a), então isola a e obtém a = exp(z)
b = a * w
print('Coefs:\n',f'{a}, {b}', end=', ')

def p(x, a, b):
	return a * (x/(x+b))

print()
print('Values:')
for value in values:
    print(f' {(p(value, a, b))}', end=", ")
print("")
print("\n\nPARA INSERIR\n")
print(f'{a}, {b}', end=', ')
for value in values:
    print(f'{(p(value, a, b))}', end=", ")
print("")