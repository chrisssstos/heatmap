import matplotlib.pyplot as plt
import numpy as np
import time
from os import path
import random
from matplotlib.patches import Rectangle
import math
import matplotlib.ticker as plticker
from scipy.stats import gaussian_kde
from scipy.spatial import distance
import mpl_scatter_density

outpath = "C:/Users/hrist/PycharmProjects/heatmap/frames"

points=[]
points2=[]
# create the figure
fig=plt.figure()
ax=fig.add_subplot(111, projection='3d')
# Removes the grey panes in 3d plots
ax.xaxis.set_pane_color((0, 0, 0.51, 1))
ax.yaxis.set_pane_color((0, 0, 0.51, 1))
ax.zaxis.set_pane_color((0, 0, 0.51, 1))

plt.show(block=False)
i=0
n1=10
n2=800
try:
    while True:
        i=i+1
        # wait for a second
        time.sleep(0.1)
        ax.xaxis.set_major_locator(plticker.MultipleLocator(5))
        ax.yaxis.set_major_locator(plticker.MultipleLocator(1.85))
        ax.grid(which='major', axis='both', linestyle='-')
        x = np.random.uniform(low=0, high=30, size=(n1,))
        y = np.random.uniform(low=0, high=7.4, size=(n1,))
        for h in range(0,n2):
            x= np.append(x,[x.flat[h]+random.gauss(0, 0.8)])
            y = np.append(y,[y.flat[h]])
        for h in range(0,n2):
            x= np.append(x,[x.flat[h]])
            y = np.append(y,[y.flat[h]+random.gauss(0, 0.8)])
            # y = np.append(y, [y.flat[h] + random.triangular(-1, 1)])
        points.append([x, y])
        for g in range(len(points)):
            points_x = [x for x, y in points]
            points_y = [y for x, y in points]
            points_x2 = [x2 for x2, y2 in points2]
            points_y2 = [y2 for x2, y2 in points2]
            # Calculate the point density
            xy = np.vstack([points_x[g], points_y[g]])
            z = gaussian_kde(xy)(xy)
            # Sort the points by density, so that the densest points are plotted last
            # idx = z.argsort()
            # x, y, z = points_x[g][idx], points_y[g][idx], z[idx]
            # if (points_x[g].any()<=30 and points_x[g].any()>=0) and (points_y[g].any()<=7.4 and points_y[g].any()>=0) :
            #     ax.scatter(points_x[g], points_y[g], 3, c=z, marker="o", s=50, depthshade=False, cmap=plt.cm.jet)
            ax.scatter(points_x[g], points_y[g], 3, c=z, marker="o", s=50, depthshade=False, cmap=plt.cm.jet)


        points.clear()
        ax.set_ylim(ymin=0)
        ax.set_xlim(xmin=0)
        ax.set_zlim(zmin=0)
        ax.set_ylim(ymax=7.4)
        ax.set_xlim(xmax=30)
        ax.set_zlim(zmax=13)
        # ax.set_axis_off()
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')
        ax.tick_params(axis='z', colors='white')
        ax.set_facecolor((0, 0, 0.51, 1))
        # replace the image contents
        fig.canvas.draw()
        fig.canvas.flush_events()
        plt.savefig(path.join(outpath, 'frame{0}.png'.format(i)), facecolor='#ffffff')
        ax.clear()


except KeyboardInterrupt:
    print('interrupted!')
