import sys
from collections import Counter


def main():
    N = int(input())
    count = Counter(map(int, input().split()))
    print(count[int(input())])


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
