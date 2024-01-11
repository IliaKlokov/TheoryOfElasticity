from models import materialBody
from methods import rungk
import math

class trajectory:
    x1 = None
    x2 = None
    def __init__(self, md, t):
        for i in range(len(md.points)):
            self.x1 = rungk(-math.exp(t)*md.points.rx)
            self.x2 = rungk(math.log(t)*md.points.rx)