
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import random as rd

# rect1 = patches.Rectangle((-200,-100), 400, 200, color='#0099FF')
# RGB


fig = plt.figure()

ax = fig.add_subplot(111)
for i in range(22):
    for j in range(11):
        c=i*j*2-200
        if c>0:
            c=(1-c/255,1-c/255,1)
        else:
            c = (1, 1+c / 255, 1+c / 255)
        if i+j>2 and i+j<30:
            rect = patches.Rectangle((i/2,j), 0.4, 0.9, color=c)
            ax.add_patch(rect)



plt.xlim([-1, 12])
plt.ylim([-1, 12])
plt.show()