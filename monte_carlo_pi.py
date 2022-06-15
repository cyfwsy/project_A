# calculate pi using monte_carlo algor
from numpy.random import rand
import numpy as np
N = 1000000
x = rand(N)
y = rand(N)
n = np.sum(x**2+y**2 < 1)
s = 4*n/N
print(s)
print('end')
print('second end')


