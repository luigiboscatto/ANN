"""Em um circuito com tensão aplicada E e com resistência R, indutância 
L e capacitância C em paralelo, a corrente i satisfaz a equação diferencial
didt=Cd2Edt2+1RdEdt+1LE.
Suponha que C=0.2311farads, R=1.3534ohm, L=1.5026henrie e que a tensão seja dada por
E(t)=e−0.0549πtsin(2t−π).
Se i(t0)=i0, com t0=0 e i0=0, use o método de Heun para encontrar estimativas
para a corrente i nos pontos
t1=0.0853, t2=0.124, t3=0.2613, t4=0.3842, t5=0.4704, t6=0.5809, t7=0.6249, 
t8=0.7385, t9=0.8313, t10=0.9542, ...... t149=14.8388 e t150=14.939."""

import numpy as np



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
    return y * (1 - x) + x + 2


def g(t, i):
    c = 0.3001
    r = 1.2223
    l = 1.645

    # considerando a função e(t) = e^(-e_value*pi*t)*sin(2*t-pi)
    # se e^(-0.0549*pi*t) => e_value = 0.0549
    e_value = 0.0647

    def e(t):
        return np.exp(-e_value*np.pi*t)*np.sin(2*t-np.pi)

    def e_(t):
        return np.exp(-e_value*np.pi*t)*(2*np.cos(np.pi-2*t)+e_value*np.pi*np.sin(np.pi-2*t))

    def e__(t):
        return np.exp(-e_value*np.pi*t)*((4-pow(e_value, 2)*pow(np.pi, 2))*np.sin(np.pi-2*t)-4*e_value*np.pi*np.cos(np.pi-2*t))

    return c*e__(t) + (1/r)*e_(t) + (1/l)*e(t)


if __name__ == '__main__':

    x0, y0 = 0,0
    h = 0.101
    n = 150
    b = 1/2
    t_values = [0.0142, 0.1644, 0.2475, 0.3157, 0.4274, 0.5755, 0.6599, 0.7766, 0.8548, 0.989, 1.0414, 1.1567, 1.2419, 1.364, 1.4853, 1.5129, 1.6743, 1.7689, 1.8542, 1.9715, 2.0315, 2.1267, 2.2519, 2.3759, 2.4775, 2.5577, 2.645, 2.7544, 2.8552, 2.956, 3.0625, 3.1371, 3.2641, 3.3294, 3.4732, 3.5884, 3.6606, 3.7743, 3.8698, 3.9547, 4.0161, 4.1668, 4.2665, 4.3347, 4.4235, 4.5719, 4.6146, 4.7592, 4.8787, 4.9405, 5.0189, 5.1328, 5.2811, 5.3328, 5.4511, 5.528, 5.6279, 5.7363, 5.8761, 5.9892, 6.0447, 6.1497, 6.2622, 6.3648, 6.4399, 6.5399, 6.6824, 6.763, 6.8576, 6.9471, 7.0555, 7.1813, 7.2149, 7.3789, 7.4251, 7.5108, 7.6813, 7.7887, 7.8567, 7.9239, 8.0229, 8.1233, 8.2849, 8.3709, 8.42, 8.5815, 8.6818, 8.7483, 8.827, 8.945, 9.05, 9.1527, 9.2673, 9.3307, 9.4637, 9.5529, 9.6451, 9.7746, 9.8583, 9.9714, 10.0653, 10.1315, 10.2625, 10.3796, 10.453, 10.5337, 10.6117, 10.7515, 10.8724, 10.938, 11.0317, 11.1838, 11.2263, 11.3803, 11.441, 11.5399, 11.6662, 11.79, 11.8411, 11.9732, 12.0325, 12.1292, 12.2238, 12.3786, 12.4253, 12.5501, 12.6731, 12.7411, 12.8741, 12.9738, 13.0426, 13.1821, 13.2579, 13.3486, 13.4381, 13.5513, 13.6445, 13.7598, 13.8372, 13.9664, 14.0673, 14.138, 14.2471, 14.3449, 14.4647, 14.545, 14.6716, 14.7553, 14.8804, 14.9346]
    """observar o valor de b na função para qual médoto é usado:
    --> b = 1 => metodo = euler_mid
    --> b = 1/2 => metodo = heun
    --> b = 2/3 => metodo = ralston"""
    
    
    # metodo1 = euler(f, x0, y0, h, n)
    # metodo2 = euler_mid(f, x0, y0, h, n)
    # metodo3 = heun(f, x0, y0, h, n)
    # metodo4 = ralston(f, x0, y0, h, n)
    # metodo5 = rk2(g, x0, y0, h, n, b)
    metodo6 = rk2_h_variavel(g, x0, y0, n, b, t_values)

    indice = [i for i in range(n)]
    lista_x, lista_y = zip(*metodo6)

    for i, xi, yi in zip(indice, lista_x, lista_y):
        # print(f'x{i} = {xi} => y{i} = {yi}')
        print(f'{yi},', end='')

 