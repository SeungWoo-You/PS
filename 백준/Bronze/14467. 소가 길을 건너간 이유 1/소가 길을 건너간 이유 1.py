import sys
from collections import defaultdict


def main():
    N = int(input())
    detection: defaultdict[int, list[int]] = defaultdict(list)
    for _ in range(N):
        cow, pos = map(int, input().split())
        detection[cow].append(pos)

    count = 0
    for ls in detection.values():
        prev = ls[0]
        for p in ls:
            if p != prev:
                count += 1
            prev = p
    print(count)


if __name__ == "__main__":
    input = sys.stdin.readline
    main()
