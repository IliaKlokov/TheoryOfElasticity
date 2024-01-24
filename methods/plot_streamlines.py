from models.Stream_line import streamLine
import matplotlib.pyplot as plt
import numpy as np

def plot_streamlines(time, min, max):
    a = np.linspace(min, max, 2*(max-min)+1)
    x, y = np.meshgrid(a, a)
    s = streamLine(time, x, y)
    plt.streamplot(x, y, s.v1, s.v2, density=0.3, color='red')
    a = np.linspace(min, max, 4*(max-min)+1)
    x, y = np.meshgrid(a, a)
    s = streamLine(time, x, y)
    plt.quiver(x, y, s.v1, s.v2, scale=100, )
    plt.title(f'time = {time}')
    plt.show()