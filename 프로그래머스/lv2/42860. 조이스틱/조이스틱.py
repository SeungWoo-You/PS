def solution(name):
    answer = 0
    N = len(name)
    m = N - 1
    for i, C in enumerate(name):
        answer += min(ord(C) - ord('A'), ord('Z') - ord(C) + 1)
        j = i + 1
        while j < N and name[j] == 'A':
            j += 1
        rem = N - j
        m = min(m, i + i + rem, i + rem + rem)
    return answer + m