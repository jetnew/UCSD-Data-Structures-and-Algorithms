# Uses python3
n = int(input())
a = [int(x) for x in input().split()]

lst = sorted(a)
print(lst[-1]*lst[-2])
