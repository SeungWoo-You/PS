def solution(players, callings):
    answer = players.copy()
    D: dict[str, int] = {p: i for i, p in enumerate(players)}
    for c in callings:
        i = D[c]
        answer[i], answer[i - 1] = answer[i - 1], answer[i]
        D[c] = i - 1
        D[answer[i]] = i
    return answer