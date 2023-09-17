def solution(s):
    answer = 0
    x = s[0]
    count_x = 1
    count_else = 0
    for i in range(1, len(s)):
        if count_x == count_else:
            answer += 1
            x = s[i]
            count_x = 1
            count_else = 0
        else:
            if s[i] == x:
                count_x += 1
            else:
                count_else += 1
    answer += 1
    return answer