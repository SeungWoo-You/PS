from itertools import combinations

def solution(number):
    answer = 0
    for T in combinations(number, 3):
        if sum(T) == 0:
            answer += 1
    return answer