# Uses python3
import sys


def pisano_period(n,m):
    pisano_period = []
    fib = []
    if n <= 1:
        return n

    previous = 0
    current  = 1
    for i in range(2*(m+1)):
        if i <= m: pisano_period.append(previous)
        fib.append(previous)
        previous, current = current, (previous + current )%m
    add = 0
    while pisano_period != fib[len(pisano_period):]:
        for _ in range(2):
            fib.append(previous)
            previous,current = current, (previous+current)%m
        pisano_period.append(fib[len(pisano_period)])
        add+=1
    return pisano_period[n%len(pisano_period)]

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(pisano_period(n,m))
