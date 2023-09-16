def solution(s):
    answer = []
    S = trans(s)
    S.sort(key=lambda p:len(p))
    checked: set[str] = set()
    for T in S:
        tp = set(list(T))
        tp -= checked
        x: str = tp.pop()
        answer.append(int(x))
        checked.add(x)
    return answer

def trans(S: str) -> list:
    res: list[list[int]] = [[]]
    stack: list[str] = []
    num = ''
    for x in S:
        if x == '{':
            stack.append(x)
        elif x == '}':
            stack.pop()
            res[-1].append(num)
            res.append([])
            num = ''
        elif x == ',' and num != '':
            res[-1].append(num)
            num = ''
        elif x == ',':
            continue
        else:
            num += x
    res.pop()
    res.pop()
    return res