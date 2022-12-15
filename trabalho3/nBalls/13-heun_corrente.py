import numpy as np
import matplotlib.pyplot as plt


def euler(f, x0, y0, h, n):
    vals = []
    for k in range(n):
        y0 += h*f(x0, y0)
        x0 += h
        vals.append([x0, y0])
    return vals


# b = 1
def euler_mid(f, x0, y0, h, n):
    vals = []
    for _ in range(n):
        m1 = f(x0, y0)
        m2 = f(x0 + h / 2, y0 + (h/2) * m1)
        y0 += h*m2
        x0 += h
        vals.append([x0, y0])
    return vals


# b = 1/2
def heun(f, x0, y0, h, n):
    vals = []
    for _ in range(n):
        m1 = f(x0, y0)
        m2 = f(x0 + h, y0 + h*m1)
        y0 += h*(m1+m2)/2
        x0 += h
        vals.append([x0, y0])
    return vals


# b = 2/3
# def ralston(f, x0, y0, h, n):
#     vals = []
#     for _ in range(n):
#         m1 = f(x0, y0)
#         m2 = f(x0 + 0.75*h, y0 + 0.75*h*m1)
#         y0 = h*(m1 + 2*m2)/3
#         x0 += h
#         vals.append([x0, y0])
#     return vals


# padrao = euler_mid
def rk2(f, x0, y0, h, n, b=1.0):
    # b = 1 => metodo = euler_mid
    # b = 1/2 => metodo = heun
    # b = 2/3 => metodo = ralston
    vals = []
    a = 1-b
    p = 1/(2*b)
    q = p
    for _ in range(n):
        m1 = f(x0, y0)
        m2 = f(x0 + p*h, y0 + q*h*m1)
        y0 += (a*m1 + b*m2)*h
        x0 += h
        vals.append([x0, y0])
    return vals


def rk2_h_variavel(f, x0, y0, n, b, x_values):
    # b = 1 => metodo = euler_mid
    # b = 1/2 => metodo = heun
    # b = 2/3 => metodo = ralston
    vals = []
    a = 1-b
    p = 1/(2*b)
    q = p
    for i in range(n):
        if i == 0:
            h = x_values[0] - x0
        else:
            h = x_values[i] - x_values[i-1]
        m1 = f(x0, y0)
        m2 = f(x0 + p*h, y0 + q*h*m1)
        y0 += (a*m1 + b*m2)*h
        x0 += h
        vals.append([x0, y0])
    return vals


def diff(a, b):
    return sum((ai - bi)**2 for ai, bi in zip(a, b))


def f(x, y):
    return -y/np.sqrt(9**2-y**2)


def g(t, i):
    c =0.3135
    r = 1.3404
    l = 1.8111
    # considerando a função e(t) = e^(-e_value*pi*t)*sin(2*t-pi)
    # se e^(-0.0619*pi*t) => e_value = 0.0619
    e_value = 0.0689

    def e(t):
        return np.exp(-e_value*np.pi*t)*np.sin(2*t-np.pi)

    def e_(t):
        return np.exp(-e_value*np.pi*t)*(2*np.cos(np.pi-2*t)+e_value*np.pi*np.sin(np.pi-2*t))

    def e__(t):
        return np.exp(-e_value*np.pi*t)*((4-pow(e_value, 2)*pow(np.pi, 2))*np.sin(np.pi-2*t)-4*e_value*np.pi*np.cos(np.pi-2*t))

    return c*e__(t) + (1/r)*e_(t) + (1/l)*e(t)


