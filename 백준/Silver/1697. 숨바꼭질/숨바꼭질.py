import sys
from collections import deque


def main():
    N, K = map(int, input().split())
    print(hide_and_seek(N, K))


def hide_and_seek(N: int, K: int) -> int:
    queue = deque([N])
    size = 10**6 + 1
    dist = [0] * size
    while queue:
        x = queue.popleft()
        if x == K:
            return dist[K]
        for dx in [x - 1, x + 1, 2 * x]:
            if 0 <= dx < size and dist[dx] == 0:
                dist[dx] = dist[x] + 1
                queue.append(dx)
    return dist[K]


if __name__ == "__main__":
    sys.setrecursionlimit(10**5)
    input = sys.stdin.readline
    main()
