from methods import *

x = [0.0369, 1.4827, 2.3016, 3.2505, 3.7049, 4.2416, 5.7797, 5.8366, 7.4815, 8.2524, 8.8732, 9.4477]
y = [4.7485, 3.9066, 3.5558, 3.0821, 3.1663, 3.1125, 3.1949, 3.2828, 3.7469, 4.2242, 4.593, 5.0132]
values = [1.063, 1.7482, 5.5974]

matrizA = []
matrizB = []
listPol = []
matrizA, matrizB, listPol = best_poly(x, y, 2)
a0 = listPol[0]
a1 = listPol[1]
a2 = listPol[2]
# print(f'{a0}, {a1}, {a2}', end=', ')
print('Coefs:\n',f'{a0}, {a1}, {a2}', end=',')

def p(x, a0, a1, a2):
	return a0 + a1 * x + a2 * pow(x, 2)
print()
print('Values:')
for value in values:
    print(f'{p(value, a0, a1, a2)}', end=", ")
print("")
# Ordem: Matriz A, Coefs, Matriz B, Values

print("\n\nPARA INSERIR\n")
print(*matrizA, sep=", ", end=", ")
print(f'{a0}, {a1}, {a2}', end=', ')
print(*matrizB, sep=", ", end=", ")
for value in values:
    print(f'{p(value, a0, a1, a2)}', end=", ")
print("")