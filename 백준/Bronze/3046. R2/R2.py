import sys


def main():
    R1, S = map(int, input().split())
    print(S * 2 - R1)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
