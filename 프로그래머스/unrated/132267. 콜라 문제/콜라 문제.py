def solution(a, b, n):
    answer = 0
    while n >= a:
        quot, rem = divmod(n, a)
        answer += b * quot
        n = b * quot + rem
    return answer