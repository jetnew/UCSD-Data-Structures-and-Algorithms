# python3
import time
import sys
import random

def get_hash_sum(s, x, m):
    n = len(s)
    h = [0]
    for i in range(1, n+1):
        val = (x * h[i-1] % m + ord(s[i-1]) % m) % m
        h.append(val)
    return h

def get_hash(h, a, l, x, m):
    return h[a+l]%m - (pow(x,l,m) * h[a]%m)%m

class Solver:
    def __init__(self, s):
        self.s = s
        self.x = random.randint(1, pow(10,9))
        self.m1 = pow(10,9) + 7  # prime number above 500K
        self.m2 = pow(10,9) + 9
        self.h1 = get_hash_sum(s, self.x, self.m1)
        self.h2 = get_hash_sum(s, self.x, self.m2)

    def ask(self, a, b, l):
        hash1a = get_hash(self.h1, a, l, self.x, self.m1)
        # print(hash1a % self.m1)
        # print(try_hash(self.h1, a, l, self.x, self.m1))
        hash1b = get_hash(self.h1, b, l, self.x, self.m1)

        hash2a = get_hash(self.h2, a, l, self.x, self.m2)
        hash2b = get_hash(self.h2, b, l, self.x, self.m2)

        # print(hash1a, hash1b)
        # print(hash2a, hash2b)

        return (hash1a % self.m1 == hash1b % self.m1
                and hash2a % self.m2 == hash2b % self.m2)

s = sys.stdin.readline()
q = int(sys.stdin.readline())
# s = "trololo"
# q = 4
solver = Solver(s)
# _a = [0,2,3,1]
# _b = [0,4,5,3]
# _l = [7,3,1,2]
for i in range(q):
    a, b, l = map(int, sys.stdin.readline().split())
    # a, b, l = _a[i], _b[i], _l[i]
    print("Yes" if solver.ask(a, b, l) else "No")
