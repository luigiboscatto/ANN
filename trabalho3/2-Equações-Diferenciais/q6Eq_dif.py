import math
import numpy as np



def euler_mid(f, x0, y0, x_values, n):
    vals = []
    for k in range(n):
        if k == 0:
            h = x_values[0] - x0
        else:
            h = x_values[k] - x_values[k-1]
        
        m1 = f(x0, y0)
        m2 = f(x0 + h / 2, y0 + (h/2) * m1)
        y0 += + h * m2
        x0 += + h
        print(f'{y0},')
        vals.append([x0, y0])
    return vals

if __name__ == '__main__':

    #def f(x, y):
    #     return k*y

    #x0, y0 = 0.0, 1185514 # x0 = t, y0 = indivíduos
   # h = 0.0625
    #n = int(1/h)
    #k = 0.0712

    #P3.7
    def f(x, y):
        return y*(2 - x) + x + 1

    x0 = 1.49172
    y0 = 0.34574
    x_values = [1.5338, 1.58654, 1.60157, 1.64802, 1.71819, 1.7695, 1.83007, 1.86558, 1.93156, 1.96231, 2.00388, 2.07362, 2.10137, 2.14947, 2.20661, 2.28543, 2.30459, 2.38308, 2.41652, 2.48468]
    n = 20
    resposta = euler_mid(f, x0, y0, x_values, n)

    # def y(x):
    #     return 5 * math.exp(x - 1) - x - 2

    # t = np.linspace(x0, x0 + n * h, 100)
    # yt = [y(i) for i in t]

    # cx, cy = zip(*resposta)
    # plt.plot(t, yt)
    # plt.scatter(cx, cy)
    # plt.show()
