from math import sqrt

def solution(k, d):
    answer = 0
    for x in range(0, d + 1, k):
        y2 = d**2 - x**2
        possible = sqrt(y2) // k + 1
        answer += possible
    return answer