import sys
from decimal import Decimal
from math import floor


def main():
    N = int(input())
    k = 0
    while N > 0:
        n = Decimal(N)
        t = floor(((1 + 8 * n).sqrt() - 1) / 2)
        N -= t * (t + 1) // 2
        k += t
    print(k)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
