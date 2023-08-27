import sys
from collections import defaultdict
from itertools import product


def main():
    N, M = map(int, input().split())
    seq = list(map(int, input().split()))
    res = [0]
    for i, x in enumerate(seq):
        res.append(res[i] + x)

    for _ in range(M):
        src, dst = map(int, input().split())
        print(res[dst] - res[src - 1])


if __name__ == "__main__":
    input = sys.stdin.readline
    main()
