from collections import deque

def solution(targets):
    Q = deque(sorted(targets, key=lambda p: p[1]))
    answer = 0
    while Q:
        _, r = Q.popleft()
        answer += 1
        shoot = r
        while Q:
            i, j = Q[0]
            if i < shoot <= j:
                Q.popleft()
            else:
                break
    return answer