import sys
from math import sqrt


def main():
    M = int(input())
    N = int(input())
    total = 0
    m = sys.maxsize
    for x in range(M, N + 1):
        if sqrt(x).is_integer():
            total += x
            m = min(m, x)
    if m == sys.maxsize:
        print(-1)
    else:
        print(total)
        print(m)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
