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

x = [0.1448, 1.0988, 1.6927, 2.2582, 3.5448, 4.0154, 4.3267, 5.5671, 6.2355, 6.9429, 7.2499, 7.9433, 9.2653, 9.6083]
y = [5.3833, 4.8237, 4.4269, 4.1311, 3.6016, 3.5723, 3.4381, 3.8252, 4.0143, 3.9803, 4.7503, 4.7352, 5.6906, 6.3164]

a0, a1, a2 = best_poly(x, y, 2)

print(a0, ',', a1, ',', a2, ',')

def p(x, a0, a1, a2):
  return a0 + a1 * x + a2 * x ** 2

values = [2.585, 2.7725, 6.5754]

for x in values:
  print(p(x, a0, a1, a2), ',')
