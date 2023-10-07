import heapq

def solution(scoville, K):
    answer = 0
    H = scoville
    heapq.heapify(H)
    while len(H) > 1 and H[0] < K:
        first = heapq.heappop(H)
        second = heapq.heappop(H)
        heapq.heappush(H, first + second * 2)
        answer += 1
    return answer if H[0] >= K else -1