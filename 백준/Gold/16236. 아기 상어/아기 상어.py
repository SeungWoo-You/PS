import sys
import heapq


class Shark:
    def __init__(self) -> None:
        self.N: int
        self.board: list[list[int]]
        self.size = 2
        self.pos: list[int]
        self.get_info()

    def get_info(self) -> None:
        self.N = int(input())
        self.board = [list(map(int, input().split())) for _ in range(self.N)]
        for i, row in enumerate(self.board):
            for j, x in enumerate(row):
                if x == 9:
                    self.pos = [i, j]

    def find(self) -> int:
        total = 0
        eat = 0
        Dx = [-1, 0, 0, 1]
        Dy = [0, -1, 1, 0]
        while True:
            t = 0
            i, j = self.pos
            H: list[tuple[int, int, int]] = [(0, i, j)]
            self.board[i][j] = 0
            checked: set[tuple[int, int]] = set()
            while H:
                d, i, j = heapq.heappop(H)
                if (i, j) in checked:
                    continue
                if 0 < self.board[i][j] < self.size:
                    self.board[i][j] = 9
                    eat += 1
                    self.pos = [i, j]
                    if eat == self.size:
                        eat = 0
                        self.size += 1
                    t = d
                    break
                checked.add((i, j))
                for dx, dy in zip(Dx, Dy):
                    x, y = i + dx, j + dy
                    if 0 <= x < self.N and 0 <= y < self.N and self.board[x][y] <= self.size:
                        heapq.heappush(H, (d + 1, x, y))
            total += t
            if t == 0:
                break
        return total


def main():
    shark = Shark()
    print(shark.find())


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
