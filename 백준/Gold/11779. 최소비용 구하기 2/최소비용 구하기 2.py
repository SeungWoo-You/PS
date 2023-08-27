import sys
from collections import defaultdict, deque


def main():
    n = int(input())
    m = int(input())
    bus: defaultdict[int, dict[int, int]] = defaultdict(dict)
    check: set[tuple[int, int]] = set()
    for _ in range(m):
        u, v, w = map(int, input().split())
        bus[u][v] = w if not (u, v) in check else min(bus[u][v], w)
        check.add((u, v))
    src, dst = map(int, input().split())
    cost, ways = find_cost(bus, n, src, dst)
    print(cost)
    print(len(ways))
    print(*ways)


def find_cost(graph: defaultdict[int, dict[int, int]], N: int, src: int, dst: int) -> tuple[int, list[int]]:
    queue = deque([(0, src)])
    costs = [sys.maxsize] * (N + 1)
    costs[src] = 0
    ways = [[src]] * (N + 1)
    while queue:
        c, u = queue.popleft()
        for v, w in graph[u].items():
            if u == v:
                continue
            if c + w < costs[v]:
                costs[v] = c + w
                ways[v] = ways[u] + [v]
                queue.append((costs[v], v))
    return costs[dst], ways[dst]


if __name__ == "__main__":
    input = sys.stdin.readline
    main()
