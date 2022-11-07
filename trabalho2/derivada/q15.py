from methods import *

x0 = 1.83555
approximations = [-0.5354858486839991, -0.5350911210082376, -0.5336292753556293, -0.5325918548218098, -0.5319978353163464, -0.5316821691360474]


new_value = richardson(approximations.copy())
print(new_value)