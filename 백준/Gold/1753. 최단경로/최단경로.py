from collections import defaultdict
import heapq
import sys


def main():
    input = sys.stdin.readline
    V, E = map(int, input().split())
    K = int(input())
    graph = defaultdict(dict)
    checked = set()
    for _ in range(E):
        u, v, w = map(int, input().split())
        if (u, v) in checked:
            graph[u][v] = min(graph[u][v], w)
        else:
            graph[u][v] = w
        checked.add((u, v))
    for i, x in enumerate(find_path(graph, V, K)):
        if i == 0:
            continue
        print(x if x != float('inf') else 'INF')


def find_path(graph: defaultdict[int, dict[int, int]], N: int, src: int) -> list[int]:
    costs = [float('inf')] * (N + 1)
    costs[src] = 0
    heap = [(0, src)]
    while heap:
        c, u = heapq.heappop(heap)
        if costs[u] < c:
            continue
        for v, w in graph[u].items():
            if costs[v] > costs[u] + w:
                costs[v] = costs[u] + w
                heapq.heappush(heap, (costs[v], v))
    return costs


if __name__ == '__main__':
    main()
