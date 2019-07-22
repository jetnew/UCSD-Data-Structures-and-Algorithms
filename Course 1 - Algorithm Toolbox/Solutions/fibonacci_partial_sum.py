# Uses python3
import sys


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


def fib_sum_last_digit(n):
    # m = fib(n+2) - 1
    m = get_fib_huge(n+2, 10) - 1
    return m


def fib_partial_sum(from_, to):
    m = fib_sum_last_digit(to)
    n = fib_sum_last_digit(from_ - 1)
    partial = (m - n) % 10
    return partial


def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

    return sum % 10


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fib_partial_sum(from_, to))