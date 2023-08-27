import sys
from collections import defaultdict


def main():
    N = int(input())
    cards = list(map(int, input().split()))
    cards_dict = defaultdict(int)
    for x in cards:
        cards_dict[x] = 1

    M = int(input())
    keys = list(map(int, input().split()))
    for k in keys:
        print(cards_dict[k], end=' ')


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
