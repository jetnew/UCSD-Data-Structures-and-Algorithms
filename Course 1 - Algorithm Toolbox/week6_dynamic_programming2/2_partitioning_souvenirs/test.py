import itertools


arr = [1,1,1,3,3,3]
perms = list(itertools.permutations(arr[:6], 3))
perms = list(set([sum(perm) for perm in perms]))
print(perms)

perms = list(itertools.permutations(arr[:6], 2))
perms = list(set([sum(perm) for perm in perms]))
print(perms)

perms = list(itertools.permutations(arr[:6], 1))
perms = list(set([sum(perm) for perm in perms]))
print(perms)