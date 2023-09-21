import sys
from itertools import product
from copy import deepcopy


class Game2048:
    def __init__(self) -> None:
        self.N: int
        self.board: list[list[int]]
        self.get_info()

    def get_info(self) -> None:
        self.N = int(input())
        self.board = [list(map(int, input().split())) for _ in range(self.N)]

    def move(self, line: list[int]) -> list[int]:
        result: list[int] = [0] * self.N
        i = 0
        for y in line:
            x = result[i]
            if y == 0:
                continue
            elif x != 0 and x == y:
                result[i] = 2 * x
                i += 1
            elif x != 0 and x != y:
                i += 1
                result[i] = y
            elif x == 0 and y != 0:
                result[i] = y
        return result

    def play(self) -> int:
        M = 0
        for T in product('LRTB', repeat=5):
            board = deepcopy(self.board)
            for way in T:
                if way == 'L':
                    for i, row in enumerate(board):
                        board[i] = self.move(row)
                if way == 'R':
                    for i, row in enumerate(board):
                        line = list(reversed(row))
                        board[i] = list(reversed(self.move(line)))
                if way == 'T':
                    for j in range(self.N):
                        col = [board[i][j] for i in range(self.N)]
                        res = self.move(col)
                        for i, val in enumerate(res):
                            board[i][j] = val
                if way == 'B':
                    for j in range(self.N):
                        col = [board[i][j] for i in range(self.N - 1, -1, -1)]
                        res = reversed(self.move(col))
                        for i, val in enumerate(res):
                            board[i][j] = val
            M = max(M, max(map(max, board)))
        return M


def main():
    game = Game2048()
    print(game.play())


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
