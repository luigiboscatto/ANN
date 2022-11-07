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

x = [-4.2833, -3.6579, -2.5231, -2.115, -1.3464, -0.3476, 1.2242, 1.856, 2.3125, 3.47, 4.2979]
y =  [4.7659, 6.6047, 6.3717, 6.9853, 6.4024, 5.3921, 5.0943, 4.7961, 5.0615, 5.4937, 6.7579]

a0, a1, a2, a3 = best_poly(x, y, 3)

print(a0, ',', a1, ',', a2, ',', a3, ',')

def p(x, a0, a1, a2, a3):
  return a0 + a1 * x + a2 * x ** 2 + a3 * x ** 3

values = [-2.7819, -0.8839, 0.6659]

for x in values:
  print(p(x, a0, a1, a2, a3), ',')
