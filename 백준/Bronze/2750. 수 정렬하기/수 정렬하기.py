import sys


def main():
    N = int(input())
    ls = [int(input()) for _ in range(N)]
    ls.sort()
    print(*ls, sep='\n')


if __name__ == "__main__":
    input = sys.stdin.readline
    main()
