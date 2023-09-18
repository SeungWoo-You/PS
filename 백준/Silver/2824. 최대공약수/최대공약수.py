import sys
from math import gcd, prod


def main():
    N = int(input())
    factors_A = list(map(int, input().split()))
    M = int(input())
    factors_B = list(map(int, input().split()))
    A = prod(factors_A)
    B = prod(factors_B)
    Q, R = divmod(gcd(A, B), 10**9)
    if Q != 0:
        print(f'{R:09d}')
    else:
        print(R)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
