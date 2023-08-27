import sys


def main():
    N = int(input())
    for i in range(N):
        space = ' ' * (N - i - 1)
        print(space + '*' * (2 * i + 1))


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
