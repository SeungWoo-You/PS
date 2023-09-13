from itertools import permutations
from math import sqrt, ceil

def solution(numbers):
    answer = 0
    checked: set[int] = set()
    for r in range(1, len(numbers) + 1):
        for T in permutations(numbers, r):
            x = int(''.join(T))
            if x in checked:
                continue
            checked.add(x)
            if x == 1 or x == 0:
                continue
            if x == 2:
                answer += 1
                continue
            for d in range(2, ceil(sqrt(x)) + 1):
                if x % d == 0:
                    break
            else:
                answer += 1
    return answer