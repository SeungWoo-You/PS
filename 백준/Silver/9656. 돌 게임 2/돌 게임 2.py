import sys


def main():
    N = int(input())
    print('SK' if N % 2 == 0 else 'CY')


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
