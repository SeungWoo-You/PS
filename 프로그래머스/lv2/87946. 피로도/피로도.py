from itertools import permutations
import sys


def solution(k, dungeons):
    answer = -1
    for T in permutations(dungeons):
        now = k
        temp  = 0
        for n, m in T:
            if now < n:
                break
            now -= m
            temp += 1
        answer = max(answer, temp)
    return answer