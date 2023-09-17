def solution(s):
    m = len(s) // 2
    if len(s) % 2 == 0:
        m
        return s[m - 1: m + 1]
    return s[m]