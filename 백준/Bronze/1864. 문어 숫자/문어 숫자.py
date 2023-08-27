import sys


def main():
    S = input().rstrip('\n')
    trans_table = {
        '-': 0,
        '\\': 1,
        '(': 2,
        '@': 3,
        '?': 4,
        '>': 5,
        '&': 6,
        '%': 7,
        '/': -1
    }

    while S != '#':
        ls = list(S)
        num = 0
        n = len(ls)
        for j, x in enumerate(ls, start=1):
            num += trans_table[x] * 8**(n - j)
        print(num)
        S = input().rstrip('\n')


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
