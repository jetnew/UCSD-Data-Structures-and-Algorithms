# Uses python3
import sys


def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1
    sum = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current
    return sum % 10


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
    return m % 10


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    # for n in range(10):
    print(fib_sum_last_digit(n))