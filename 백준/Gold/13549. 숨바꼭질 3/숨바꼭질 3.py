import sys
from collections import deque


def main():
    N, K = map(int, input().split())
    print(hide_and_seek(N, K))


def hide_and_seek(N: int, K: int) -> int:
    queue = deque([N])
    size = 10**6 + 1
    visited = [-1] * size
    visited[N] = 0
    while queue:
        x = queue.popleft()
        if x == K:
            return visited[K]
        dx = 2 * x
        if 0 <= dx < size and visited[dx] == -1:
            visited[dx] = visited[x]
            queue.append(dx)
        for dx in [x - 1, x + 1]:
            if 0 <= dx < size and visited[dx] == -1:
                visited[dx] = 0
                visited[dx] = visited[x] + 1
                queue.append(dx)
    return visited[K]


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
