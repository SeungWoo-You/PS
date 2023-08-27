import sys


def main():
    N = int(input())
    for i in range(N):
        space = ' ' * i
        print(space + '*' * (2 * (N - i) - 1))
    for i in range(N - 2, -1, -1):
        space = ' ' * i
        print(space + '*' * (2 * (N - i) - 1))


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
