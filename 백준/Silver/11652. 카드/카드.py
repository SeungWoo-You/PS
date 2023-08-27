import sys
from collections import Counter


def main():
    N = int(input())
    cards = Counter([int(input()) for _ in range(N)])
    print(sorted(cards.items(), key=lambda p: (-p[1], p[0]))[0][0])


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
