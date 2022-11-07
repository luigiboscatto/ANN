from methods import *

'''
Óleo vaza de um tanque a uma taxa de r(t) litros por hora. A taxa decresce à medida que o tempo passa, conforme mostrado na tabela a seguir.
'''

answer = []
x = []
y = []

lista = []
lista.append((0.0, 9.94))
lista.append((0.75, 9.24))
lista.append((1.5, 8.87))
lista.append((2.25, 8.42))
lista.append((3.0, 8.08))
lista.append((3.75, 7.86))
lista.append((4.5, 7.44))
lista.append((5.25, 6.78))
lista.append((6.0, 6.43))
lista.append((6.75, 5.93))
lista.append((7.5, 5.82))
lista.append((8.25, 5.42))
lista.append((9.0, 4.94))
lista.append((9.75, 4.29))
lista.append((10.5, 3.93))
lista.append((11.25, 3.73))
lista.append((12.0, 3.15))

for i in range(len(lista)):
    x.append(lista[i][0])
    y.append(lista[i][1])

answer.append(trapzPonto(x, y))
answer.append(simpsPonto(x, y))

print(*answer, sep=", ")