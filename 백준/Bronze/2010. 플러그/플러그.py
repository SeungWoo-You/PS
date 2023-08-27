import sys


def main():
    N = int(input())
    count = sum([int(input()) for _ in range(N)]) - (N - 1)
    print(count)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
