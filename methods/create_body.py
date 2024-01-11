from models.Material_body import Material_body
import math
def create_body(xc,yc,ang,n):
    mbpx = []
    mbpy = []
    mbc = Material_body(xc, yc, ang)
    for i in range(n):
        mbpx.append(xc + xc * math.cos(0 + ang + i * 90 / n))
        mbpx.append(xc + xc * math.cos(math.pi/2 + ang + i * 90 / n))
        mbpx.append(xc + xc * math.cos(math.pi + ang + i * 90 / n))
        mbpx.append(xc + xc * math.cos(math.pi/2*3 + ang + i * 90 / n))
        mbpy.append(yc + yc * math.sin(0 + ang + i * 90 / n))
        mbpy.append(yc + yc * math.sin(math.pi/2 + ang + i * 90 / n))
        mbpy.append(yc + yc * math.sin(math.pi + ang + i * 90 / n))
        mbpy.append(yc + yc * math.sin(math.pi/2*3 + ang + i * 90 / n))

    return mbc, mbpx, mbpy
