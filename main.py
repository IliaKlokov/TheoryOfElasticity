from methods.move_through_space import movet
from methods.create_body import create_body
import matplotlib.pyplot as plt
mbc, mbpx, mbpy = create_body(1,1,0,25)
plt.plot(mbpx,mbpy)
plt.show()
movet(1,1,25,mbpx,mbpy)

