import sys
from collections import deque


class Maze:
    def __init__(self) -> None:
        self.N: int
        self.M: int
        self.mat: list[list[int]]
        self.get_info()

    def get_info(self) -> None:
        self.N, self.M = map(int, input().split())
        self.mat = [list(map(int, list(input().strip())))
                    for _ in range(self.N)]

    def move(self) -> int:
        visited = [[[0] * 2 for _ in range(self.M)] for _ in range(self.N)]
        visited[0][0][0] = 1
        Q = deque([(0, 0, 0)])
        Dx = [0, 0, -1, 1]
        Dy = [-1, 1, 0, 0]
        while Q:
            i, j, k = Q.popleft()
            if i == self.N - 1 and j == self.M - 1:
                return visited[i][j][k]
            for dx, dy in zip(Dx, Dy):
                x = i + dx
                y = j + dy
                if 0 <= x < self.N and 0 <= y < self.M:
                    if self.mat[x][y] == 1 and k == 0 and not visited[x][y][k + 1]:
                        visited[x][y][k + 1] = visited[i][j][k] + 1
                        Q.append((x, y, k + 1))
                    elif self.mat[x][y] == 0 and not visited[x][y][k]:
                        visited[x][y][k] = visited[i][j][k] + 1
                        Q.append((x, y, k))
        return -1


def main():
    maze = Maze()
    print(maze.move())


if __name__ == "__main__":
    input = sys.stdin.readline
    main()
