def solution(ingredient):
    S: list[int] = []
    answer = 0
    for x in ingredient:
        S.append(x)
        if x == 1:
            while len(S) >= 4:
                if S[-1] == 1 and S[-2] == 3 and S[-3] == 2 and S[-4] == 1:
                    answer += 1
                    for _ in range(4):
                        S.pop()
                else:
                    break
    return answer