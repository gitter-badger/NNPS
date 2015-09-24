import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


def plot_test(data):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x, y, z = [], [], []
    for point in data:
        x.append(point[0])
        y.append(point[1])
        z.append(point[2])
    ax.scatter(x,y,z,c='r')
    plt.show()
    return
