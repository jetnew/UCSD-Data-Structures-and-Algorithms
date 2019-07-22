# Uses python3
import sys
import itertools


def partition3(A):
    if sum(A) % 3 != 0:
        return 0

    one_third = sum(A) / 3
    x, y, z = one_third, one_third, one_third

    def helper(A, x, y, z):
        if x == 0 and y == 0 and z == 0:
            return 1
        if x < 0 or y < 0 or z < 0:
            return 0
        return max(helper(A[1:], x-A[0], y, z),
                   helper(A[1:], x, y-A[0], z),
                   helper(A[1:], x, y, z-A[0]))

    return helper(A, x, y, z)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))

    # tests = [
    #     "4 3 3 3 3",
    #     "1 40",
    #     "13 1 2 3 4 5 5 7 7 8 10 12 19 25",
    #     "11 17 59 34 57 17 23 67 1 18 2 59",
    #     "4 1 1 2 2",
    #     "5 3 1 1 2 2",
    # ]
    # for input in tests:
    #     n, *A = list(map(int, input.split()))
    #     print(partition3(A))

