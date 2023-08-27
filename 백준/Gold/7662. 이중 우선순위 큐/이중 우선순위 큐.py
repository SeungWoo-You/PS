import sys
import heapq


def main():
    T = int(input())
    for _ in range(T):
        Q = int(input())
        max_heap: list[int] = []
        min_heap: list[int] = []
        visited = [0] * Q
        for i in range(Q):
            mode, x = input().strip().split()
            if mode == 'I':
                x = int(x)
                heapq.heappush(max_heap, (-x, i))
                heapq.heappush(min_heap, (x, i))
                visited[i] = 1
            if mode == 'D':
                x = int(x)
                if x == -1:
                    while min_heap and visited[min_heap[0][1]] == 0:
                        heapq.heappop(min_heap)
                    if min_heap:
                        visited[min_heap[0][1]] = 0
                        heapq.heappop(min_heap)
                else:
                    while max_heap and visited[max_heap[0][1]] == 0:
                        heapq.heappop(max_heap)
                    if max_heap:
                        visited[max_heap[0][1]] = 0
                        heapq.heappop(max_heap)

        while max_heap and visited[max_heap[0][1]] == 0:
            heapq.heappop(max_heap)
        while min_heap and visited[min_heap[0][1]] == 0:
            heapq.heappop(min_heap)
        if 1 not in set(visited):
            print("EMPTY")
        else:
            print(-max_heap[0][0], min_heap[0][0])


if __name__ == "__main__":
    input = sys.stdin.readline
    main()
