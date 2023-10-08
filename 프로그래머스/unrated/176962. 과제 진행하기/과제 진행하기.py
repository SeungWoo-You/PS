def solution(plans):
    answer = []
    ls = []
    for P in plans:
        work, s, e = P
        T = list(map(int, s.split(':')))
        start = T[0] * 60 + T[1]
        playtime = int(e)
        ls.append([work, start, playtime])
    ls.sort(key=lambda p: p[1])
    S = [ls[0]]
    now = ls[0][1]
    for i in range(1, len(ls)):
        start = ls[i][1]
        while S:
            h, t, q = S.pop()
            if t > now:
                now = t
            if now + q <= start:
                now += q
                answer.append(h)
            else:
                S.append([h, t, q - (start - now)])
                now = start
                break
        S.append(ls[i])
    while S:
        answer.append(S.pop()[0])
    return answer