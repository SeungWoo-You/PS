import sys


def main():
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        _ = [input() for _ in range(M)]
        print(N - 1)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
