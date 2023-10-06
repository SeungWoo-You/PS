def solution(n):
    if n == 1:
        return '1'
    elif n == 2:
        return '2'
    elif n == 3:
        return '4'
    answer = ''
    for k in range(16, 0, -1):
        T = 3 * (3**k - 1) // 2
        quot, rem = divmod(n, T)
        if quot != 0 and rem != 0:
            break
    n -= T
    for i in range(k, 0, -1):
        quot, rem = divmod(n, 3**i)
        quot = quot if rem != 0 else quot - 1
        if quot == 2 or quot == -1:
            answer += '4'
        elif quot == 1:
            answer += '2'
        elif quot == 0:
            answer += '1'
        n = rem
    if n == 1:
        answer += '1'
    elif n == 2:
        answer += '2'
    elif n == 0:
        answer += '4'
    return answer