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

x = [-4.3449, -3.7119, -2.9731, -2.5488, -1.9667, -1.6805, -0.7761, -0.3651, 0.0921, 0.6431, 1.5124, 2.1903, 2.5373, 3.0762, 3.4904, 4.1701]
y = [-2.0524, 1.0894, 0.8457, 0.2782, -0.1945, -0.3375, -0.2451, -0.1631, -0.1375, 0.132, 0.4442, -0.331, -0.3839, -1.1281, -0.9652, 1.0424]

a0, a1, a2, a3, a4, a5 = best_poly(x, y, 5)

print(a0, ',', a1, ',', a2, ',', a3, ',', a4, ',', a5, ',')

def p(x, a0, a1, a2, a3, a4, a5):
  return a0 + a1 * x + a2 * x ** 2 + a3 * x ** 3 + a4 * x ** 4 + a5 * x ** 5

values = [-4.1643, 1.6537, 1.9204]

for x in values:
  print(p(x, a0, a1, a2, a3, a4, a5), ',')
