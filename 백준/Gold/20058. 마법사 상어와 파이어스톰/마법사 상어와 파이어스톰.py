import sys
from collections import deque


class FireStorm:
    def __init__(self) -> None:
        self.N: int
        self.Q: int
        self.S: int
        self.board: list[list[int]]
        self.magic: list[int]
        self.get_info()

    def get_info(self) -> None:
        self.N, self.Q = map(int, input().split())
        self.S = 2**self.N
        self.board = [list(map(int, input().split())) for _ in range(self.S)]
        self.magic = list(map(int, input().split()))

    def rotate(self, L: int) -> None:
        for m in range(2**L // 2 + 1):
            side = 2 ** L - 2 * m
            for si in range(0 + m, self.S, 2**L):
                for sj in range(0 + m, self.S, 2**L):
                    ei, ej = si + side - 1, sj + side - 1
                    Q: deque[int] = deque([self.board[si][y]
                                          for y in range(sj + 1, ej + 1)])
                    Q.extend([self.board[x][ej]
                             for x in range(si + 1, ei + 1)])
                    Q.extend([self.board[ei][y]
                             for y in range(ej - 1, sj - 1, -1)])
                    Q.extend([self.board[x][sj]
                             for x in range(ei - 1, si - 1, -1)])
                    for _ in range(side - 1):
                        Q.appendleft(Q.pop())
                    for y in range(sj + 1, ej + 1):
                        self.board[si][y] = Q.popleft()
                    for x in range(si + 1, ei + 1):
                        self.board[x][ej] = Q.popleft()
                    for y in range(ej - 1, sj - 1, -1):
                        self.board[ei][y] = Q.popleft()
                    for x in range(ei - 1, si - 1, -1):
                        self.board[x][sj] = Q.popleft()

    def melt(self) -> None:
        Dx = [0, 0, -1, 1]
        Dy = [-1, 1, 0, 0]
        minus_cell = [[0] * self.S for _ in range(self.S)]
        for i in range(self.S):
            for j in range(self.S):
                if self.board[i][j] == 0:
                    continue
                near = 0
                for dx, dy in zip(Dx, Dy):
                    x, y = i + dx, j + dy
                    if 0 <= x < self.S and 0 <= y < self.S and self.board[x][y] != 0:
                        near += 1
                if near < 3:
                    minus_cell[i][j] = -1
        for i in range(self.S):
            for j in range(self.S):
                self.board[i][j] += minus_cell[i][j]

    def count_ice(self) -> tuple[int, int]:
        possible: set[tuple[int, int]] = set()
        total = 0
        for i, row in enumerate(self.board):
            for j, x in enumerate(row):
                if x != 0:
                    possible.add((i, j))
                total += x

        Dx = [0, 0, -1, 1]
        Dy = [-1, 1, 0, 0]
        gp = 0
        while possible:
            i, j = possible.pop()
            Q: deque[tuple[int, int]] = deque([(i, j)])
            checked: set[tuple[int, int]] = set()
            while Q:
                i, j = Q.popleft()
                if (i, j) in checked:
                    continue
                checked.add((i, j))
                for dx, dy in zip(Dx, Dy):
                    x, y = i + dx, j + dy
                    if 0 <= x < self.S and 0 <= y < self.S and self.board[x][y] != 0:
                        Q.append((x, y))
            gp = max(gp, len(checked))
            possible.difference_update(checked)
        return total, gp

    def play(self) -> tuple[int, int]:
        for L in self.magic:
            self.rotate(L)
            self.melt()
        return self.count_ice()


def main():
    FS = FireStorm()
    result = FS.play()
    print(*result)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
