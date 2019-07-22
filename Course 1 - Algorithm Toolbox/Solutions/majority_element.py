# Uses python3
import sys


def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]

    count = {}
    for num in a:
        if num not in count:
            count[num] = 1
        else:
            count[num] += 1
        if count[num] > len(a)/2:
            return 0
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
