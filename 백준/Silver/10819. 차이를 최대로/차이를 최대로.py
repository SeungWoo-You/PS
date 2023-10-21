import sys
from itertools import permutations


def main():
    N = int(input())
    A = list(map(int, input().split()))
    M = 0
    for T in permutations(A):
        S = 0
        for i in range(1, N):
            S += abs(T[i] - T[i - 1])
        M = max(M, S)
    print(M)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
