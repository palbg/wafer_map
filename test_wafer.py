import numpy as np
from scipy.interpolate import griddata
import matplotlib.pyplot as plt

'''points = [[1, 1],
          [1, 2],
          [2, 1],
          [2, 2]]

value=[0, 10, 2, 5]

grid = griddata(points, value, np.mgrid[1:2:10j, 1:2:10j], method='cubic')
plt.imshow(grid.T, extent=(0, 1, 0, 1), origin='lower')
plt.show()
'''

def func(x,y):
    return x+y

grid_x, grid_y = np.mgrid[0:1:10j, 0:1:10j]
points = np.random.rand(5, 2)
values = func(points[:,0], points[:,1])
print(points, values)
grid = griddata(points, values, (grid_x, grid_y), method='cubic')
plt.imshow(grid.T, extent=(0, 1, 0, 1), origin='lower')
plt.show()