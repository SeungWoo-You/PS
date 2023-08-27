import sys
from itertools import combinations


def main():
    global N, S, ls
    N, S = map(int, input().split())
    ls = list(map(int, input().split()))

    count = 0
    for i in range(1, N + 1):
        for pack in combinations(ls, i):
            if sum(pack) == S:
                count += 1
    print(count)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
