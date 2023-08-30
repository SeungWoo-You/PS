import sys
from itertools import permutations


def main():
    N, M = map(int, input().split())
    seq = list(map(int, input().split()))
    seq.sort()
    for C in permutations(seq, M):
        print(*C)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
