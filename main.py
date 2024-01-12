from methods.move_through_space import movet
from methods.create_body import create_body
from methods.plot_streamlines import plot_streamlines
import matplotlib.pyplot as plt
mbc, mbpx, mbpy = create_body(-2,-2,0,10)
plt.plot(mbpx,mbpy)
plt.show()
movet(0.1,1,25,mbpx,mbpy)
print(mbpx,mbpy)
plot_streamlines(mbpx, mbpy[0], mbpy[-1], len(mbpx), 1)