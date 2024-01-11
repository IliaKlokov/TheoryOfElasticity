from models.Material_body import Material_body
import math
def create_body(xc,yc,ang,n):
    mbpx = []
    mbpy = []
    mbc = Material_body(xc, yc, ang)
    for i in range(n):
        mbpx.append(xc + math.sqrt(2) / 2 * math.cos(1*math.pi / 2 + ang))
        mbpx.append(xc + math.sqrt(2) / 2 * math.cos(2*math.pi / 2 + ang))
        mbpx.append(xc + math.sqrt(2) / 2 * math.cos(3*math.pi / 2 + ang))
        mbpx.append(xc + math.sqrt(2) / 2 * math.cos(4*math.pi / 2 + ang))
        mbpy.append(yc + math.sqrt(2) / 2 * math.sin(1 * math.pi / 2 + ang))
        mbpy.append(yc + math.sqrt(2) / 2 * math.sin(2 * math.pi / 2 + ang))
        mbpy.append(yc + math.sqrt(2) / 2 * math.sin(3 * math.pi / 2 + ang))
        mbpy.append(yc + math.sqrt(2) / 2 * math.sin(4 * math.pi / 2 + ang))
    return mbc, mbpx, mbpy

