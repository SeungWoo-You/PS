def solution(n, s):
    quot, rem = divmod(s, n)
    if quot == 0:
        return [-1]
    answer = [quot] * n
    for i in range(n - 1, n - rem - 1, -1):
        answer[i] += 1
    return answer