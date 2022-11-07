from methods import *

def f(x):
    return x**2 * math.cos(x - 1) * math.exp(-3 * x ** 2)
x0 = 0.0386
order = 5
x = [-0.2039, -0.1252, -0.0629, -0.0216, 0.0278, 0.0435, 0.1076, 0.1774, 0.2258, 0.2621]
values = [-0.0744, 0.0076, 0.1007, 0.1748, 0.2248]

order1 = 1
order2 = 2
order3 = 3
order4 = 4
order5 = 5

p = 0
n = len(values)
for i in range(n):
    p = f(x0) + finite_diffs(x, order1, x0, f)*(values[i] - x0) + ((finite_diffs(x, order2, x0, f)/2) * ((values[i]-x0)**2)) + ((finite_diffs(x, order3, x0, f)/6) * ((values[i]-x0)**3)) + ((finite_diffs(x, order4, x0, f)/24) * ((values[i]-x0)**4)) + ((finite_diffs(x, order, x0, f)/120) * ((values[i]-x0)**5)) 
    erroN = math.sqrt(((f(values[i]) - p)**2))
    print(f'{p}, {erroN}', end=", ")
print("")