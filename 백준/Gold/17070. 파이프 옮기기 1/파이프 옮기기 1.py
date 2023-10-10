import sys


class Home:
    def __init__(self) -> None:
        self.N: int
        self.board: list[list[int]]
        self.get_info()

    def get_info(self) -> None:
        self.N = int(input())
        self.board = [list(map(int, input().split())) for _ in range(self.N)]

    def move_pipes(self) -> int:
        possible = [[[0] * self.N for _ in range(self.N)] for _ in range(3)]
        possible[0][0][1] = 1
        for i in range(2, self.N):
            if self.board[0][i] == 0:
                possible[0][0][i] = possible[0][0][i - 1]
        for x in range(1, self.N):
            for y in range(1, self.N):
                if self.board[x][y] == 0 and self.board[x][y - 1] == 0 and self.board[x - 1][y] == 0:
                    possible[2][x][y] = possible[0][x - 1][y - 1] + \
                        possible[1][x - 1][y - 1] + possible[2][x - 1][y - 1]
                if self.board[x][y] == 0:
                    possible[0][x][y] = possible[0][x][y - 1] + \
                        possible[2][x][y - 1]
                    possible[1][x][y] = possible[1][x - 1][y] + \
                        possible[2][x - 1][y]
        return sum(possible[i][-1][-1] for i in range(3))


def main():
    room = Home()
    print(room.move_pipes())


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
