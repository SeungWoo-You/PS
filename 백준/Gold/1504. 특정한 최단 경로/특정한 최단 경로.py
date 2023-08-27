from collections import defaultdict, deque


def main():
    N, E = map(int, input().split())
    graph = defaultdict(dict)
    for _ in range(E):
        u, v, w = map(int, input().split())
        graph[u][v] = w
        graph[v][u] = w
    v1, v2 = map(int, input().split())
    from_src = find_shortest_path(graph, N, 1)
    from_v1 = find_shortest_path(graph, N, v1)
    from_v2 = find_shortest_path(graph, N, v2)
    res1 = from_src[v1] + from_v1[v2] + from_v2[N]
    res2 = from_src[v2] + from_v2[v1] + from_v1[N]
    res = min(res1, res2)
    print(res if res != float('inf') else -1)


def find_shortest_path(graph: defaultdict[int, dict[int]], N: int, src: int) -> list[int]:
    costs = [float('inf')] * (N + 1)
    costs[src] = 0
    queue = deque([src])
    while queue:
        u = queue.popleft()
        for v, w in graph[u].items():
            if costs[v] > costs[u] + w:
                costs[v] = costs[u] + w
                queue.append(v)
    return costs


if __name__ == '__main__':
    main()
