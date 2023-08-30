import sys
from itertools import permutations


def main():
    N, M = map(int, input().split())
    seq = list(map(int, input().split()))
    seq.sort()
    checked: set[int] = set()
    for C in permutations(seq, M):
        if C not in checked:
            print(*C)
            checked.add(C)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
