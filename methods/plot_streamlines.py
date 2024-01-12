import matplotlib.pyplot as plt
import numpy as np

def streamlines(mb, y, time):
    x = mb*np.fabs(y)**(-np.exp(time)/np.log(time))
    return x

def plot_streamlines(mb, y_min, y_max, y_num, time):
    y = np.linspace(y_min, y_max, y_num)
    t = np.linspace(0.1, time, 10)
    a, b = 0, 0
    for j in range(len(t)):
        fig, ax = plt.subplots()
        for i in range(len(mb)):
            x = streamlines(mb[i], y, t[j])
            plt.title('t = ' + str((j + 1) * 0.1))
            ax.plot(x, y, 'r-')
            if (min(x) < a): a = min(x)
        x = np.linspace(a, max(mb), y_num//3)
        y = np.linspace(y_min, y_max, y_num//3)
        v1 = [-np.exp(t[j])*x[i] for i in range(len(x))]
        v2 = [np.log(t[j])*y[i] for i in range(len(y))]
        for i in range(len(x)):
            for k in range(len(y)):
                plt.quiver(x[i], y[k], v1[i], v2[k])
        #plt.show()
        plt.savefig(str((j+1)*0.1)+'.png', format='png')