def solution(absolutes, signs):
    answer = 0
    for x, s in zip(absolutes, signs):
        if s == True:
            answer += x
        else:
            answer -= x
    return answer