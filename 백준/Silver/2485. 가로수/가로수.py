import sys
from math import gcd


def main():
    N = int(input())
    tree = [int(input()) for _ in range(N)]
    diff: list[int] = []
    t1 = tree[0]
    for i in range(1, N):
        t2 = tree[i]
        diff.append(t2 - t1)
        t1 = t2
    space = gcd(*diff)
    print(sum([x // space - 1 for x in diff]))


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
