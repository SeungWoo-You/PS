from collections import deque


def main():
    N, M = map(int, input().split())
    compares: dict[int, set[int]] = {v: set() for v in range(1, N + 1)}
    deg = {v: 0 for v in range(1, N + 1)}
    for _ in range(M):
        A, B = map(int, input().split())
        compares[A].add(B)
        deg[B] += 1
    print(*line_up(compares, deg))


def line_up(order: dict[int, set[int]], deg: dict[int, int]) -> list:
    queue: deque[int] = deque([])
    for v in order:
        if deg[v] == 0:
            queue.append(v)
    ordered = []

    while queue:
        u = queue.popleft()
        ordered.append(u)
        for v in order[u]:
            deg[v] -= 1
            if deg[v] == 0:
                queue.append(v)
    return ordered


if __name__ == '__main__':
    main()
