import sys
from itertools import combinations_with_replacement


def main():
    N = int(input())
    Roman = [1, 5, 10, 50]
    checked: set[int] = set()
    for T in combinations_with_replacement(Roman, N):
        checked.add(sum(T))
    print(len(checked))


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
