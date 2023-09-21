import sys
from collections import deque


class Tetromino:
    def __init__(self) -> None:
        self.N: int
        self.M: int
        self.board: list[list[int]]
        self.get_info()

    def get_info(self) -> None:
        self.N, self.M = map(int, input().split())
        self.board = [list(map(int, input().split())) for _ in range(self.N)]

    def place(self) -> int:
        Dx = [0, 0, -1, 1]
        Dy = [-1, 1, 0, 0]
        total = 0
        for u in range(self.N):
            for v in range(self.M):
                src = (u, v, 1, self.board[u][v], (-1, -1))
                Q = deque([src])
                while Q:
                    i, j, p, t, prev = Q.popleft()
                    if p >= 4:
                        total = max(total, t)
                        continue
                    for dx, dy in zip(Dx, Dy):
                        x, y = i + dx, j + dy
                        if 0 <= x < self.N and 0 <= y < self.M and (x, y) != prev:
                            if p == 2:
                                for d1, d2 in zip(Dx, Dy):
                                    k1, k2 = i + d1, j + d2
                                    if (k1, k2) != (x, y) and (k1, k2) != prev:
                                        if 0 <= k1 < self.N and 0 <= k2 < self.M:
                                            total = max(
                                                total, t + self.board[x][y] + self.board[k1][k2])
                            Q.append(
                                (x, y, p + 1, t + self.board[x][y], (i, j)))
        return total


def main():
    game = Tetromino()
    print(game.place())


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
