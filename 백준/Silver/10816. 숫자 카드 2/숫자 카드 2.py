from collections import defaultdict


def main():
    N = int(input())
    hands = list(map(int, input().split()))
    M = int(input())
    given = list(map(int, input().split()))

    counts = defaultdict(int)
    for x in hands:
        counts[x] += 1
    for v in given:
        print(counts[v], end=' ')


if __name__ == '__main__':
    main()
