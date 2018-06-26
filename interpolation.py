import matplotlib.pyplot as plt
from scipy.interpolate import griddata
import numpy as np
from matplotlib import cm

def draw_interpolation(wafer):

    fig = plt.figure(1)
    ax = fig.add_subplot(122)

    for cell in wafer.cell_list:
        x,y = cell.x, cell.y
        values = np.array(cell.value)

    points=[np.array(x),np.array(y)]
    points = np.transpose(points)

    (grid_x, grid_y)=np.mgrid[-0.5:23.5:200j, -0.5:12.5:100j]

    grid = griddata(points, values, (grid_x, grid_y), method='cubic')


    plt.imshow(grid.T, extent=(0, 1, 0, 1), origin='lower', cmap=cm.bwr)
    plt.title('Cubic')
    plt.colorbar()
    plt.axis('off')