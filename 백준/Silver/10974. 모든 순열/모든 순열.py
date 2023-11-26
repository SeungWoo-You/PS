import sys
from itertools import permutations


def main():
    N = int(input())
    for T in permutations(range(1, N + 1)):
        print(*T)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
