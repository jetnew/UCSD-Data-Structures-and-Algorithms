# Uses python3
import sys


def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


def fib(n):
    l = [0, 1]
    for i in range(n-1):
        l.append(l[-1] + l[-2])
    return l[-1]


def len_period(m):
    l = []
    i = 2
    while l[-2:] != [0, 1]:
        l.append(fib(i) % m)
        i += 1
    l = [0, 1] + l[:-2]
    return len(l)


def get_fib_huge(n, m):
    remainder = n % len_period(m)
    remainder = fib(remainder) % m
    return remainder


if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fib_huge(n, m))
