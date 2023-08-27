import sys
from collections import Counter


def main():
    N = int(input())
    count = Counter([input().strip() for _ in range(N)])
    print(sorted(count.items(), key=lambda p: (-p[1], p[0]))[0][0])


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
