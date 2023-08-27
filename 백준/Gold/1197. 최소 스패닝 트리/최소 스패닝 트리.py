from collections import defaultdict
import heapq


def main():
    V, E = map(int, input().split())
    graph: defaultdict[int, dict[int, int]] = defaultdict(dict)
    for _ in range(E):
        u, v, w = map(int, input().split())
        graph[u][v] = graph[v][u] = w
    print(find_MST(graph, V))


def find_MST(graph: defaultdict[int, dict[int, int]], N: int) -> int:
    visited = [False] * (N + 1)
    heap = [(0, 1)]
    res = 0
    while heap:
        weight, node = heapq.heappop(heap)
        if visited[node] == True:
            continue
        res += weight
        visited[node] = True
        for v in graph[node]:
            heapq.heappush(heap, (graph[node][v], v))
    return res


if __name__ == '__main__':
    main()
