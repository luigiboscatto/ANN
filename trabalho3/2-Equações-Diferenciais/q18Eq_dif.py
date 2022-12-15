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
        m2 = f(x0 + h/2, y0 + (h/2) * m1)
        m3 = f(x0 + h/2, y0 + (h/2) * m2)
        m4 = f(x0 + h, y0 + h * m3)
        y0 = y0 + h * (m1+2 * m2 + 2 * m3 + m4)/6
        h = x_values[k] - x_values[k-1]
        x0 = x_values[k-1]
        yield[x0,y0]

    m1 = f(x0,y0)
    m2 = f(x0 + h/2, y0 + (h/2) * m1)
    m3 = f(x0 + h/2, y0 + (h/2) * m2)
    m4 = f(x0 + h, y0 + h * m3)
    y0 = y0 + h * (m1+2 * m2 + 2 * m3 + m4)/6
    h = x_values[n-1] - x_values[n-2]
    x0 = x_values[k-1]
    yield[x0,y0]




if __name__ == "__main__":
    
    def f(x,y):
        func = y * (1 - x) + x + 2
        return func

    x0 = 1.471
    y0 = 2.2156
    x_values = [1.5027, 1.5493, 1.6152, 1.6543, 1.68, 1.7534, 1.8115, 1.8305, 1.88, 1.9375, 1.9869, 2.0598, 2.0939, 2.1561, 2.2013, 2.2659, 2.2986, 2.3587, 2.4009, 2.4606]
    b = 1
    n = 20

    h = x_values[0] - x0
    r5 = RungeKutta2(f,x0,y0,h,n,x_values,b)
    x5,y5 = zip(*r5)

    valores = str(y5)[1:-1] 
    print(valores)

