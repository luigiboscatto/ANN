from methods import *
import matplotlib.pyplot as plt
from math import *
#funcoes do tipo y = e^x
x = [0.0155, 0.1048, 0.1595, 0.201, 0.2247, 0.3048, 0.3593, 0.4174, 0.4726, 0.5524, 0.5581, 0.6612, 0.7, 0.7595, 0.8268, 0.8468, 0.9402, 0.9869, 1.0259, 1.0802, 1.1263, 1.1895, 1.2621, 1.3125, 1.3401, 1.4296, 1.4552, 1.5046, 1.5621, 1.6579, 1.6712, 1.7339, 1.7999, 1.8636, 1.9333, 1.9763]
y = [4.9171, 5.0459, 5.5306, 6.17, 5.7266, 6.115, 7.0471, 7.0253, 8.0151, 9.5799, 8.909, 9.8914, 10.4975, 12.722, 11.817, 12.2284, 13.5072, 14.7, 16.2714, 15.8203, 18.5838, 18.3522, 19.9496, 23.3829, 21.5052, 24.1953, 23.8871, 26.8771, 28.3502, 31.4961, 30.9157, 33.1045, 35.3646, 40.5673, 41.2545, 44.7927]
values = [1.0629, 1.0777, 1.148, 1.1707, 1.763]

#linearização, transformando y em ln(y)
for i in range(0, len(y)):
    y[i] = log(y[i])
    
z, b = best_poly(x,y, 1) 

a = exp(z) # a função te retorna um valor z = ln(a), então isola a e obtém a = exp(z)
print('Coefs:\n',f'{a}, {b}', end=',')

def p(x, a, b):
	return a * exp(b*x) 

print()
print('Values:\n')
for value in values:
    print(f'{(p(value, a, b))}', end=", ")
print("")
