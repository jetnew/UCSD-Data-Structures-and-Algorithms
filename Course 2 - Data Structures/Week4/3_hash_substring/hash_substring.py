# python3
import math

def read_input():
    # return ("aba".rstrip(), "abacaba".rstrip())
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def hash(string):
    # val = 0
    # for s in string:
    #     val += ord(s)
    #     val *= 1000
    # val //= 1000
    # return val

    return string

def rehash(hash, next_char, n):
    # remove = hash // 10**((n-1)*3)
    # hash -= remove * 10**((n-1)*3)
    # hash *= 1000
    # hash += ord(next_char)
    # return hash
    return hash[1:] + next_char

def get_occurrences(pattern, text):
    # return [
    #     i
    #     for i in range(len(text) - len(pattern) + 1)
    #     if text[i:i + len(pattern)] == pattern
    # ]
    n = len(pattern)
    results = []
    pattern_hash = hash(pattern)
    sub_hash = hash(text[:len(pattern)])

    i = 0
    while i < len(text) - len(pattern) + 1:
        if pattern_hash == sub_hash:
            # print(pattern, text[i:i+len(pattern)])
            if pattern == text[i:i+len(pattern)]:
                results.append(i)

        if i < len(text) - len(pattern):
            # print(len(text))
            # print(text[i+len(pattern)], i+len(pattern))
            # print("Before:", sub_hash)
            # print(sub_hash)
            sub_hash = rehash(sub_hash, text[i+len(pattern)], n)
            # print("After:", sub_hash)
        i += 1
    return results

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

