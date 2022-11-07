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

x = [-4.9701, -4.5259, -4.2726, -4.0104, -3.6891, -3.4866, -3.1737, -2.6867, -2.6263, -2.3306, -1.9572, -1.5515, -1.2952, -1.0515, -0.7607, -0.4885, -0.3647, 0.1109, 0.4953, 0.507, 0.8259, 1.098, 1.6033, 1.6712, 2.0087, 2.3986, 2.7524, 2.938, 3.2794, 3.4666, 3.736, 4.2464, 4.2962, 4.576, 5.118, 5.313, 5.6257, 5.7445]
y = [-6.8097, -2.7224, -2.0236, 0.7066, 0.425, 1.3164, 1.7971, 2.0392, 1.7387, 1.6267, 0.2972, 0.5974, 0.4499, 0.2508, 0.7348, -0.6649, -0.6385, -0.8415, -0.3048, -0.103, -1.1748, -0.825, 1.0456, 0.0123, 0.6553, 2.1298, 2.4955, 3.3547, 3.4197, 3.6801, 4.2702, 2.9077, 2.8177, 2.3354, -0.6319, -2.5647, -6.0666, -6.9591]

a0, a1, a2, a3, a4 = best_poly(x, y, 4)

print(a0, ',', a1, ',', a2, ',', a3, ',', a4, ',')

def p(x, a0, a1, a2, a3, a4):
  return a0 + a1 * x + a2 * x ** 2 + a3 * x ** 3 + a4 * x ** 4

values = [-1.4309, 0.2765, 3.2384, 3.2938, 4.6249]

for x in values:
  print(p(x, a0, a1, a2, a3, a4), ',')
