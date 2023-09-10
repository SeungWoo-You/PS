import sys


def main():
    N, K = map(int, input().split())
    ls = list(map(int, input().split()))
    ls.sort()
    print(ls[K - 1])


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
