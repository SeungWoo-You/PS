import sys
from itertools import product


def main():
    N, M = map(int, input().split())
    for seq in product(range(1, N + 1), repeat=M):
        print(*seq)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
