from methods import *
import matplotlib.pyplot as plt
from math import *


x = [0.0195, 0.0996, 0.1205, 0.2131, 0.2645, 0.3051, 0.3582, 0.439, 0.4747, 0.5052, 0.6074, 0.6455, 0.6693, 0.7283, 0.7987, 0.8501, 0.9407, 0.9702, 1.0462, 1.0754, 1.1505, 1.2197, 1.2575, 1.3027, 1.367, 1.396, 1.4759, 1.5131, 1.5598, 1.6313, 1.6786, 1.7295, 1.8309, 1.8867, 1.9126, 1.9565]
y = [6.8768, 4.2902, 4.4642, 4.9823, 4.993, 6.4301, 7.5472, 8.3771, 8.8608, 5.1754, 9.5316, 9.6711, 9.8065, 12.3241, 13.1973, 11.232, 13.1189, 16.0689, 17.3175, 17.9982, 18.7237, 21.4215, 21.4475, 23.4115, 25.1334, 28.5328, 29.611, 31.2965, 33.9717, 37.3332, 39.6432, 42.3863, 49.389, 52.9091, 54.5507, 58.1737]
values = [0.142, 0.3215, 0.8594, 1.1532, 1.5543]


#linearização, transformando y em ln(y)
for i in range(0, len(y)):
    y[i] = log(y[i])

    

z, w = best_poly(x,y, 1) 

a = exp(z) # a função te retorna um valor z = ln(a), então isola a e obtém a = exp(z)
b = w/log(2) # a função te retorna um valor w = b * ln(2), então isola b e obtém b = w/log(2)
print('Coefs:\n',f'{a}, {b}', end=',')

def p(x, a, b):
	return a * pow(2, b*x) 

print()
print('Values:\n')
for value in values:
    print(f'{(p(value, a, b))}', end=", ")
print("")
