import sys


def main():
    n, k = map(int, input().split())
    coins = sorted([int(input()) for _ in range(n)])

    res = count_coins(coins, k)
    print(res if res != sys.maxsize else -1)


def count_coins(coins: list[int], K: int) -> int:
    counts = [sys.maxsize] * (K + 1)
    counts[0] = 0
    for i in range(1, K + 1):
        for c in coins:
            if i >= c:
                counts[i] = min(counts[i], counts[i - c] + 1)
            else:
                break
    return counts[K]


if __name__ == "__main__":
    input = sys.stdin.readline
    main()
