from collections import defaultdict


def main():
    N = int(input())
    E = int(input())
    network: defaultdict[int, list[int]] = defaultdict(list)
    for _ in range(E):
        u, v = map(int, input().split())
        network[u].append(v)
        network[v].append(u)
    print(spread_virus(network, N))


def spread_virus(graph: defaultdict[int, list[int]], N: int) -> int:
    count = 0
    stack = [1]
    visited = {v: False for v in range(1, N + 1)}
    while stack:
        u = stack.pop()
        if visited[u] == True:
            continue
        visited[u] = True
        count += 1
        stack.extend(graph[u])
    return count - 1


if __name__ == '__main__':
    main()
