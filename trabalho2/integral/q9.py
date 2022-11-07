import math

def simps(f, a, b, n):
    if n % 2 != 0 or n < 1:
        raise ValueError("n deve ser par e maior q 1")
    h = (b - a) / n
    soma_odd, soma_even = 0, 0
    for k in range(1,n,2):
        soma_odd += f(a+k*h)
    for k in range(2,n,2):
        soma_even += f(a + k * h)
    return (h/3) * (f(a) + 4 * soma_odd + 2 * soma_even + f(b))

def f(x):
    return math.sqrt(1 + math.cos(x)**2)

def simp(x0,x1,x3,y0,y1,y2):
    return ((x1-x0)/3)*(y0+4*y1+y2)

def simpsPonto(x, y):
    tam = (len(x) - 1) // 2
    somas = 0
    k = 0
    for i in range(tam):
        somas += simp(x[k],x[k+1],x[k+2],y[k],y[k+1],y[k+2])
        k += 2
    print(f'{somas}')

x = [0.037, 0.547, 1.057, 1.2705, 1.484, 1.6505, 1.817, 2.0705, 2.324, 2.432, 2.54, 2.7615, 2.983, 3.143, 3.303, 3.627, 3.951, 3.9715, 3.992, 4.0695, 4.147]
y = [1.347, 2.857, 2.777, 2.507, 2.263, 2.122, 2.033, 2.005, 2.105, 2.186, 2.287, 2.548, 2.823, 2.965, 2.992, 2.475, 1.383, 1.322, 1.264, 1.091, 1.005]
simpsPonto(x, y)
