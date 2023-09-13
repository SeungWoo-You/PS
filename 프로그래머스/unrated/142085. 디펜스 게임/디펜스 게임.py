import heapq

def solution(n, k, enemy):
    H: list[int] = []
    for i, e in enumerate(enemy, start=1):
        heapq.heappush(H, e)
        if len(H) > k:
            n -= heapq.heappop(H)
        if n < 0:
            i -= 1
            break
    return i