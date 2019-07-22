# Uses python3
import sys


def binary_search(a, x, index):
    # if len(a) == 0:
    #     return -1
    #
    # left, right = 0, len(a)
    # mid = (left + right) // 2
    #
    # if x == a[mid]:
    #     return index+mid
    # elif x > a[mid]:
    #     return binary_search(a[mid+1:], x, index+mid+1)
    # else:
    #     return binary_search(a[:mid], x, index+0)

    left, right = 0, len(a)

    while left < right:
        mid = (left + right) // 2
        if x == a[mid]:
            return mid
        if x > a[mid]:
            left = mid + 1
        else:
            right = mid
    return -1


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x, 0), end = ' ')
