from models.Trajectory import Tracectory
from methods.runge_kutta import rungk
def move(t0, t, n, x0, y0):
    h=t/n
    tr = Tracectory()
    prx=x0
    pry=y0
    for i in range(n):
        x,y=rungk(t0+h*i, h, prx, pry)
        print(x, y)
        tr.add(x,y)
        prx=x
        pry=y
    return tr

