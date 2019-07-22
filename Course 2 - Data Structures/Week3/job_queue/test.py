import heapq

arr = [5,7,9,1,3]
# arr = [(5,2), (7,3), (9,4), (1,3), (3,4)]
heapq.heapify(arr)
print(heapq.heappop(arr))
print(list(arr))