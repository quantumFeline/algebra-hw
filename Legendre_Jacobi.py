import functions
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib import colors as mcolors


def legendre(a,p):
    return functions.fast_power(a, (p-1)//2, p)


def jacobi(a,n):
    # print(a, n)
    if n <= 0 or n % 2 == 0:
        return -2  # Undefined

    res = 1
    while True:
        # print('cycle', a, n)

        if a == 1 or n == 1:
            return res

        if functions.gcd(a, n) != 1:
            return 0

        if a % 2 == 0:
            if n % 8 == 3 or n % 8 == 5:
                res *= -1
            a //= 2

        res *= (-1) ** ((n-1)//2) * (-1) ** ((a-1)//2)
        a, n = n % a, a


if __name__ == "__main__":
    print(jacobi(13,13))

    arr = np.fromfunction(np.vectorize(jacobi), (100, 100), dtype=int).T
    colors = [(0, 0, 0, 1), (1, 0, 0, 1), (1, 1, 1, 1), (0, 1, 0, 1)]
    values = [-2, -1, 0, 1]
    colormap = mcolors.ListedColormap(['black', 'red', 'white', 'green'])
    norm = mcolors.BoundaryNorm(values, colormap.N)
    im = plt.imshow(arr, cmap=colormap)
    # colors = [ im.cmap(im.norm(value)) for value in values]
    print(colors)
    patches = [ mpatches.Patch(color=colors[i], label="{l}".format(l=values[i])) for i in range(len(values))]
    plt.legend(handles=patches, bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

    plt.xlabel('a')
    plt.ylabel('n')

    plt.show()

# fig = plt.figure()
# ax = plt.subplot(111)
# chartBox = ax.get_position()
# ax.set_position([chartBox.x0, chartBox.y0, chartBox.width*0.6, chartBox.height])
# fig.colorbar(loc='upper center', bbox_to_anchor=(1.45, 0.8), shadow=True, ncol=1)
# ax.imshow(arr)
# plt.show()
