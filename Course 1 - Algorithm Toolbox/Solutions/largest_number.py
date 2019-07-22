#Uses python3

import sys


def largest_number(a):

    answer = ""
    while a:
        max_digit = 0
        for digit in a:
            if int(digit+str(max_digit)) > int(str(max_digit)+digit):
                max_digit = digit
        answer += max_digit
        a.remove(max_digit)
    return answer


if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
