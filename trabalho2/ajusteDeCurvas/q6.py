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

x = [-4.9651, -4.4942, -4.2706, -3.9941, -3.7122, -3.3605, -3.1876, -2.6606, -2.5382, -2.0919, -2.0478, -1.7083, -1.3165, -0.9258, -0.6448, -0.4633, -0.1748, 0.0614, 0.4668, 0.6467, 1.0567, 1.2201, 1.498, 2.0443, 2.0908, 2.3785, 2.8712, 3.1582, 3.2567, 3.7682, 3.9212, 4.1353, 4.6987, 4.9183]
y = [2.4494, 4.9352, 3.9013, 5.0677, 5.7014, 6.3937, 6.565, 7.0759, 6.852, 6.8517, 6.8192, 6.9572, 6.9942, 6.6924, 6.5616, 6.0789, 5.4282, 5.7322, 5.8609, 5.3496, 5.0053, 5.3057, 5.8192, 4.7851, 4.5638, 4.269, 5.2318, 5.337, 5.5182, 6.2277, 6.5108, 6.7626, 8.6003, 8.24]

a0, a1, a2, a3 = best_poly(x, y, 3)

print(a0, ',', a1, ',', a2, ',', a3, ',')

def p(x, a0, a1, a2, a3):
  return a0 + a1 * x + a2 * x ** 2 + a3 * x ** 3

values = [-2.8201, -1.9439, 1.0616, 2.4633, 3.9542]

for x in values:
  print(p(x, a0, a1, a2, a3), ',')
