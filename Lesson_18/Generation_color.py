#! wget -nc "https://raw.githubusercontent.com/PacktPublishing/Python_Master-the-Art-of-Design-Patterns/master/Module%201/Chapter9/colors.csv"
import csv
from random import random
import math
from collections import Counter

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

dataset_filename = 'colors.csv'


def load_colors(filename):
    with open(filename) as dataset_file:
        lines = csv.reader(dataset_file)
        for line in lines:
            # print(line)
            yield tuple(float(y) for y in line[0:3]), line[3]


def generate_colors(count=100):
    for i in range(count):
        yield (random(), random(), random())


def color_distance(color1, color2):
    channels = zip(color1, color2)
    sum_distance_squared = 0
    for c1, c2 in channels:
        sum_distance_squared += (c1 - c2) ** 2
    return math.sqrt(sum_distance_squared)


# def color_distance(color1, color2):
#    return math.sqrt(sum((x[0] - x[1]) ** 2 for x in zip(color1, color2)))


def nearest_neighbors(model_colors, num_neighbors):
    model = list(model_colors)
    target = yield
    while True:
        distances = sorted(
            ((color_distance(c[0], target), c) for c in model),
        )
        target = yield [
            d[1] for d in distances[0:num_neighbors]
        ]


def name_colors(get_neighbors):
    color = yield
    while True:
        near = get_neighbors.send(color)
        name_guess = Counter(n[1] for n in near).most_common(1)[0][0]
        color = yield name_guess


def write_results(filename="output.csv"):
    with open(filename, "w") as file:
        writer = csv.writer(file)
        while True:
            color, name = yield
            writer.writerow(list(color) + [name])


def process_colors(dataset_filename="colors.csv"):
    model_colors = load_colors(dataset_filename)
    get_neighbors = nearest_neighbors(model_colors, 5)
    get_color_name = name_colors(get_neighbors)
    output = write_results()
    next(output)
    next(get_neighbors)
    next(get_color_name)

    # this for rendering colors
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    rs, gs, bs, cs, ns = [], [], [], [], []

    for color in generate_colors(300):
        name = get_color_name.send(color)
        output.send((color, name))

        # for drawing
        rs.append(color[0])
        gs.append(color[1])
        bs.append(color[2])
        cs.append(color)
        ax.text(
            color[0], color[1], color[2], name, size=6, zorder=1, color='k')

    ax.scatter(xs=rs, ys=gs, zs=bs, c=cs)
    plt.show()

process_colors()