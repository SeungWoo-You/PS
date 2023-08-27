import sys
import heapq


class Maze:
    def __init__(self) -> None:
        self.M: int
        self.N: int
        self.rooms: list[list[int]]
        self.get_info()

    def get_info(self) -> None:
        self.M, self.N = map(int, input().split())
        self.rooms = [list(map(int, list(input().strip())))
                      for _ in range(self.N)]

    def escape(self) -> int:
        Dx = [0, 0, -1, 1]
        Dy = [-1, 1, 0, 0]
        costs = [[sys.maxsize] * self.M for _ in range(self.N)]
        costs[0][0] = 0
        H = [(0, 0, 0)]
        while H:
            c, i, j = heapq.heappop(H)
            for dx, dy in zip(Dx, Dy):
                x, y = i + dx, j + dy
                if 0 <= x < self.N and 0 <= y < self.M:
                    k = c + self.rooms[x][y]
                    if k < costs[x][y]:
                        costs[x][y] = k
                        heapq.heappush(H, (k, x, y))
        return costs[self.N - 1][self.M - 1]


def main():
    maze = Maze()
    print(maze.escape())


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
