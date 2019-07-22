# Uses python3
import sys


def get_change(m):

    num = []

    for i in range(m+1):
        # print(i)
        if i == 0:
            num.append(0)
        else:
            choice = []
            if i >= 1:
                choice.append(num[-1] + 1)
            if i >= 3:
                choice.append(num[-3] + 1)
            if i >= 4:
                choice.append(num[-4] + 1)
            # print(choice)
            smallest = choice.index(min(choice))

            num.append(choice[smallest])

    return num[-1]


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
