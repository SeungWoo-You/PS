import heapq

def solution(jobs):
    answer = 0
    H: list[tuple[int, int]] = []
    N = len(jobs)
    start, end, done = -1, 0, 0
    while done < N:
        for work in jobs:
            if start < work[0] <= end:
                heapq.heappush(H, (work[1], work[0]))
        if H:
            ing = heapq.heappop(H)
            start = end
            end += ing[0]
            answer += end - ing[1]
            done += 1
        else:
                end += 1
    answer //= N
    return answer