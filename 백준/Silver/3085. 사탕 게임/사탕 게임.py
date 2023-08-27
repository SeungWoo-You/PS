import sys


class Game:
    def __init__(self) -> None:
        self.N: int
        self.board: list[list[str]]
        self.get_info()

    def get_info(self) -> None:
        self.N = int(input())
        self.board = [list(input().strip()) for _ in range(self.N)]

    def play(self) -> int:
        count = 0
        Dx = [0, 0, -1, 1]
        Dy = [-1, 1, 0, 0]
        for i in range(self.N):
            for j in range(self.N):
                for dx, dy in zip(Dx, Dy):
                    x, y = i + dx, j + dy
                    if 0 <= x < self.N and 0 <= y < self.N:
                        self.board[i][j], self.board[x][y] = self.board[x][y], self.board[i][j]
                        count = max(count, self.eating(
                            'row', (x, y)), self.eating('col', (x, y)))
                        self.board[i][j], self.board[x][y] = self.board[x][y], self.board[i][j]
        return count

    def eating(self, dim: str, idx: tuple[int, int]) -> int:
        count = 1
        if dim == 'row':
            dx, dy = 0, 1
            x, y = idx[0], 0
        elif dim == 'col':
            dx, dy = 1, 0
            x, y = 0, idx[1]
        candy = self.board[x][y]

        temp = 1
        for _ in range(self.N - 1):
            x, y = x + dx, y + dy
            temp = temp + 1 if candy == self.board[x][y] else 1
            count = max(count, temp)
            candy = self.board[x][y]
        return count


def main():
    game = Game()
    print(game.play())


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
