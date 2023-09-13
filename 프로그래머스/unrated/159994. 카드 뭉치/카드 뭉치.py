from collections import deque

def solution(cards1, cards2, goal):
    C1: deque[str] = deque(cards1)
    C2: deque[str] = deque(cards2)
    i = 0
    while i < len(goal):
        if C1 and C1[0] == goal[i]:
            C1.popleft()
            i += 1
        elif C2 and C2[0] == goal[i]:
            C2.popleft()
            i += 1
        else:
            return 'No'
    return 'Yes'