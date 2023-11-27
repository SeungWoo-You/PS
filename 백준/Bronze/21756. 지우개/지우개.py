import sys


def main():
    N = int(input())
    L = list(range(1, N + 1))
    while len(L) != 1:
        L = L[1::2]
    print(L[0])


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
