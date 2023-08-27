import sys
from collections import Counter


def main():
    N, M = map(int, input().split())
    words = [input().strip() for _ in range(N)]
    count = Counter(words)
    memo = sorted(count.items(), key=lambda p: (-p[1], -len(p[0]), p[0]))
    for item in memo:
        if len(item[0]) >= M:
            print(item[0])


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
