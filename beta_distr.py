import numpy as np
from numpy._distributor_init import NUMPY_MKL  # requires numpy+mkl
import matplotlib.pyplot as plt
import scipy
import scipy.special
import math

N = 50
x = np.random.rand(N)
y = np.random.rand(N)

a = 3.38175026476458
# lst = [[],[],[]]
# shift = [4, 5, 2]
# for i in range(10000):
# 	for j in range(3):
# 		lst[j].append(shift[j] + np.random.beta(a,a)*4)

# plt.scatter(sorted(lst[0]), range(len(lst[0])))
# plt.show()

# X = np.linspace(0, 1, 256, endpoint=True)
# B = [math.pow(x,a-1)*math.pow(1-x,a-1)/scipy.special.beta(a,a) for x in X]
# plt.plot(X, B)
# plt.show()

from scipy.stats import beta
import matplotlib.pyplot as plt
import numpy as np
# a = 2
b = a
x = np.arange (-50, 50, 0.1)
y = beta.pdf(x,a,b, scale=50, loc=-50)
plt.plot(x,y)
plt.show()