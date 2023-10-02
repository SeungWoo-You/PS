import sys
import heapq


class Cave:
    def __init__(self) -> None:
        self.N: int
        self.maze: list[list[int]]
        self.get_info()

    def get_info(self) -> None:
        self.N = int(input())
        self.maze = [list(map(int, input().split())) for _ in range(self.N)]

    def escape(self) -> int:
        Dx = [0, 0, -1, 1]
        Dy = [-1, 1, 0, 0]
        visited = [[sys.maxsize] * self.N for _ in range(self.N)]
        visited[0][0] = self.maze[0][0]
        H: list[tuple[int, int, int]] = [(visited[0][0], 0, 0)]
        while H:
            d, i, j = heapq.heappop(H)
            for dx, dy in zip(Dx, Dy):
                x, y = i + dx, j + dy
                if 0 <= x < self.N and 0 <= y < self.N:
                    if visited[x][y] > visited[i][j] + self.maze[x][y]:
                        visited[x][y] = visited[i][j] + self.maze[x][y]
                        heapq.heappush(H, (visited[x][y], x, y))
        return visited[-1][-1]


def main():
    cave = Cave()
    i = 1
    while cave.N != 0:
        print(f'Problem {i}: {cave.escape()}')
        cave = Cave()
        i += 1


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
