import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    rw = RandomWalk(5_0000)
    rw.fill_walk()
    # 将所有的点都绘制出来
    plt.style.use('classic')
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Oranges, edgecolors='none', s=1)
    ax.scatter(0, 0, c='yellow', edgecolors='none', s=50)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=50)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()

    keep_running = input("Make another walk?(y/n):")
    if keep_running == "n":
        break
