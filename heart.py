import matplotlib.pyplot as plt
from matplotlib.pyplot import *
import matplotlib_inline.backend_inline

matplotlib_inline.backend_inline.set_matplotlib_formats('svg', 'pdf')
plt.rcParams['figure.dpi'] = 200
plt.rcParams['savefig.dpi'] = 200
plt.style.use('default')


def heart(x, y, z):
    return (x ** 2 + ((9 * y ** 2) / 4) + z ** 2 - 1) ** 3 - x ** 2 * z ** 3 - ((9 * y ** 2 * z ** 3) / 80)


def plot_implicit(fn, bbox=(-1.5, 1.5)):
    N = 10
    i = 0
    while N != 200:
        """ create a plot of an implicit function
        fn  ...implicit function (plot where fn==0)
        bbox ..the x,y,and z limits of plotted interval"""
        xmin, xmax, ymin, ymax, zmin, zmax = bbox * 3
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        resolution = np.linspace(xmin, xmax, 100)  # resolution of the contour
        slices = np.linspace(xmin, xmax, 20)  # number of slices
        resolution1, resolution2 = np.meshgrid(resolution, resolution)  # grid on which the contour is plotted

        for z in slices:  # plot contours in the XY plane
            X, Y = resolution1, resolution2
            Z = fn(X, Y, z)
            colorSet = ax.contour(X, Y, Z + z, [z], zdir='z', colors=('r',))
            # [z] defines the only level to plot
            # for this contour for this value of z

        for y in slices:  # plot contours in the XZ plane
            X, Z = resolution1, resolution2
            Y = fn(X, y, Z)
            colorSet = ax.contour(X, Y + y, Z, [y], zdir='y', colors=('purple',))

        for x in slices:  # plot contours in the YZ plane
            Y, Z = resolution1, resolution2
            X = fn(x, Y, Z)
            colorSet = ax.contour(X + x, Y, Z, [x], zdir='x', colors=('pink',))

        # must set plot limits because the contour will likely extend
        # way beyond the displayed level.  Otherwise matplotlib extends the plot limits
        # to encompass all values in the contour.
        ax.set_zlim3d(zmin, zmax)
        ax.set_xlim3d(xmin, xmax)
        ax.set_ylim3d(ymin, ymax)
        elev = 10
        azim = N
        ax.view_init(elev, azim)
        N += 0.5
        i +=1
        print('ax.azim = {}'.format(ax.azim))
        print('ax.dist = {}'.format(ax.dist))
        print('ax.elev = {}'.format(ax.elev))
        print("__________________")

        plt.show()
        plt.close('all')

if __name__ == '__main__':
    plot_implicit(heart)
