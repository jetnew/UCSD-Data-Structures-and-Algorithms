# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def optimal_points(segments):
    points = []
    while segments:
        # Segment with smallest end
        smallest = min(segments, key = lambda t: t[1])
        points.append(smallest.end)

        segments.remove(smallest)
        # print(segments)
        for s in segments[:]:
            # print(s.start)
            # print(smallest.end)
            # print(s.end)
            if s.start <= smallest.end <= s.end:
                segments.remove(s)
        # print(segments)
    return points

#   ----
#  ----
# ---
# 1234567
#    ----
# ---
#  ----
#     --


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
