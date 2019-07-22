# Uses python3
import sys


def primitive_dp(n):
    lookup = []
    i = 1
    while i <= n:
        if i == 1:
            lookup.append(0)
        else:
            choice = []

            if i >= 2 and i % 2 == 0:
                choice.append(lookup[i//2 - 1] + 1)
            if i >= 3 and i % 3 == 0:
                choice.append(lookup[i//3 - 1] + 1)
            if i > 1:
                choice.append(lookup[-1] + 1)
            select = choice.index(min(choice))
            lookup.append(choice[select])
        i += 1

    sequence = [n]
    while n > 1:
        choice = {}
        if n >= 2 and n % 2 == 0:
            choice[lookup[n//2 - 1] + 1] = 0
        if n >= 3 and n % 3 == 0:
            choice[lookup[n//3 - 1] + 1] = 1
        if n > 1:
            choice[lookup[n-1] + 1] = 2
        select = choice[min(choice)]
        if select == 0:
            sequence.append(n//2)
            n //= 2
        if select == 1:
            sequence.append(n//3)
            n //= 3
        if select == 2:
            sequence.append(n-1)
            n -= 1
    return reversed(sequence)


def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)


input = sys.stdin.read()
n = int(input)
# print(primitive_dp(n))
sequence = list(primitive_dp(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
