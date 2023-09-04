from collections import defaultdict

def solution(name, yearning, photo):
    name: list[str]
    yearning: list[int]
    photo: list[list[str]]
    scores: defaultdict[str, int] = defaultdict(int)
    scores.update({n: y for n, y in zip(name, yearning)})
    answer = [sum([scores[x] for x in ls]) for ls in photo]
    return answer