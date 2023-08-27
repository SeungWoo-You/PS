import sys
from collections import Counter


def main():
    T = int(input())
    for _ in range(T):
        n = int(input())

        ls = [input().strip().split()[-1] for _ in range(n)]

        counter = Counter(ls)
        res = 1
        for c in counter.values():
            res *= (c + 1)
        print(res - 1)


if __name__ == "__main__":
    input = sys.stdin.readline
    main()
