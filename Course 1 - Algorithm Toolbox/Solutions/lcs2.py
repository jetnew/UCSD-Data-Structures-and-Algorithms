#Uses python3

import sys


def lcs2(a, b):
    lookup = edit_distance(a, b)
    for row in lookup:
        print(row)
    return


def edit_distance(s, t):
    s = [' '] + s
    t = [' '] + t
    len_s = len(s)   # s is row
    len_t = len(t)   # t is col

    # Initialise lookup table
    lookup = [[-1*i]+[0]*(len_t-1) for i in range(len_s)]
    lookup[0] = [-1*i for i in range(len_t)]

    for i in range(len_s):
        for j in range(len_t):
            if i > 0 and j > 0:
                if s[i] == t[j]:
                    lookup[i][j] = lookup[i-1][j-1]
                else:
                    a = lookup[i-1][j] + 1
                    b = lookup[i][j-1] + 1
                    c = lookup[i-1][j-1] + 1
                    lookup[i][j] = min(a, b, c)
    return lookup


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
