import sys


def main():
    N = int(input())
    wine: list[int] = [int(input()) for _ in range(N)]
    dp: list[list[int]] = [[0] * 3 for _ in range(N)]
    dp[0][1] = wine[0]
    for i in range(1, N):
        dp[i][1] = dp[i - 1][0] + wine[i]
        dp[i][2] = dp[i - 1][1] + wine[i]
        dp[i][0] = max(dp[i - 1])
    print(max(dp[-1]))


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
