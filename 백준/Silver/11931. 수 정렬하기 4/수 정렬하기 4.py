import sys


def main():
    N = int(input())
    ls = [int(input()) for _ in range(N)]
    print(*sorted(ls, reverse=True), sep='\n')


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
