import sys
from itertools import product
from collections import deque


def main():
    cards = input().strip().split()
    clock_num = find_clock(cards)
    possibles: set[str] = set()
    for T in product(map(str, range(1, 10)), repeat=4):
        possibles.add(find_clock(T))
    P = sorted(possibles)
    print(P.index(clock_num) + 1)


def find_clock(C: list[str]) -> str:
    Q = deque(C)
    possibles = []
    for _ in range(4):
        possibles.append(''.join(Q))
        Q.appendleft(Q.pop())
    return min(possibles)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
