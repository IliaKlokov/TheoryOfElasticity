class Stream_line:
    x_sl_points=[]
    y_sl_points=[]
    def __init__(self, x_sl_points, y_sl_points):
        self.x_sl_points = x_sl_points
        self.y_sl_points = y_sl_points
    def add (self,x,y):
        self.x_sl_points.append(x)
        self.y_sl_points.append(y)