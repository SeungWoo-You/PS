import sys
from collections import deque


def main():
    global N, M, K
    N, M, K = map(int, input().split())
    mat = [list(map(int, list(input().strip()))) for _ in range(N)]
    res = move(mat)
    print(res)


def move(mat: list[list[int]]) -> int:
    visited = [[[0] * (K + 1) for _ in range(M)] for _ in range(N)]
    visited[0][0][0] = 1
    Q = deque([(0, 0, 0)])

    Dx = [0, 0, -1, 1]
    Dy = [-1, 1, 0, 0]

    while Q:
        i, j, k = Q.popleft()
        if i == N - 1 and j == M - 1:
            return visited[i][j][k]
        for dx, dy in zip(Dx, Dy):
            x = i + dx
            y = j + dy
            if 0 <= x < N and 0 <= y < M:
                if mat[x][y] == 1 and k < K and not visited[x][y][k + 1]:
                    visited[x][y][k + 1] = visited[i][j][k] + 1
                    Q.append((x, y, k + 1))
                elif mat[x][y] == 0 and not visited[x][y][k]:
                    visited[x][y][k] = visited[i][j][k] + 1
                    Q.append((x, y, k))
    return -1


if __name__ == "__main__":
    input = sys.stdin.readline
    main()
