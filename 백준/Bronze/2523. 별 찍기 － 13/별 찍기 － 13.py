import sys


def main():
    N = int(input())
    for i in range(1, N + 1):
        print('*' * i)
    for i in range(N - 1, 0, -1):
        print('*' * i)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
