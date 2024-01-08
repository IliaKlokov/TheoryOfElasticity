import math
def rungk(t0, dt, x0, y0):
    kx1=-math.exp(t0)*x0
    kx2=-math.exp(t0+dt/3) * (x0+dt*kx1/3)
    kx3=-math.exp(t0+2*dt/3) * (x0+dt*2*kx2/3)
    x1=x0+dt*(kx1/4+3*kx3/4)

    ky1 = math.log(t0) * y0
    ky2 = math.log(t0 + dt / 3) * (y0 + dt * ky1 / 3)
    ky3 = math.log(t0 + 2 * dt / 3) * (y0 + dt * 2 * ky2 / 3)
    y1 = y0 + dt * (ky1 / 4 + 3 * ky3 / 4)
    return x1,y1
