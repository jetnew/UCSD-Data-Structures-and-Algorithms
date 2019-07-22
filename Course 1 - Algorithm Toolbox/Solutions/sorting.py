# Uses python3
import sys
import random


def partition3(a, l, r):
    x = a[l] # left-most element in array
    j = l  # index of left element
    k = r
    i = l+1
    # print(a)
    while i < k+1:
        # print("Index", i, ":", a[i])
        if a[i] < x: # if curr element is smaller than selected elem
            j += 1 # go to next index
            a[i], a[j] = a[j], a[i] # swap them
        elif a[i] > x:
            a[i], a[k] = a[k], a[i]
            k -= 1
            i -= 1
        i+=1
        # print(a, j, k)
    a[l], a[j] = a[j], a[l] # put the element in the right position
    a[r], a[k] = a[k], a[r]
    return j, k


def partition2(a, l, r):
    x = a[l] # element in array
    j = l;  # index of element
    for i in range(l + 1, r + 1): # for all subsequent elements
        if a[i] <= x: # if curr element is smaller than selected elem
            j += 1 # go to next index
            a[i], a[j] = a[j], a[i] # swap them
    a[l], a[j] = a[j], a[l] # put the element in the right position
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    j = random.randint(l, r)
    a[l], a[j] = a[j], a[l]
    # print("---Selected=", a[l])
    m1, m2 = partition3(a, l, r)
    randomized_quick_sort(a, l, m1-1)
    randomized_quick_sort(a, m2, r)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n-1)
    for x in a:
        print(x, end=" ")

    # sort = True
    # while sort:
    #     print("New---------------------------------------------")
    #     a = [random.randint(0,9) for i in range(8)]
    #     n = len(a)
    #     print("Begin:", a)
    #
    #     randomized_quick_sort(a, 0, n - 1)
    #
    #     if a != sorted(a):
    #         sort = False
    #         print("End:", a)