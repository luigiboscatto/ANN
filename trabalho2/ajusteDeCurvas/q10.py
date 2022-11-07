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

x = [-4.4522, -4.1644, -3.8427, -3.7979, -3.5841, -3.1989, -2.9946, -2.8633, -2.6288, -2.4475, -2.2838, -2.046, -1.695, -1.6022, -1.3373, -1.1533, -0.7888, -0.6485, -0.4013, -0.2893, 0.068, 0.2449, 0.5332, 0.6772, 0.9453, 1.1282, 1.3233, 1.5501, 1.7681, 2.0415, 2.1453, 2.4953, 2.6146, 2.8747, 3.0189, 3.3839, 3.5717, 3.7779, 3.976, 4.1333, 4.38]
y =  [-3.2537, -0.8939, 0.5557, 1.2402, 1.6315, 1.5773, 1.749, 1.0211, 1.0276, 0.5249, 0.6333, 0.0996, -1.2315, 0.3713, -0.3534, -0.8213, -0.9327, -0.5883, -0.0811, -0.4589, 0.0596, 0.3974, 0.5234, 0.5872, -1.1697, 1.3968, 0.5626, 0.5564, 0.4865, 0.0362, -0.3673, -1.039, -1.0674, -1.0858, -1.1593, -1.5206, -1.1487, -1.3723, -0.2096, 0.5653, 3.0324]

a0, a1, a2, a3, a4, a5 = best_poly(x, y, 5)

print(a0, ',', a1, ',', a2, ',', a3, ',', a4, ',', a5, ',')

def p(x, a0, a1, a2, a3, a4, a5):
  return a0 + a1 * x + a2 * x ** 2 + a3 * x ** 3 + a4 * x ** 4 + a5 * x ** 5

values = [-3.5975, -3.3524, -0.5212, -0.3461, 3.2791]

for x in values:
  print(p(x, a0, a1, a2, a3, a4, a5), ',')
