# Uses python3
import sys


def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l
    return a*b


def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    larger = max([a, b])
    smaller = min([a, b])

    remainder = larger % smaller

    return gcd(smaller, remainder)


def lcm(a, b):
    lcm = a*b // gcd(a, b)
    return lcm


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))

