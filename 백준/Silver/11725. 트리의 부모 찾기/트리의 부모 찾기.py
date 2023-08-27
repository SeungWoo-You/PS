import sys
from collections import defaultdict, deque


def main():
    N = int(input())
    graph: defaultdict[int, set[int]] = defaultdict(set)
    for _ in range(N - 1):
        u, v = map(int, input().split())
        graph[u].add(v)
        graph[v].add(u)
    pair = find_parent(graph, N)
    for v in sorted(pair.keys()):
        if v == 1:
            continue
        print(pair[v])


def find_parent(graph: defaultdict[int, list[int]], N: int) -> dict[int, int]:
    Q = deque([1])
    pair: dict[int, int] = {1: -1}
    checked: set[int] = set()
    while Q:
        u = Q.popleft()
        if u in checked:
            continue
        checked.add(u)
        for v in graph[u]:
            Q.append(v)
            if v not in pair:
                pair[v] = u
    return pair


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
