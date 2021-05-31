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
fig,ax =plt.subplots(figsize=(30,7.4))

# ax.add_patch(Rectangle((0, 0), 30, 7.4,facecolor="#04134e",edgecolor='#ff0000',linewidth=2.0,zorder=0,
#                       alpha=1))
plt.show(block=False)
i=0
n=20
try:
    while True:
        i=i+1
        # wait for a second
        time.sleep(3)
        ax.xaxis.set_major_locator(plticker.MultipleLocator(5))
        ax.yaxis.set_major_locator(plticker.MultipleLocator(1.85))
        ax.grid(which='major', axis='both', linestyle='-')
        ax.add_patch(Rectangle((0, 0), 30, 7.4, facecolor="#04134e", edgecolor='#ff0000', linewidth=2.0, zorder=0,
                               alpha=1))
        for j in range(0, n):
            x = round(random.uniform(1, 30),2)
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
                size=30000
            elif len(distnlist)<3 and len(distnlist)>1:
                color='#ffaa00'
                zord=50
                size=15000
            elif len(distnlist)<=1:
                color='#ffff00'
                zord=10
                size=10000
            distnlist.clear()
            plt.scatter(points_x[g],points_y[g], marker="s",s=size, facecolor=color, zorder=zord)

        # plt.scatter(*zip(*points), marker="s", facecolor='#ff0000', zorder=10)
        points.clear()
        ax.set_ylim(ymin=0)
        ax.set_xlim(xmin=0)
        ax.set_ylim(ymax=7.4)
        ax.set_xlim(xmax=30)
        # replace the image contents
        plt.savefig(path.join(outpath,'frame{0}.png'.format(i)), facecolor='#ffffff')
        fig.canvas.draw()
        fig.canvas.flush_events()
        ax.clear()


except KeyboardInterrupt:
    print('interrupted!')
