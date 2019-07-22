# Uses python3
from sys import stdin


def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10


def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
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


def fib_sum_sq(n):
    a = get_fib_huge(n, 10)
    b = get_fib_huge(n+1, 10)
    sum_sq = a * b
    sum_sq %= 10
    return sum_sq

#

if __name__ == '__main__':
    n = int(stdin.read())
    print(fib_sum_sq(n))
