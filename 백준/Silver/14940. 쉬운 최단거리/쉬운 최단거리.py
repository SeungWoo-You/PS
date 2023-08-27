import sys
from collections import deque


def main():
    global n, m, visited
    n, m = map(int, input().split())
    mat = []
    visited = [[-1] * m for _ in range(n)]
    src = (-1, -1)
    for i in range(n):
        line = list(map(int, input().split()))
        for j in range(m):
            if src == (-1, -1) and line[j] == 2:
                src = (i, j)
                visited[i][j] = 0
            elif line[j] == 0:
                visited[i][j] = 0
        mat.append(line)
    res = find_dist(mat, src)
    for i in range(n):
        print(*res[i])


def find_dist(mat: list[list[int]], src: tuple[int, int]) -> list[list[int]]:
    Q = deque([src])
    Dx = [-1, 1, 0, 0]
    Dy = [0, 0, -1, 1]

    while Q:
        i, j = Q.popleft()
        for dx, dy in zip(Dx, Dy):
            x = i + dx
            y = j + dy
            if 0 <= x < n and 0 <= y < m and visited[x][y] == -1:
                if mat[x][y] == 1:
                    visited[x][y] = visited[i][j] + 1
                    Q.append((x, y))
    return visited


if __name__ == "__main__":
    input = sys.stdin.readline
    main()
