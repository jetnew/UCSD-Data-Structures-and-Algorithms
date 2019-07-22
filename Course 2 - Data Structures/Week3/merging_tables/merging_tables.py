# python3

import sys
import threading



def main():

    n, m = map(int, sys.stdin.readline().split())
    lines = list(map(int, sys.stdin.readline().split()))
    # n = 6
    # m = 4
    # lines = [10,0,5,0,3,3]
    rank = [1] * n
    parent = list(range(0, n))
    ans = max(lines)

    def getParent(table):
        # find parent and compress path
        if table == parent[table]:
            return parent[table]

        p = getParent(parent[table])
        setParent(table, p)
        return p

    def setParent(table, p):
        parent[table] = p

    def merge(destination, source):
        realDestination = getParent(destination)
        realSource = getParent(source)
        if realDestination == realSource:
            return False

        # merge two components
        # use union by rank heuristic
        # update ans with the new maximum table size
        # print(source, destination)
        # print(realSource, realDestination)
        if rank[realDestination] < rank[realSource]:
            setParent(realDestination, realSource)
        elif rank[realDestination] > rank[realSource]:
            setParent(realSource, realDestination)
        else:
            rank[realSource] += 1
            setParent(realSource, realDestination)



        new_row = lines[realDestination] + lines[realSource]
        lines[realDestination] = new_row
        lines[realSource] = new_row
        # print(lines)
        nonlocal ans
        if new_row > ans:
            ans = new_row

        return True

    # q = [
    #     [6,6],
    #     [6,5],
    #     [5,4],
    #     [4,3],
    # ]
    for i in range(m):
        destination, source = map(int, sys.stdin.readline().split())
        # destination, source = q[i]
        merge(destination - 1, source - 1)
        print(ans)
    # print(parent)

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()