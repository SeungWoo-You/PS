import sys


def main():
    while True:
        N, M = map(int, input().split())
        if (N, M) == (0, 0):
            return
        C1 = {int(input()) for _ in range(N)}
        C2 = {int(input()) for _ in range(M)}
        print(len(C1 & C2))


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
