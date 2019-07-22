# Uses python3
import sys
import random


def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)

    return number_of_inversions


def mergesort(a):
    assert type(a) is list
    # print(a)
    invs = 0
    if a is [] or len(a) == 1:
        return a, 0

    m = len(a)//2
    # print("arrays before 1st and 2nd MS", a[:m], a[m:])
    x, i1 = mergesort(a[:m])
    # print("inversions in 1st MS", i1)
    y, i2 = mergesort(a[m:])
    # print("inversions in 2nd MS", i2)
    # print("arrays after 1st & 2nd MS", x,y)
    a, i3 = merge(x, y)
    # print("inversions in Merge", i3)
    invs += i1 + i2 + i3
    # print("total inversions from 1 merge sort", invs)
    return a, invs


def merge(x, y):
    assert type(x) is list
    assert type(y) is list
    lst = []
    i = 0
    z = len(x) + len(y)
    # print(x, y)
    for _ in range(z):
        if not x:
            lst += y
            break
        elif not y:
            lst += x
            break
        if x[0] < y[0]:
            lst.append(x.pop(0))
        elif x[0] > y[0]:
            i += len(x)
            # print(i)
            lst.append(y.pop(0))
            # i += 1
        else:
            lst.append(x.pop(0))
            # lst.append(y.pop(0))
    return lst, i


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    # print(get_number_of_inversions(a, b, 0, len(a)))
    # a = [9,8,7,3,2,1]
    print(mergesort(a)[1])