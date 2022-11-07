from methods import *

def f(x):
    return x**2 * math.cos(x - 1) * math.exp(-3 * x ** 2)
x0 = 0.6883
order = 5
x = [0.4682, 0.4934, 0.5582, 0.6231, 0.6745, 0.7358, 0.7664, 0.7911, 0.8699, 0.8898]
values = [0.5416, 0.6699, 0.6817, 0.6879, 0.8612]

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