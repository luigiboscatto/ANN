from methods import *

def f(x):
    return math.log(2 + math.cos(math.exp(-x)))

x0 = -1.1096
order = 4
x = [-1.3238, -1.27, -1.2107, -1.1157, -1.0842, -1.0116, -0.9426, -0.8821]
values = [-1.0122, -0.9588, -0.9573, -0.9515]

order1 = 1
order2 = 2
order3 = 3
order4 = 4

p = 0
n = len(values)
for i in range(n):
    p = f(x0) + finite_diffs(x, order1, x0, f)*(values[i] - x0) + ((finite_diffs(x, order2, x0, f)/2) * ((values[i]-x0)**2)) + ((finite_diffs(x, order3, x0, f)/6) * ((values[i]-x0)**3))  + ((finite_diffs(x, order4, x0, f)/24) * ((values[i]-x0)**4))
    erroN = math.sqrt(((f(values[i]) - p)**2))
    print(f'{values[i]} = {p} e |f(x) - p3(x)| = {erroN}')

num_pontos = 0
a = x0 - 0.25
b = x0 + 0.25

print("")
for i in range(n):
    p = f(x0) + finite_diffs(x, order1, x0, f)*(values[i] - x0) + ((finite_diffs(x, order2, x0, f)/2) * ((values[i]-x0)**2)) + ((finite_diffs(x, order3, x0, f)/6) * ((values[i]-x0)**3))  + ((finite_diffs(x, order4, x0, f)/24) * ((values[i]-x0)**4))
    erroN = math.sqrt(((f(values[i]) - p)**2))
    print(f'{p}, {erroN}', end=", ")
print("")