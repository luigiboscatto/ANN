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

x = [0.2092, 0.3841, 0.9207, 1.0888, 1.3235, 1.7637, 1.9784, 2.4597, 2.7707, 3.0136, 3.4241, 3.7192, 4.0227, 4.3534, 4.6229, 4.9955, 5.2808, 5.5327, 5.7574, 6.0936, 6.2981, 6.7422, 6.9153, 7.2403, 7.5568, 8.0978, 8.312, 8.6286, 8.9195, 9.1355, 9.4555, 9.9665]
y = [1.907, 2.392, 3.763, 4.1571, 4.6808, 5.8607, 6.4449, 7.7482, 8.794, 9.1752, 10.7195, 10.9724, 11.8448, 12.7074, 13.3277, 14.8925, 15.0053, 16.1299, 15.9331, 17.2538, 17.8446, 18.4788, 19.5225, 20.3336, 20.7587, 22.5305, 23.1677, 23.9293, 24.5909, 25.0961, 25.9741, 27.3255]

a0, a1 = best_poly(x, y, 1)

print(a0, ',', a1, ',')

def p(x, a0, a1):
  return a0 + a1 * x

values = [1.6175, 2.1647, 3.0434, 6.8943, 7.8736]

for x in values:
  print(p(x, a0, a1), ',')
