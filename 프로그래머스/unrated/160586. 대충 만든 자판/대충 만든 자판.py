def solution(keymap, targets):
    keymap: list[str]
    targets: list[str]
    N = len(keymap)
    D: dict[str, int] = {}
    for j in range(101):
        for i in range(N):
            try:
                k = keymap[i][j]
                if k not in D:
                    D[k] = j + 1
            except:
                pass
    print(D)
    answer: list[int] = []
    for cmd in targets:
        try:
            answer.append(sum([D[c] for c in cmd]))
        except:
            answer.append(-1)
    return answer