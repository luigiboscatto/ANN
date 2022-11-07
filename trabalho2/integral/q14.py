from methods import *

'''
A tabela a seguir mostra leituras do velocímetro de um carro, durante um período de 60.0 segundos, numa corrida na Daytona International Speedway, Flórida.
'''

answer = []
x = []
y = []

lista = []
lista.append((0.0, 257.52))
lista.append((5.0, 163.22))
lista.append((10.0, 198.1))
lista.append((15.0, 158.89))
lista.append((20.0, 125.45))
lista.append((25.0, 226.58))
lista.append((30.0, 102.59))
lista.append((35.0, 181.57))
lista.append((40.0, 133.62))
lista.append((45.0, 251.29))
lista.append((50.0, 289.81))
lista.append((55.0, 271.45))
lista.append((60.0, 209.24))

for i in range(len(lista)):
    x.append(lista[i][0] / 3600)
    y.append(lista[i][1])

answer.append(trapzPonto(x, y))
answer.append(simpsPonto(x, y))

print(*answer, sep=", ")