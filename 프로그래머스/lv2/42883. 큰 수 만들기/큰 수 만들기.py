def solution(number, k):
    answer = ''
    S = []
    rm = 0
    for n in number:
        while S:
            if rm == k:
                break
            if int(n) > int(S[-1]):
                S.pop()
                rm += 1
            else:
                break
        S.append(n)
    for _ in range(rm, k):
        S.pop()
    return ''.join(S)