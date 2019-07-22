# python3

class HeapBuilder:
  def __init__(self):
    self._swaps = []
    self._data = []

  def ReadData(self):
    n = int(input())
    self._data = [int(s) for s in input().split()]
    assert n == len(self._data)

  def WriteResponse(self):
    print(len(self._swaps))
    for swap in self._swaps:
      print(swap[0], swap[1])

  def SiftDown(self, i):
      arr = self._data
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
          self._swaps.append((i, smallest))
          self.SiftDown(smallest)

  def GenerateSwaps(self):
    n = len(self._data)
    for i in range(n, -1, -1):
      self.SiftDown(i)

  def Solve(self):
    self.ReadData()
    # print(self._data)
    self.GenerateSwaps()
    # print(self._data)
    self.WriteResponse()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
