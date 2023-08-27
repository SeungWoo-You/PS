import sys


def main():
    ls = map(int, input().split())
    print(*sorted(ls))


if __name__ == "__main__":
    input = sys.stdin.readline
    main()
