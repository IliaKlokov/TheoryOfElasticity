import numpy as np
import matplotlib.pyplot as plt
import math
def plot_streamlines(t,x1,x2):
    X1, X2 = np.meshgrid(x1, x2)

    V1 = -math.exp(t) * X1
    V2 = math.log(t) * X2

    plt.streamplot(X1, X2, V1, V2, density=2)

    plt.xlabel('x1')
    plt.ylabel('x2')
    plt.title('Линии тока для поля скоростей')
    plt.grid()
    plt.show()