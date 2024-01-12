from methods.move_through_space import movet
from methods.create_body import create_body
import matplotlib.pyplot as plt
mbc, mbpx, mbpy = create_body(-2,-2,0,10)
plt.plot(mbpx,mbpy)
plt.show()
movet(0.1,1,25,mbpx,mbpy)

