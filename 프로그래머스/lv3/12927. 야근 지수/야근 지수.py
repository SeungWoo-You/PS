import heapq

def solution(n, works):
    answer = 0
    H: list[int] = [-w for w in works]
    heapq.heapify(H)
    for _ in range(n):
        t = heapq.heappop(H)
        if t == 0:
            return 0
        heapq.heappush(H, t + 1)
    while H:
        x = heapq.heappop(H)
        if x == 0:
            break
        answer += x**2
    return answer