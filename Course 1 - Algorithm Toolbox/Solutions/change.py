# Uses python3
import sys


def get_change(m):
    no = 0
    while m-10 >= 0:
        m -= 10
        no += 1
    while m-5 >= 0:
        m -= 5
        no += 1
    no += m
    return no


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
