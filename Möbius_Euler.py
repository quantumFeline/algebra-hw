import functions
import numpy as np
import matplotlib.pyplot as plt


def mobius(max_a):
    arr_res = np.zeros((max_a+1,))
    for i in range(1, max_a+1):
        factors = functions.factorisation(i)
        if factors.shape == np.unique(factors).shape:
            arr_res[i] = 1 if factors.shape[0] % 2 == 0 else -1
        else:
            arr_res[i] = 0
    return arr_res


def euler(max_a):
    return np.array([sum([1 if functions.gcd(n, x) == 1 else 0 for x in range(1,n)]) for n in range(0, max_a)])


mobius_calc = mobius(1000)
plt.scatter(np.arange(100), mobius_calc[:100], s=1)
plt.show()
plt.scatter(np.arange(1000), euler(1000), s=1)
plt.show()
