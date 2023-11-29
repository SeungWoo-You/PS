import sys


def main():
    A, B, C = map(int, input().split())
    if C > B:
        print(A // (C - B) + 1)
    else:
        print(-1)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
