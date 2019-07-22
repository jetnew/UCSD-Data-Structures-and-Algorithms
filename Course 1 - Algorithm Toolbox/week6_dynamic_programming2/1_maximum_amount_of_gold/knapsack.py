# Uses python3
import sys


def optimal_weight(W, w):
    n = len(w)
    value = [[0]*(W+1) for _ in range(n)]

    for i in range(n):
        for j in range(1, W+1):
            value[i][j] = value[i-1][j]
            if w[i] <= j:
                val = value[i-1][j-w[i]] + w[i]
                if value[i][j] < val:
                    value[i][j] = val

    # print
    # for row in value:
    #     print(row)
    return value[-1][-1]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))

    print(optimal_weight(W, w))

