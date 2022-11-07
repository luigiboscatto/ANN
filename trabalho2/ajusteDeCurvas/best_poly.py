from operator import le
import numpy as np

def best_poly(x, y, k):
  n = len(x)
  if n <= k:
    raise ValueError('O numero de pontos deve ser maior que o grau k do polinomio')

  somas = {}
  somas[0] = n
  for n in range(1, 2 * k + 1):
    somas[n] = sum(xi ** n for xi in x)

  A = []
  B = []
  for i in range(k + 1):
    row = []
    for j in range(k + 1):
      row.append(somas[i + j])
    
    A.append(row)
    
    if i == 0:
      B.append(sum(y))
    else:
      B.append(sum(xi ** i * yi for xi, yi in zip(x, y)))

  return np.linalg.solve(A, B)

x = [0.0242, 1.0304, 2.4941, 2.8465, 4.0349, 4.5887, 5.0764, 6.0015, 7.2343, 7.6473, 8.8595, 9.6744]
y = [3.6639, 5.6968, 8.1634, 9.4005, 11.5632, 12.729, 13.6911, 15.5534, 18.2956, 19.0611, 21.557, 23.1773]

a0, a1 = best_poly(x, y, 1)

print(f'{a0=} e {a1=}')

def p(x, a0, a1):
  return a0 + a1 * x

values = [0.5547, 3.0291, 5.9454]

for x in values:
  print(p(x, a0, a1), ',')
