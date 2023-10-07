import heapq

def solution(book_time):
    times = []
    answer = 1
    for s, e in book_time:
        S = list(map(int, s.split(':')))
        m1 = S[0] * 60 + S[1]
        E = list(map(int, e.split(':')))
        m2 = E[0] * 60 + E[1]
        times.append([m1, m2])
    times.sort()
    rooms: list[int] = []
    for start, end in times:
        if not rooms:
            heapq.heappush(rooms, end)
            continue
        if rooms[0] <= start:
            heapq.heappop(rooms)
        else:
            answer += 1
        heapq.heappush(rooms, end + 10)
    return answer