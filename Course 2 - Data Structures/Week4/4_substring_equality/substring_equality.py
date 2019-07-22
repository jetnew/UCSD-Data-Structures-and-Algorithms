# python3

import sys
import random

def get_prefixes(s, x, m):
    n = len(s)
    prefixes = []
    for i in range(n):
        # print(ord(s[j])*(x**(m-j-1)))
        # print(ord(s[j]))
        val = 0
        for j in range(i+1):
            val += ord(s[j])*(x**(i-j-1))
        prefixes.append(val)
    return prefixes

def get_hash(prefixes, a, l, x):
    return prefixes[a+l-1] - (x**l)*prefixes[a-1]

def get_hash_sum(s, x, m):
    n = len(s)
    h = [0]
    for i in range(1, n+1):
        h.append((x * h[i-1] + ord(s[i-1])) % m)
    return h

def get_hash(h, a, l, x):
    return h[a+l] - (x**l) * h[a]

class Solver:
    def __init__(self, s):
        self.s = s
        self.x = random.randint(1, 10**9)
        self.m1 = 10**9 + 7  # prime number above 500K
        self.m2 = 10**9 + 9
        # self.h1 = get_prefixes(s, self.x, self.m1)
        # self.h2 = get_prefixes(s, self.x, self.m2)
        # print(self.prefixes)
        # print(self.h1)
        self.h1 = get_hash_sum(s, self.x, self.m1)
        # print(self.h1)
        self.h2 = get_hash_sum(s, self.x, self.m2)

    def ask(self, a, b, l):
        hash1a = get_hash(self.h1, a, l, self.x)
        hash1b = get_hash(self.h1, b, l, self.x)

        hash2a = get_hash(self.h2, a, l, self.x)
        hash2b = get_hash(self.h2, b, l, self.x)

        # print(hash1a, hash1b)
        # print(hash2a, hash2b)
        return (hash1a % self.m1 == hash1b % self.m1
                and hash2a % self.m2 == hash2b % self.m2)

        # return s[a:a+l] == s[b:b+l]


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
