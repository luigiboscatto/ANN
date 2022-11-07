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

x = [0.0042, 0.5326, 0.7632, 0.9985, 1.3267, 1.6634, 1.9168, 2.053, 2.3415, 2.5147, 2.81, 3.3149, 3.5467, 3.8744, 4.1132, 4.3628, 4.6569, 4.765, 5.0527, 5.4054, 5.8238, 5.9594, 6.1971, 6.5554, 6.9046, 7.2167, 7.3266, 7.5709, 7.8138, 8.2501, 8.5691, 8.8255, 9.0751, 9.1926, 9.5567, 9.9184]
y = [5.6868, 5.3169, 5.166, 4.8402, 4.7377, 4.6695, 4.5307, 4.4068, 4.3679, 4.2367, 4.1372, 4.2957, 4.0014, 3.9545, 3.8954, 3.9697, 3.8398, 3.8674, 3.9881, 3.7901, 3.9894, 3.9954, 3.6041, 4.2463, 4.2727, 4.4148, 4.4473, 4.3652, 4.6965, 4.9036, 5.2735, 5.2319, 5.4631, 5.684, 5.7954, 6.1349]

a0, a1, a2 = best_poly(x, y, 2)

print(a0, ',', a1, ',', a2, ',')

def p(x, a0, a1, a2):
  return a0 + a1 * x + a2 * x ** 2

values = [0.5462, 1.1826, 4.6473, 6.0453, 7.554]

for x in values:
  print(p(x, a0, a1, a2), ',')
