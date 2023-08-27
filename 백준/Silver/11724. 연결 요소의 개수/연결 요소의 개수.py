import sys
from collections import defaultdict


def main():
    N, M = map(int, input().split())
    graph: defaultdict[int, list[int]] = defaultdict(list)
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    print(count_components(graph) + N - len(graph))


def count_components(graph: defaultdict[int, list[int]]) -> int:
    if not graph:
        return 0
    visited = {v: False for v in graph}
    start = next((v for v in graph.keys()))
    stack = [start]

    count = 1
    while False in set(visited.values()):
        if not stack:
            for key, val in visited.items():
                if val == False:
                    count += 1
                    stack.append(key)
                    break
        u = stack.pop()
        if visited[u] == True:
            continue
        visited[u] = True
        stack.extend(graph[u])
    return count


if __name__ == "__main__":
    input = sys.stdin.readline
    main()
