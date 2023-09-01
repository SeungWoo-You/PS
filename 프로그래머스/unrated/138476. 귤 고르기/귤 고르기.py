from collections import Counter

def solution(k, tangerine):
    tangerline: list[int]
    count: Counter[int, int] = Counter(tangerine)
    answer = 0
    for num in sorted(count.values(), reverse=True):
        if num >= k:
            answer += 1
            break
        else:
            k -= num
            answer += 1
    return answer