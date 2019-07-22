# Uses python3
import sys


def optimal_summands(n):
    summands = []
    m = n
    i = 1
    while m > 0:
        summands.append(i)
        i += 1
        m -= i
    summands[-1] += n - sum(summands)
    return summands


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
