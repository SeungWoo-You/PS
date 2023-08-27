import sys


def main():
    N = int(input())
    for n in range(N, 0, -1):
        print('*' * n)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
