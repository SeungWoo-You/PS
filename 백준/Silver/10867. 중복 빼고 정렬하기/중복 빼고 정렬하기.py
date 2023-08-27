import sys


def main():
    N = int(input())
    ls = set(map(int, input().split()))
    print(*sorted(ls))


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
