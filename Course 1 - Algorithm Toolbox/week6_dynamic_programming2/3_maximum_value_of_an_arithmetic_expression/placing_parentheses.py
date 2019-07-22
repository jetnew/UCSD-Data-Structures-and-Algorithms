# Uses python3
def evalt(a, b, op):
    a = int(a)
    b = int(b)
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


def get_maximum_value(s):
    def min_max(i, j):
        _min = 99999999999999  # float('inf')
        _max = -99999999999999  # -float('inf')
        for k in range(i, j):
            a = evalt(M[i][k], M[k+1][j], ops[k])
            b = evalt(M[i][k], m[k+1][j], ops[k])
            c = evalt(m[i][k], M[k + 1][j], ops[k])
            d = evalt(m[i][k], m[k + 1][j], ops[k])
            _min = min(_min, a, b, c, d)
            _max = max(_max, a, b, c, d)
        return (_min, _max)

    num = [None] + [s[i] for i in range(0, len(s), 2)]
    ops = [None] + [s[i] for i in range(1, len(s), 2)]
    n = (len(s)+1)//2

    M = [[0 for _ in range(n+1)] for _ in range(n+1)]
    m = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        M[i][i] = num[i]
        m[i][i] = num[i]

    for i in range(1, n+1):
        for j in range(1, n+1-i):
            k = i+j
            m[j][k], M[j][k] = min_max(j, k)
    # for r in M:
    #     print(r)
    return M[1][n]


if __name__ == "__main__":
    # input = "5-8+7*4-8+9"
    print(get_maximum_value(input()))
