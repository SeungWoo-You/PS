import sys


def main():
    N = int(input())
    for _ in range(N):
        x = int(input())
        print('even' if x % 2 == 0 else 'odd')


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
