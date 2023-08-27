import sys
from collections import deque


def main():
    N, M = map(int, input().split())
    maze = [list(map(int, list(input().strip()))) for _ in range(N)]
    print(find_root(maze, N, M))


def find_root(maze: list[list[int]], N: int, M: int) -> int:
    count = [[sys.maxsize] * (M + 1) for _ in range(N + 1)]
    Q = deque([(1, 1, 1)])
    Dx = [1, -1, 0, 0]
    Dy = [0, 0, 1, -1]

    while Q:
        i, j, w = Q.popleft()
        for dx, dy in zip(Dx, Dy):
            x, y = i + dx, j + dy
            if 0 < x <= N and 0 < y <= M and maze[x - 1][y - 1] == 1:
                if count[x][y] > w + 1:
                    count[x][y] = w + 1
                    Q.append((x, y, w + 1))
    return count[N][M]


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
