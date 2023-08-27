import sys
from itertools import permutations


def main():
    n = int(input())
    k = int(input())
    checked: set[str] = set()
    cards = [input().strip() for _ in range(n)]
    for X in permutations(cards, k):
        num = ''.join(X)
        checked.add(num)
    print(len(checked))


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
