import sys
from collections import Counter


class Piece:
    def __init__(self) -> None:
        self.pos: list[tuple[int, int]] = []
        self.get_info()

    def get_info(self) -> None:
        info = list(map(int, input().split()))
        for i in range(1, info[0] * 2, 2):
            self.pos.append(tuple([info[i], info[i + 1]]))

    def mark(self, board: list[list[int | str]]) -> None:
        pass

    def move(self, board: list[list[int | str]]) -> None:
        pass


class Queen(Piece):
    def __init__(self) -> None:
        super().__init__()

    def mark(self, board: list[list[int | str]]) -> None:
        for x, y in self.pos:
            board[x][y] = 'Q'

    def move(self, board: list[list[int | str]], N: int, M: int) -> None:
        Dx = [0, 0, -1, 1, -1, -1, 1, 1]
        Dy = [1, -1, 0, 0, -1, 1, -1, 1]
        for i, j in self.pos:
            for dx, dy in zip(Dx, Dy):
                x, y = i + dx, j + dy
                while 0 < x <= N and 0 < y <= M:
                    if isinstance(board[x][y], int) or board[x][y] == 'Q':
                        board[x][y] = 'Q'
                        x, y = x + dx, y + dy
                    else:
                        break


class Knight(Piece):
    def __init__(self) -> None:
        super().__init__()

    def mark(self, board: list[list[int | str]]) -> None:
        for x, y in self.pos:
            board[x][y] = 'K'

    def move(self, board: list[list[int | str]], N: int, M: int) -> None:
        Dx = [2, 2, -1, 1, -2, -2, -1, 1]
        Dy = [1, -1, 2, 2, -1, 1, -2, -2]
        for i, j in self.pos:
            for dx, dy in zip(Dx, Dy):
                x, y = i + dx, j + dy
                if 0 < x <= N and 0 < y <= M and isinstance(board[x][y], int):
                    board[x][y] = 'K'


class Pawn(Piece):
    def __init__(self) -> None:
        super().__init__()

    def mark(self, board: list[list[int | str]]) -> None:
        for x, y in self.pos:
            board[x][y] = 'P'


class Chess:
    def __init__(self) -> None:
        self.get_info()
        self.n: int
        self.m: int
        self.queen = Queen()
        self.knight = Knight()
        self.pawn = Pawn()

    def get_info(self) -> None:
        self.n, self.m = map(int, input().split())

    def safe(self) -> int:
        board = [[0] * (self.m + 1) for _ in range(self.n + 1)]
        for i in range(self.n + 1):
            board[i][0] = 'X'
        for j in range(self.m + 1):
            board[0][j] = 'X'
        self.queen.mark(board)
        self.knight.mark(board)
        self.pawn.mark(board)
        self.queen.move(board, self.n, self.m)
        self.knight.move(board, self.n, self.m)

        count = Counter()
        for row in board:
            count.update(row)
        return count[0]


def main():
    chess = Chess()
    print(chess.safe())


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
