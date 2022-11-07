from methods import *






x = [0.1051, 1.2131, 1.7034, 2.7041, 4.0487, 4.4889, 5.194, 5.9167, 6.7552, 7.7411, 9.0971, 9.3474]
y = [6.328, 5.419, 5.0938, 4.4847, 4.0178, 3.9677, 3.9648, 3.9381, 4.0913, 4.4786, 5.0122, 5.2545]
values = [1.8752, 6.4229, 6.6755]



a0, a1, a2 = best_poly(x, y, 2)
print('Coefs:\n',f'{a0}, {a1}, {a2}', end=',')

def p(x, a0, a1, a2):
	return a0 + a1 * x + a2 * pow(x, 2)
print()
print('Values:')
for value in values:
    print(f'{p(value, a0, a1, a2)}', end=", ")
print("")
