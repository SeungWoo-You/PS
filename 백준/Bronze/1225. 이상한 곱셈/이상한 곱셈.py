import sys
from itertools import product


def main():
    A, B = input().split()
    A, B = list(A), list(B)
    A, B = list(map(int, A)), list(map(int, B))
    S = 0
    for a, b in product(A, B):
        S += a * b
    print(S)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
