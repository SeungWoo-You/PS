import sys


def main():
    A, B = map(int, input().split())
    C = int(input())
    k = A + B - 2 * C
    print(k if k >= 0 else A + B)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
