import sys


def main():
    N = int(input())
    for i in range(1, N + 1):
        space = ' ' * 2 * (N - i)
        star = '*' * i
        print(star + space + star)
    for i in range(N - 1, 0, -1):
        space = ' ' * 2 * (N - i)
        star = '*' * i
        print(star + space + star)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
