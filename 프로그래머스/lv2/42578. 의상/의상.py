from collections import defaultdict

def solution(clothes):
    clothes: list[list[str]]
    fashion: defalutdict[str, set[str]] = defaultdict(set)
    for item, part in clothes:
        fashion[part].add(item)
    answer = 1
    print(fashion)
    for S in fashion.values():
        answer *= (len(S) + 1)
    return answer - 1