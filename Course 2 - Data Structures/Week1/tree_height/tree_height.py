# python3

import sys
import threading


def fail_compute_height(n, parents):
    def fill_array(i, p):
        if array[i] != 0:
            return
        if p == -1:
            array[i] = 1
            return
        if array[p] == 0:
            fill_array(p, parents[p])
        array[i] = array[p] + 1
    array = [0]*n
    for i, p in enumerate(parents):
        fill_array(i, p)
    return max(array)


def compute_height(n, parents):
    tree = {}
    for c, p in enumerate(parents):
        if p not in tree:
            tree[p] = [c]
        else:
            tree[p].append(c)
    # tree = {-1:[1],1:[2,3,4],2:[],3:[],4:[]}
    # print(tree)
    height = []
    def traverse(i, count):
        if i not in tree:
            return
        height.append(count)
        for p in tree[i]:
            traverse(p, count+1)
    traverse(-1, 1)
    return max(height)


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))
    # n, parents = 5, [4,-1,4,1,1]
    # n, parents = 5, [-1,0,4,0,3]
    # print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
