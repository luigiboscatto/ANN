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

x = [-4.3843, -3.9503, -2.9606, -2.6519, -1.5716, -0.9595, -0.587, 0.7287, 1.1062, 2.0997, 2.7061, 3.6442, 4.341, 4.6848, 5.4906]
y = [-1.8008, -0.2175, 3.8726, 1.7538, 0.7522, 0.0856, -0.7892, -0.5172, 0.1911, 1.63, 2.846, 3.6719, 2.9889, 1.6734, -3.9122]

a0, a1, a2, a3, a4 = best_poly(x, y, 4)

print(a0, ',', a1, ',', a2, ',', a3, ',', a4, ',')

def p(x, a0, a1, a2, a3, a4):
  return a0 + a1 * x + a2 * x ** 2 + a3 * x ** 3 + a4 * x ** 4

values = [-4.0833, -0.7929, 5.41]

for x in values:
  print(p(x, a0, a1, a2, a3, a4), ',')
