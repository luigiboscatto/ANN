import math

def trapz(f, a, b, n):
    h = (b - a) / n
    soma = 0
    for k in range(1, n):
        soma += f(a + k * h)
    soma *= 2
    soma += f(a)
    soma += f(b)
    soma *= (h/2.0)
    print(f'Area aproximadamente: {soma}')

def f(x):
    return math.sqrt(math.sin(math.cos(math.log(x**2 + 1) + 2) + 3) + 4)

def trapzPonto(x, y):
    tam = len(x) - 1
    somas = 0
    for i in range(tam):
        h = x[i+1] - x[i]
        somas += (h/2) * (y[i] + y[i+1])
    print(f'Area = {somas}')


x = [0.027, 0.186, 0.442, 0.557, 0.566, 0.88, 0.967, 1.166, 1.242, 1.274, 1.848, 2.041, 2.112, 2.388, 2.638, 2.897, 3.428, 3.601, 3.646, 3.82, 4.06, 4.278, 4.34]
y = [1.318, 1.852, 2.655, 2.872, 2.884, 2.95, 2.876, 2.641, 2.543, 2.503, 2.023, 2.002, 2.013, 2.15, 2.396, 2.721, 2.892, 2.547, 2.419, 1.83, 1.108, 1.112, 1.277]
intervalo = [0.027,4.34]

trapzPonto(x, y)