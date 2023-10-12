import sys
from collections import deque


class Marble:
    def __init__(self) -> None:
        self.N: int
        self.M: int
        self.board: list[list[str]]
        self.R: tuple[int, int]
        self.B: tuple[int, int]
        self.get_info()

    def get_info(self) -> None:
        self.N, self.M = map(int, input().split())
        self.board = [list(input().strip()) for _ in range(self.N)]
        for i, row in enumerate(self.board):
            for j, x in enumerate(row):
                if x == 'R':
                    self.R = (i, j)
                elif x == 'B':
                    self.B = (i, j)

    def play(self) -> int:
        Q: deque[tuple[int, ...]] = deque([(*self.R, *self.B, 0)])
        visited: set[tuple[int, ...]] = set()
        Dx = [0, 0, -1, 1]
        Dy = [-1, 1, 0, 0]
        while Q:
            ri, rj, bi, bj, t = Q.popleft()
            if self.board[ri][rj] == 'O':
                return t
            if (ri, rj, bi, bj) in visited:
                continue
            visited.add((ri, rj, bi, bj))
            if t >= 10:
                continue
            for dx, dy in zip(Dx, Dy):
                rx, ry = ri + dx, rj + dy
                rmove = 0
                while True:
                    if self.board[rx][ry] == '#':
                        rx, ry = rx - dx, ry - dy
                        break
                    if self.board[rx][ry] == 'O':
                        break
                    rx, ry = rx + dx, ry + dy
                    rmove += 1
                bx, by = bi + dx, bj + dy
                bmove = 0
                while True:
                    if self.board[bx][by] == '#':
                        bx, by = bx - dx, by - dy
                        break
                    if self.board[bx][by] == 'O':
                        break
                    bx, by = bx + dx, by + dy
                    bmove += 1
                if self.board[bx][by] == 'O':
                    continue
                if (rx, ry) == (bx, by):
                    if rmove > bmove:
                        rx, ry = rx - dx, ry - dy
                    else:
                        bx, by = bx - dx, by - dy
                Q.append((rx, ry, bx, by, t + 1))
        return -1


def main():
    marble = Marble()
    print(marble.play())


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
