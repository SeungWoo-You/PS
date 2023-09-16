from itertools import permutations

def solution(user_id, banned_id):
    answer = 0
    checked: list[set[str]] = []
    for T in permutations(user_id, len(banned_id)):
        for i, name in enumerate(T):
            if len(name) != len(banned_id[i]):
                break
            m = len(name)
            keep = True
            for j in range(m):
                if banned_id[i][j] == '*':
                    continue
                if name[j] != banned_id[i][j]:
                    keep = False
                    break
            if keep == False:
                break
        else:
            S = set(T)
            if S not in checked:
                checked.append(S)
                answer += 1
    return answer