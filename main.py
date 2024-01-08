from methods.create_body import create_body
from methods.move_body import move
from methods.plot_trajectory import plottr

mb = create_body(1, 1, 15)
res=move(1,2,10000,1,1)
plottr(res.x_tr_points, res.y_tr_points)

