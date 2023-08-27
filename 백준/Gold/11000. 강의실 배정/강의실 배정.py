import sys
import heapq


def main():
    N = int(input())
    lectures = [tuple(map(int, input().split())) for _ in range(N)]
    lectures.sort()

    rooms = 0
    ends: list[int] = []
    temp = ends.copy()
    for s, e in lectures:
        while ends and s >= ends[0]:
            E = heapq.heappop(ends)
            heapq.heappush(temp, E)
        if not temp:
            rooms += 1
            heapq.heappush(ends, e)
            continue
        heapq.heappop(temp)
        heapq.heappush(ends, e)
    print(rooms)


if __name__ == "__main__":
    input = sys.stdin.readline
    main()
