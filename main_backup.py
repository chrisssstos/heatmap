import matplotlib.pyplot as plt
import numpy as np
import time
from os import path
import random
from matplotlib.patches import Rectangle
import math
import matplotlib.ticker as plticker

from scipy.spatial import distance

outpath = "C:/Users/hrist/PycharmProjects/heatmap/frames"

points=[]

# create the figure
fig=plt.figure()
ax=fig.add_subplot(111, projection='3d')


# ax.add_patch(Rectangle((0, 0), 30, 7.4,facecolor="#04134e",edgecolor='#ff0000',linewidth=2.0,zorder=0,
#                       alpha=1))
plt.show(block=False)
i=0
n=5
try:
    while True:
        i=i+1
        # wait for a second
        time.sleep(0.1)
        ax.xaxis.set_major_locator(plticker.MultipleLocator(5))
        ax.yaxis.set_major_locator(plticker.MultipleLocator(1.85))
        ax.grid(which='major', axis='both', linestyle='-')
        ax.plot_wireframe(30, 7, np.atleast_2d(-2.0), rstride=10, cstride=10)
        for j in range(0, n):
            x = round(random.uniform(0, 30),2)
            y = round(random.uniform(0, 7.4),2)
            points.append([x,y])
        for g in range(len(points)):
            tot_d = 0
            distnlist = []
            points_x = [x for x, y in points]
            points_y = [y for x, y in points]
            for f in range(len(points)):
                distn = round(math.sqrt(((points_x[g] - points_x[f]) ** 2) + ((points_y[g] - points_y[f]) ** 2)),2)
                if distn<=2:
                    distnlist.append(distn)
            print(len(distnlist))
            if len(distnlist)>=3:
                color='#ff0000'
                zord=100
                size=300
                for i in range(0, 12):
                    ax.scatter(points_x[g], points_y[g], i, s=size, marker="s", facecolor=color)
            elif len(distnlist)<3 and len(distnlist)>1:
                color='#ffaa00'
                zord=50
                size=150
                for i in range(0, 6):
                    ax.scatter(points_x[g], points_y[g], i, s=size, marker="s", facecolor=color)
            elif len(distnlist)<=1:
                color='#ffff00'
                zord=10
                size=100
                for i in range(0, 3):
                    ax.scatter(points_x[g], points_y[g], i, s=size, marker="s", facecolor=color)
            distnlist.clear()


        # plt.scatter(*zip(*points), marker="s", facecolor='#ff0000', zorder=10)
        points.clear()
        ax.set_ylim(ymin=0)
        ax.set_xlim(xmin=0)
        ax.set_zlim(zmin=0)
        ax.set_ylim(ymax=7.4)
        ax.set_xlim(xmax=30)
        ax.set_zlim(zmax=13)
        # replace the image contents
        fig.canvas.draw()
        fig.canvas.flush_events()
        ax.clear()


except KeyboardInterrupt:
    print('interrupted!')
