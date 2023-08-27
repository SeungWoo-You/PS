from collections import defaultdict
import heapq


def main():
    N = int(input())
    M = int(input())
    bus_line: defaultdict[int, dict[int, int]] = defaultdict(dict)
    checked = set()
    for _ in range(M):
        u, v, w = map(int, input().split())
        if (u, v) in checked:
            bus_line[u][v] = min(w, bus_line[u][v])
            continue
        bus_line[u][v] = w
        checked.add((u, v))
    src, dst = map(int, input().split())
    print(find_cost(bus_line, N, src)[dst])


def find_cost(graph: defaultdict[int, dict[int, int]], N: int, src: int) -> list[int]:
    res = [float('inf')] * (N + 1)
    heap = [(0, src)]
    res[src] = 0
    while heap:
        weight, u = heapq.heappop(heap)
        for v, w in graph[u].items():
            if w + weight < res[v]:
                res[v] = weight + w
                heapq.heappush(heap, (res[v], v))
    return res


if __name__ == '__main__':
    main()
