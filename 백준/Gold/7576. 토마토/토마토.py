import sys
from collections import deque


def main():
    global M, N, visited
    M, N = map(int, input().split())
    tomato: deque[tuple[int, int]] = deque([])
    visited = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if visited[i][j] == 1:
                tomato.append((i, j))

    ripe_tomato(tomato)
    res = 0
    for ls in visited:
        for x in ls:
            if x == 0:
                print(-1)
                exit(0)
        res = max(res, max(ls))
    print(res - 1)


def ripe_tomato(tomato: deque[tuple[int, int, int]]) -> None:
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    while tomato:
        i, j = tomato.popleft()
        for k in range(4):
            x, y = dx[k] + i, dy[k] + j
            if 0 <= x < N and 0 <= y < M and visited[x][y] == 0:
                visited[x][y] = visited[i][j] + 1
                tomato.append((x, y))
    return


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
