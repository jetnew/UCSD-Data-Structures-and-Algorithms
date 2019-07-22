# Uses python3
def edit_distance(s, t):
    s = ' ' + s
    t = ' ' + t
    len_s = len(s)   # s is row
    len_t = len(t)   # t is col

    # Initialise lookup table
    lookup = [[i]+[0]*(len_t-1) for i in range(len_s)]
    lookup[0] = [i for i in range(len_t)]

    for i in range(len_s):
        for j in range(len_t):
            if i > 0 and j > 0:
                if s[i] == t[j]:
                    lookup[i][j] = lookup[i-1][j-1]
                else:
                    a = lookup[i-1][j] + 1
                    b = lookup[i][j-1] + 1
                    c = lookup[i-1][j-1] + 1
                    lookup[i][j] = min(a, b, c)
                    # if len(s[:i]) == len(t[:j]):
                    #     d = len(s[:i])
                    #     lookup[i][j] = min(a, b, c, d)
                    # else:
                    #     lookup[i][j] = min(a, b, c)

    # for row in lookup:
    #     print(row)
    return lookup[-1][-1]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
