from methods import *

'''
Em 16 de Maio de 2011 o ônibus espacial Endeavour realizou seu último voo (STS-134) em direção à ISS (International Space Station) com a missão de levar o AMS-2 (Espectômetro Magnético Alpha) e o ELC-3 à estação espacial.
'''

answer = []
x = []
y = []

lista = []
lista.append((0, 0))
lista.append((5, 108))
lista.append((10, 233))
lista.append((15, 359))
lista.append((20, 515))
lista.append((25, 671))
lista.append((30, 820))
lista.append((35, 972))
lista.append((40, 1094))
lista.append((45, 1204))
lista.append((50, 1325))
lista.append((55, 1457))
lista.append((60, 1627))
lista.append((65, 1823))
lista.append((70, 2051))
lista.append((75, 2318))
lista.append((80, 2603))
lista.append((85, 2901))
lista.append((90, 3201))

for i in range(len(lista)):
    x.append(lista[i][0] / 3600)
    y.append(lista[i][1])

answer.append(trapzPonto(x, y))
answer.append(simpsPonto(x, y))

print(*answer, sep=", ")