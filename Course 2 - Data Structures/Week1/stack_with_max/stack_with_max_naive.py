#python3
import sys

class StackWithMax():
    def __init__(self):
        self.max = -float('inf')
        self.__stack = []
        self.max_stack = [-float('inf')]

    def Push(self, a):
        if a >= self.max_stack[-1]:
            self.max_stack.append(a)
        self.__stack.append(a)

    def Pop(self):
        assert(len(self.__stack))
        a = self.__stack.pop()
        if a == self.max_stack[-1]:
            self.max_stack.pop()

    def Max(self):
        assert(len(self.__stack))
        return self.max_stack[-1]
        # return max(self.__stack)


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
