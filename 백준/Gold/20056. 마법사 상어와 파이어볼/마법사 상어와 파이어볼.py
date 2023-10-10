import sys
from dataclasses import dataclass


@dataclass
class Fireball:
    m: int
    s: int
    d: int


class Table:
    def __init__(self) -> None:
        self.N: int
        self.M: int
        self.K: int
        self.board: list[list[list[Fireball]]]
        self.get_info()

    def get_info(self) -> None:
        self.N, self.M, self.K = map(int, input().split())
        self.board = [[[] for _ in range(self.N)] for _ in range(self.N)]
        for _ in range(self.M):
            r, c, m, s, d = map(int, input().split())
            self.board[r - 1][c - 1].append(Fireball(m, s, d))

    def move(self) -> None:
        board = [[[] for _ in range(self.N)] for _ in range(self.N)]
        D: dict[int, tuple[int, int]] = {
            0: (-1, 0),
            1: (-1, 1),
            2: (0, 1),
            3: (1, 1),
            4: (1, 0),
            5: (1, -1),
            6: (0, -1),
            7: (-1, -1)
        }
        for i in range(self.N):
            for j in range(self.N):
                for F in self.board[i][j]:
                    dx, dy = D[F.d]
                    x, y = (i + F.s * dx) % self.N, (j + F.s * dy) % self.N
                    board[x][y].append(F)
        self.board = board

    def merge_and_split(self) -> None:
        for i in range(self.N):
            for j in range(self.N):
                if len(self.board[i][j]) >= 2:
                    mass, speed = 0, 0
                    direction: set[bool] = set()
                    for F in self.board[i][j]:
                        mass += F.m
                        speed += F.s
                        direction.add(True if F.d % 2 == 0 else False)
                    mass //= 5
                    speed //= len(self.board[i][j])
                    self.board[i][j].clear()
                    if mass > 0:
                        start = 0 if len(direction) == 1 else 1
                        for d in range(start, 8, 2):
                            self.board[i][j].append(
                                Fireball(mass, speed, d))


def main():
    table = Table()
    for _ in range(table.K):
        table.move()
        table.merge_and_split()
    total = 0
    for row in table.board:
        for S in row:
            for F in S:
                total += F.m
    print(total)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
