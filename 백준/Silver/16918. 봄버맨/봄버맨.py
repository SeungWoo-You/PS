import sys


class Bomber:
    def __init__(self) -> None:
        self.R: int
        self.C: int
        self.N: int
        self.board: list[list[str]]
        self.get_info()

    def get_info(self) -> None:
        self.R, self.C, self.N = map(int, input().split())
        self.board = [list(input().strip()) for _ in range(self.R)]

    def play(self) -> None:
        bombs, empty = self.find()
        for t in range(2, self.N + 1):
            if t % 2 == 0:
                self.plant(empty)
            elif t % 2 == 1:
                boom, temp = self.explode(bombs)
                bombs, empty = empty - boom, temp

    def find(self) -> tuple[set[tuple[int, int]], set[tuple[int, int]]]:
        bombs: set[tuple[int, int]] = set()
        empty: set[tuple[int, int]] = set()
        for i, row in enumerate(self.board):
            for j, tile in enumerate(row):
                if tile == 'O':
                    bombs.add((i, j))
                elif tile == '.':
                    empty.add((i, j))
        return (bombs, empty)

    def plant(self, empty: set[tuple[int, int]]) -> None:
        for i, j in empty:
            self.board[i][j] = 'O'

    def explode(self, bombs: set[tuple[int, int]]) -> tuple[set[tuple[int, int]], set[tuple[int, int]]]:
        Dx = [0, 0, -1, 1]
        Dy = [-1, 1, 0, 0]
        empty: set[tuple[int, int]] = set()
        boom: set[tuple[int, int]] = set()
        for i, j in bombs:
            self.board[i][j] = '.'
            empty.add((i, j))
            for dx, dy in zip(Dx, Dy):
                x, y = i + dx, j + dy
                if 0 <= x < self.R and 0 <= y < self.C:
                    if self.board[x][y] == 'O':
                        boom.add((x, y))
                    self.board[x][y] = '.'
                    empty.add((x, y))
        return (boom, empty)


def main():
    bomber_man = Bomber()
    bomber_man.play()
    for row in bomber_man.board:
        print(''.join(row))


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
