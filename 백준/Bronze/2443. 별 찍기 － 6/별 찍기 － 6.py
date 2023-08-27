import sys


def main():
    N = int(input())
    for i in range(N, 0, -1):
        space = ' ' * (N - i)
        print(space + '*' * (2 * i - 1))


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
