import sys


def main():
    S = set(range(1, 31))
    checked: set[int] = set([int(input()) for _ in range(28)])
    print(*sorted(S - checked), sep='\n')


if __name__ == '__main__':
    input = sys.stdin.readline
    main()