if __name__ == '__main__':

    x0, y0 = 0, 0
    h = 0.1472
    n = 150
    b = 1/2
    x_values = []
    for i in range(1, n+1):
        x_values.append(i*h)
    x_values = [0.0551, 0.1871, 0.2378, 0.3182, 0.4829, 0.577, 0.6395, 0.7575, 0.8757, 0.9328, 1.0819, 1.1513, 1.2556, 1.3387, 1.4527, 1.587, 1.6273, 1.7821, 1.8289, 1.9577, 2.0106, 2.1511, 2.2818, 2.332, 2.4898, 2.534, 2.6548, 2.7535, 2.8202, 2.9882, 3.0455, 3.1483, 3.273, 3.3279, 3.4622, 3.5885, 3.6405, 3.7788, 3.8897, 3.9115, 4.0105, 4.1177, 4.2491, 4.3345, 4.4705, 4.5491, 4.6557, 4.7646, 4.8626, 4.916, 5.038, 5.151, 5.2649, 5.3485, 5.4357, 5.563, 5.6339, 5.7183, 5.8778, 5.9284, 6.0883, 6.1294, 6.2383, 6.3558, 6.4348, 6.5425, 6.6749, 6.7698, 6.8884, 6.9131, 7.0355, 7.1448, 7.2408, 7.3766, 7.4822, 7.5366, 7.6385, 7.7483, 7.8808, 7.9192, 8.0404, 8.1205, 8.2501, 8.3848, 8.4335, 8.5734, 8.6275, 8.7421, 8.8169, 8.9766, 9.0108, 9.1752, 9.2469, 9.3469, 9.4615, 9.5798, 9.6163, 9.76, 9.8701, 9.9854, 10.0327, 10.1396, 10.2562, 10.3479, 10.4673, 10.56, 10.6246, 10.7577, 10.8384, 10.9757, 11.018, 11.1244, 11.2722, 11.3616, 11.4137, 11.5616, 11.6452, 11.754, 11.8824, 11.9728, 12.0103, 12.1597, 12.2504, 12.3469, 12.4719, 12.5168, 12.6533, 12.7513, 12.8676, 12.9286, 13.0467, 13.1851, 13.2757, 13.3295, 13.4585, 13.5422, 13.6374, 13.7274, 13.8306, 13.9754, 14.0156, 14.1831, 14.2686, 14.353, 14.4881, 14.5818, 14.6371, 14.7876, 14.854, 14.9489]
    
    # metodo1 = euler(f, x0, y0, h, n)
    # metodo2 = euler_mid(f, x0, y0, h, n)
    # metodo3 = heun(f, x0, y0, h, n)
    # metodo4 = ralston(f, x0, y0, h, n)
    # metodo5 = rk2(g, x0, y0, h, n, b)
    metodo5 = rk2_h_variavel(g, x0, y0, n, b, x_values)

    indice = [i for i in range(n)]
    lista_x, lista_y = zip(*metodo5)

    for i, xi, yi in zip(indice, lista_x, lista_y):
        # print(f'x{i} = {xi} => y{i} = {yi}')
        print(f'{yi},', end='')

    plt.scatter(lista_x, lista_y)

    plt.savefig('edo.png')
    print()
    print()
    print('MUDAR C, L, I, H, e', 'MUDAR C, L, I, H, e', 'MUDAR C, L, I, H, e', 'MUDAR C, L, I, H, e', 'MUDAR C, L, I, H, e',
          'MUDAR C, L, I, H, e', 'MUDAR C, L, I, H, e', 'MUDAR C, L, I, H, e', 'MUDAR C, L, I, H, e', 'MUDAR C, L, I, H, e')
    print('MUDAR C, L, I, H, e', 'MUDAR C, L, I, H, e', 'MUDAR C, L, I, H, e', 'MUDAR C, L, I, H, e', 'MUDAR C, L, I, H, e',
          'MUDAR C, L, I, H, e', 'MUDAR C, L, I, H, e', 'MUDAR C, L, I, H, e', 'MUDAR C, L, I, H, e', 'MUDAR C, L, I, H, e')
    print('SE ELE DER X_VALUES TB TEM Q MUDAR','SE ELE DER X_VALUES TB TEM Q MUDAR','SE ELE DER X_VALUES TB TEM Q MUDAR','SE ELE DER X_VALUES TB TEM Q MUDAR''SE ELE DER X_VALUES TB TEM Q MUDAR',
    'SE ELE DER X_VALUES TB TEM Q MUDAR','SE ELE DER X_VALUES TB TEM Q MUDAR','SE ELE DER X_VALUES TB TEM Q MUDAR','SE ELE DER X_VALUES TB TEM Q MUDAR',
    'SE ELE DER X_VALUES TB TEM Q MUDAR','SE ELE DER X_VALUES TB TEM Q MUDAR')
