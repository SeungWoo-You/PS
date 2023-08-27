import sys
from decimal import Decimal
from math import floor


def main():
    X, Y = map(int, input().split())
    Z = calc_winrate(X, Y)
    start, end = 0, sys.maxsize
    while start <= end:
        mid = (start + end) // 2
        if Z < calc_winrate(X + mid, Y + mid):
            end = mid - 1
        else:
            start = mid + 1
    if start >= sys.maxsize:
        print(-1)
    else:
        print(start)


def calc_winrate(X: int, Y: int) -> int:
    return floor(Decimal(Y) / Decimal(X) * 100)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
