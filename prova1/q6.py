from weakref import ProxyTypes
import numpy as np


def poly(x,y):
    n = len(x)-1
    A =[]
    B =[]
    for xi in x:
        row = [1]
        for j in range(1, n+1):
            row.append(xi ** j)
        A.append(row)
    return np.linalg.solve(A, y)

def func_poly(x, coeffs):
    first=coeffs[0]
    return first + sum([ai * x ** j for j, ai in enumerate(coeffs[1:], 1)])

if __name__ == '__main__':
    #exemplo 1

    x=[-3.569, -2.576, -1.577, -0.828, 0.059, 1.051, 1.836, 2.627, 3.877]
    y=[3.726, 3.33, 0.609, 2.606, 3.993, 3.287, 1.878, 3.972, 2.974]

    coeffs = poly(x,y)
    #print(coeffs)

    for x in (coeffs):
        print("%.16f," %x)
    def p(x):
        return func_poly(x,coeffs)

print("%.16f" %p(-1.403))
print("%.16f" %p(-1.397))
print("%.16f" %p(0.931))
print("%.16f" %p(1.833))




#visulaizar
#import matplotlib.pylab as plt

#plt.scatter(x,y)
#t = np.linspace(min(x),  max(x), 200)
#pt = [p(ti) for ti in t]

#função seno
# st=np.sin(t)
# plt.plot(t, pt)
# plt.plot(t, st)

#plt.plot(t, pt)
#plt.savefig('interp.png')