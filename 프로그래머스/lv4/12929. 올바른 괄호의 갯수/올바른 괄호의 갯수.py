def solution(n):
    answer = 0
    dp = [1, 1, 2]
    while len(dp) < n + 1:
        k = len(dp) - 1
        count = sum([dp[i] * dp[k - i] for i in range(k + 1)])
        dp.append(count)
    return dp[n]