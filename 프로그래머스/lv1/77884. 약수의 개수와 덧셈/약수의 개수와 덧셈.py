def solution(left, right):
    answer = 0
    for x in range(left, right + 1):
        count = 0
        for n in range(1, x + 1):
            if x % n == 0:
                count += 1
        if count % 2 == 0:
            answer += x
        else:
            answer -= x
    return answer