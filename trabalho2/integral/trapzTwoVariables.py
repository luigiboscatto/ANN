from methods import *

'''
Use a regra dos trapézios para aproximar o valor da integral
'''

def f(x, y):
	# return math.cos(pow(x, 2)) * math.sin(pow(y, 2) * x) * math.exp(-math.pow(y, 2)) + 1
	return math.sqrt(math.exp((-x**2)*(y**2))+1)

intervalo1 = [-1.243, 1.741]
intervalo2 = [-1.784, 1.518]
n1 = 6
n2 = 8

# double_trapz(f, a: float, b: float, c: float, d: float, n1: int, n2: int) -> float:

print(double_trapz(f, intervalo1[0], intervalo1[1], intervalo2[0], intervalo2[1], n1, n2))