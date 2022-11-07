import math


def trapz(nome_funcao, a, b, h):
    n = int((b-a)/h)
    soma = 0

    for k in range(1, n):
        soma += f(nome_funcao, a+k*h)

    return (h/2)*(f(nome_funcao, a) + 2*soma + f(nome_funcao, b))


def romberg(coluna_f1):
    coluna_f1 = [i for i in coluna_f1]
    n = len(coluna_f1)
    for j in range(n-1):
        temp_col = [0] * (n-1-j)
        for i in range(n-1-j):
            power = j+1
            temp_col[i] = (4**power*coluna_f1[i+1]-coluna_f1[i])/(4**power-1)
        coluna_f1[:n-1-j] = temp_col
        #print(f'F_{j+2} = {temp_col}')
    return coluna_f1[0]


def f_1():
    def f(x):
        return math.exp(-x**2)
    return f


def f_2():
    def f(x):
        return math.sqrt(1+x**2)

    return f


def f_3():
    def f(x):
        return (x+1/x)**2

    return f


def f_4():
    def f(x):
        return math.cos(-x**2/3)

    return f


def f_5():
    def f(x):
        return math.exp(x)*math.sin(x)/(1+x**2)

    return f


def f(nome_funcao, value):
    x = value
    return eval(nome_funcao)


if __name__ == '__main__':
    func = ['-x*(x-21)*(x+1)']
    a = [0]
    b = [12]
    order = [8]
    h = [12/10]
    c = 0
    #for i in n:
     #   h.append((b[c]-a[c])/n[c])
      #  c+=1

    for i in range(len(func)):
        k = int(order[i]/2)
        hs = [h[i]/2**ki for ki in range(k)]

        col1 = [trapz(func[i], a[i], b[i], hi) for hi in hs]

        #print(f'F_1 = {col1}')

        r = romberg(col1)

        print(r,',')
