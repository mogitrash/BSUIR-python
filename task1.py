import numpy as np
import math as m

a = -3.45
b = 349.1

y = pow(m.cos(m.pi/4),4) + pow(a+1.5,1/5) + a*pow(b,8) - b/m.log10(m.log10(abs(a) * m.log10(abs(a))))
print(y)