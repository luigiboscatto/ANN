"""Considere o seguinte PVI
y′=y(1−x)+x+2,y(x0)=y0,
com x0=1.83721 e y0=2.36241. Use o método de Runge-Kutta de ordem 2 com 
b=0.81755 para estimar o valor da solução exata desse PVI nos pontos
x1=1.84746, x2=1.92956, x3=1.94906, x4=2.00383, x5=2.06776, x6=2.1044, 
x7=2.18218, x8=2.19876, x9=2.26233, x10=2.32604, x11=2.36078, x12=2.39659, 
x13=2.44405, x14=2.52061, x15=2.56662, x16=2.60515, x17=2.66296, x18=2.71895,
x19=2.77636 e x20=2.82829."""





def RungeKutta2(f,x0,y0,h,n,x_values,b):
    
    '''''
    B = 1 corresponde ao metodo do ponto medio de Euler.
    B = 1/2 corresponde ao metodo de Heun
    B = 2/3 corresponde ao metodo de Ralston

    Porém, não testei.
    '''''

    a = 1 - b
    p = 1 / ( 2 * b)
    q = p
    for k in range(1,n):
        m1 = f(x0,y0)
        m2 = f(x0 + p * h,y0 + q * h * m1)
        y0 = y0 + (a * m1 + b * m2) * h
        h = x_values[k] - x_values[k-1]
        x0 = x_values[k-1]
        yield[x0,y0]

    m1 = f(x0,y0)
    m2 = f(x0 + p * h,y0 + q * h * m1)
    y0 = y0 + (a * m1 + b * m2) * h
    h = x_values[n-1] - x_values[n-2]
    x0 = x_values[k-1]
    yield[x0,y0]




if __name__ == "__main__":
    
    def f(x,y):
        func = y * (1 - x) + x + 2
        return func

    x0 = 0.22812
    y0 = 1.02399
    x_values = [0.25564, 0.28965, 0.36116, 0.38395, 0.4513, 0.49142, 0.53859, 0.59543, 0.65903, 0.68916, 0.73648, 0.80893, 0.86182, 0.89592, 0.93326, 0.99871, 1.04524, 1.11979, 1.14005, 1.19852]
    b = 0.54646
    n = 20

    h = x_values[0] - x0
    r5 = RungeKutta2(f,x0,y0,h,n,x_values,b)
    x5,y5 = zip(*r5)

    valores = str(y5)[1:-1] 
    print(valores)

