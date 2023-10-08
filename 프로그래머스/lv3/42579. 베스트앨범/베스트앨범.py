def solution(genres, plays):
    answer = []
    D = dict()
    
    for i, T in enumerate(zip(genres, plays)):
        g, p = T
        if g not in D:
            D[g] = [0, []]
        D[g][0] += p
        D[g][1].append((i, p))
    
    for V in sorted(D.values(), key=lambda p: -p[0]):
        _, T = V
        T.sort(key=lambda p: (p[1], -p[0]))
        for _ in range(2):
            if T:
                i, k = T.pop()
                answer.append(i)
    return answer