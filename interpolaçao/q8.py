def lagrange(x,y):
    #retorna yi dividido pelo denominador do polinomio Li
    num=len(x)
    coefs = []
    for i in range(num):
        prod=1
        for j in range(num):
            if i!=j:
                prod*=(x[i] - x[j])
        ci=y[i]/prod
        coefs.append(ci)
    return coefs

def pl(t,x,coefs) -> float:
    soma=0
    num = len(coefs)
    for i in range(num):
        prod=1
        for j in range(num):
            if i!=j:
                prod*=(t-x[j])
        prod*= coefs[i]
        soma+=prod
    return soma


def poly(x, coefs):
    def f(t):
        return pl(t,x, coefs)
    return f


if __name__ == '__main__':
    x=[2.674, 2.958, 3.138, 3.572, 3.779, 3.925, 4.214, 4.44]
    y=[0.647, 0.785, 0.84, 0.935, 0.969, 0.988, 0.994, 0.842]
    
    # x=[-0.691, 0.247, 0.681]
    # y=[0.07729752396, 0.39600431644 ,0.07940273264]
    
    # x=[1,3]
    # y=[1,-1]
    c = lagrange(x,y)
    print(c)
    lagr=poly(x, c)
    # print(lagrange(x, y))
    #print(lagr(0))

   #import matplotlib.pyplot as plt
    #import numpy as np

    #plt.scatter(x,y)
    #t=np.linspace(min(x), max(x), 100)
    #lt=[lagr(ti) for ti in t]
    #plt.plot(t, lt)
    #plt.savefig('lagrange.png')