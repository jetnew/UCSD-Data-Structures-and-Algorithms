# Uses python3
import sys
import random


def fast_count_segments(starts, ends, points):
    start_pairs = [(i, 'l') for i in starts]
    end_pairs = [(i, 'r') for i in ends]
    point_pairs = [(i, 'p') for i in points]

    pairs = start_pairs + end_pairs + point_pairs
    randomized_quick_sort(pairs, 0, len(pairs)-1)

    count_list = []
    segs = 0
    for i in pairs:
        if i[1] == 'l':
            segs += 1
        elif i[1] == 'r':
            segs -= 1
        elif i[1] == 'p':
            count_list.append(segs)

    count_dict = {}
    for i, j in enumerate(sorted(points)):
        count_dict[j] = count_list[i]

    cnt = []
    for i in points:
        cnt.append(count_dict[i])
    return cnt


def partition3(a, l, r):
    x_num = a[l][0] # left-most element in array
    x_type = a[l][1]
    j = l  # index of left element
    k = r
    i = l+1
    # print(a)
    while i < k+1:
        # print("Index", i, ":", a[i])
        if a[i][0] < x_num: # if curr element is smaller than selected elem
            j += 1 # go to next index
            a[i], a[j] = a[j], a[i] # swap them
        elif a[i][0] > x_num:
            a[i], a[k] = a[k], a[i]
            k -= 1
            i -= 1
        elif a[i][0] == x_num:
            if a[i][1] < x_type:
                j += 1
                a[i], a[j] = a[j], a[i]
            elif a[i][1] > x_type:
                a[i], a[k] = a[k], a[i]
                k -= 1
                i -= 1
        i+=1
        # print(a, j, k)
    a[l], a[j] = a[j], a[l] # put the element in the right position
    a[r], a[k] = a[k], a[r]
    return j, k


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    j = random.randint(l, r)
    a[l], a[j] = a[j], a[l]
    # print("---Selected=", a[l])
    m1, m2 = partition3(a, l, r)
    randomized_quick_sort(a, l, m1-1)
    randomized_quick_sort(a, m2, r)


def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')




    # points = [3]
    # pairs = [(3, 'p'), (3, 'l'), (3, 'r')]
    # randomized_quick_sort(pairs, 0, len(pairs)-1)
    # print(pairs)
    # count_list = []
    # segs = 0
    # for i in pairs:
    #     if i[1] == 'l':
    #         segs += 1
    #         print(segs)
    #     elif i[1] == 'r':
    #         segs -= 1
    #         print(segs)
    #     if i[1] == 'p':
    #         count_list.append(segs)
    # count_dict = {}
    # for i, j in enumerate(sorted(points)):
    #     count_dict[j] = count_list[i]
    #
    # print(count_dict)
