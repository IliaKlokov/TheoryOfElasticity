import matplotlib.pyplot as plt
import numpy as np

def streamlines(mb, y, time):
    x = mb*np.fabs(y)**(-np.exp(time)/np.log(time))
    return x

def plot_streamlines(mb, y_min, y_max, y_num, time):
    y = np.linspace(y_min, y_max, y_num)
    t = np.linspace(0.1,time,10)
    for j in range(len(t)):
        fig, ax = plt.subplots()
        for i in range(len(mb)):
            x = streamlines(mb[i], y, t[j])
            plt.title('t = ' + str((j+1)*0.1))
            ax.plot(x, y, 'r-')
        v1 = [-np.exp(t[j])*k for k in mb]
        v2 = [np.log(t[j])*k for k in mb]
        ax.quiver(mb, y, v1, v2)    
        plt.show()
        #plt.savefig(str((j+1)*0.1)+'.png', format='png')