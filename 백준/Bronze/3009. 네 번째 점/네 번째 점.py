import sys
from collections import Counter


def main():
    pts = [tuple(map(int, input().split())) for _ in range(3)]
    X = Counter([x for x, _ in pts])
    Y = Counter([y for _, y in pts])
    ans = [0, 0]
    for x, v in X.items():
        if v == 1:
            ans[0] = x
            break
    for y, v in Y.items():
        if v == 1:
            ans[1] = y
            break
    print(*ans)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
