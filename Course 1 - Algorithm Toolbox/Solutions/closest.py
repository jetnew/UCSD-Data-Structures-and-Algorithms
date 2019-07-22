#Uses python3
import sys
import math
import random


def naive_min(x, y):
    length = len(x)
    min_dist = 1000
    if length == 2:
        min_dist = math.sqrt((x[0] - x[1]) ** 2 + (y[0] - y[1]) ** 2)
    return min_dist


def minimum_distance(x, y):
    if len(x) == 1:
        return 10000
    if len(x) == 2:
        return math.sqrt((x[0] - x[1]) ** 2 + (y[0] - y[1]) ** 2)

    # Sort the points in order to get middle partition index
    points = []
    for i in range(len(x)):
        points.append((x[i], y[i]))
    points = sorted(points)
    p_index = len(x) // 2

    # Re-arrange x and y after sorting by x-coordinate
    x = []
    y = []
    for i in points:
        x.append(i[0])
        y.append(i[1])

    # Recursively call the minimum distance for the 2 segments
    d1 = minimum_distance(x[:p_index], y[:p_index])
    d2 = minimum_distance(x[p_index:], y[p_index:])
    d = min(d1, d2)

    # Get a list of points of partition strip
    strip = []
    for i in points:
        if abs(i[0] - x[p_index]) < d:
            strip.append(i)

    # Sort coordinates on strip by y-coordinate
    strip.sort(key=lambda x: x[1]) # O(nlogn)

    # Compute minimum distance based on the next 7 points for each point
    min_dist = d
    for k, i in enumerate(strip):
        for j in strip[k+1:k+7]:
            dist = math.sqrt((i[0] - j[0]) ** 2 + (i[1] - j[1]) ** 2)
            if dist < min_dist:
                min_dist = dist
    return min_dist


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
