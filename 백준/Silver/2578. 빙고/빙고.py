import sys


class Bingo:
    def __init__(self) -> None:
        self.N: int = 5
        self.board: list[list[int]]
        self.count: int = 0
        self.get_info()

    def get_info(self) -> None:
        self.board = [list(map(int, input().split())) for _ in range(self.N)]

    def check(self, c: int) -> None:
        for i, row in enumerate(self.board):
            for j, x in enumerate(row):
                if x == c:
                    break
            else:
                continue
            break
        self.board[i][j] = 0
        possible = [True] * 2
        if i == j:
            possible.append(True)
        if i == self.N - 1 - j:
            possible.append(True)
        for k in range(self.N):
            if i == j:
                if possible[2] == True and self.board[k][k] != 0:
                    possible[2] = False
            if i == self.N - 1 - j:
                if possible[-1] == True and self.board[k][self.N - 1 - k] != 0:
                    possible[-1] = False
            if possible[1] == True and self.board[i][k] != 0:
                possible[1] = False
            if possible[0] == True and self.board[k][j] != 0:
                possible[0] = False
        self.count += possible.count(True)


def main():
    game = Bingo()
    calls: list[int] = []
    for _ in range(5):
        line = map(int, input().split())
        calls.extend(line)
    for i, t in enumerate(calls, start=1):
        game.check(t)
        if game.count >= 3:
            break
    print(i)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
