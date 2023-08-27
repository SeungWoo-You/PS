import sys


def main():
    N, K = map(int, input().split())
    values = [int(input()) for _ in range(N)]
    res = 0
    now = K
    for coin in reversed(values):
        if now == 0:
            break
        elif now >= coin:
            quot, rem = divmod(now, coin)
            res += quot
            now = rem
    print(res)


if __name__ == "__main__":
    input = sys.stdin.readline
    main()
