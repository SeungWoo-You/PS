import sys
from math import factorial


def main():
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        count = factorial(M) // (factorial(M - N) * factorial(N))
        print(count)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
