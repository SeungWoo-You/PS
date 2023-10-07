import heapq


def solution(picks, minerals):
    answer = 0
    gp = [minerals[5 * i:5 * (i + 1)] for i in range(min(len(minerals) // 5 + 1, sum(picks)))]
    weight: list[int] = []
    for G in gp:
        temp = 0
        for ore in G:
            if ore == 'diamond':
                temp += 25
            elif ore == 'iron':
                temp += 5
            else:
                temp += 1
        weight.append(temp)
    H = [(-w, g) for w, g in zip(weight, gp)]
    heapq.heapify(H)
    for _ in range(picks[0]):
        if not H:
            return answer
        _, G = heapq.heappop(H)
        answer += len(G)
    for _ in range(picks[1]):
        if not H:
            return answer
        _, G = heapq.heappop(H)
        for ore in G:
            if ore == 'diamond':
                answer += 5
            else:
                answer += 1
    for _ in range(picks[2]):
        if not H:
            return answer
        w, _ = heapq.heappop(H)
        answer -= w
    return answer