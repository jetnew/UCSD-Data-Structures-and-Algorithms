arr = [5,4,3,2,1]
test = [1,2,3,5,4]

arr = [12,11,13,5,6,7]


def SiftDown(arr, i):
    n = len(arr)
    smallest = i
    l = (2 * i) + 1
    r = (2 * i) + 2
    if l < n and arr[smallest] > arr[l]:
        smallest = l
    if r < n and arr[smallest] > arr[r]:
        smallest = r
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        SiftDown(arr, smallest)

print(arr)

n = len(arr)
for i in range(n, -1, -1):
    print(i)
    SiftDown(arr, i)

print(arr)
# print(test)

