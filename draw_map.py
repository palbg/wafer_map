'''Taking a map composed of cells, we draw a colored map of a considered value
blue is the highest value while red is the lowest'''

import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(wafer):

    fig = plt.figure()
    ax = fig.add_subplot(111)

    for cell in wafer.cell_list:
        x,y = cell.x, cell.y
        value = cell.value

        Amplitude, Middle, Maxi, Mini = wafer.amplitude()

        for k in range(len(value)):

            #takes values from the class 'wafer'
            value_k=value[k]
            x_k=x[k]
            y_k=y[k]
            print(x_k,y_k, value_k)

            # blue for values above the middle value, red for belows
            if (value_k-Middle)/Amplitude>=0:
                c = (1-(value_k-Middle)/Amplitude , 1-(value_k-Middle)/Amplitude, 1)
            else:
                c = (1, 1+(value_k-Middle)/Amplitude, 1+(value_k-Middle)/Amplitude)

            rect = patches.Rectangle((x_k,y_k), 0.9, 0.9, facecolor=c, edgecolor='k')
            ax.add_patch(rect)

    maxPatch = patches.Rectangle((0, 0), 0, 0, facecolor='b', edgecolor='k')
    midPatch = patches.Rectangle((0, 0), 0, 0, facecolor='w', edgecolor='k')
    minPatch = patches.Rectangle((0, 0), 0, 0, facecolor='r', edgecolor='k')

    plt.legend([maxPatch, midPatch, minPatch], [str(round(Maxi,4)), str(round(Middle,4)),str(round(Mini,4))], markerscale=100, frameon=False, fontsize=10)

    plt.xlim([-1, 23])
    plt.ylim([-1, 12])
    plt.axis('off')
    plt.show()