from models.Material_body import materialBody
from models.Material_point import Material_point
def create_body(xc,yc):
    p = []
    for i in range(-0.5,0.5,0.5):
        for j in range(-0.5,0.,0.5):
            p.append(Material_point(xc+j,yc+j))
    mb = materialBody(xc, yc, p)
    return mb