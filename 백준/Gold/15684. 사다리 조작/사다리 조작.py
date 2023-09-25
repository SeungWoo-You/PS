import sys


class Game:
    def __init__(self) -> None:
        self.N: int
        self.M: int
        self.H: int
        self.ladders: list[list[int]] = []
        self.get_info()

    def get_info(self) -> None:
        self.N, self.M, self.H = map(int, input().split())
        self.ladders = [[0] * self.N for _ in range(self.H)]
        for _ in range(self.M):
            h, n = map(int, input().split())
            self.ladders[h - 1][n - 1] = 1
            self.ladders[h - 1][n] = 2

    def modify(self, i: int, col: int) -> int:
        if i > 3:
            return sys.maxsize
        total = sys.maxsize
        if self.run() == True:
            return i
        for h in range(self.H):
            for n in range(col, self.N - 1):
                if self.ladders[h][n] == 0 and self.ladders[h][n + 1] == 0:
                    self.ladders[h][n] = 1
                    self.ladders[h][n + 1] = 2
                    total = min(total, self.modify(i + 1, n))
                    self.ladders[h][n] = 0
                    self.ladders[h][n + 1] = 0
        return total

    def run(self) -> bool:
        for n in range(self.N):
            i = n
            for h in range(self.H):
                if self.ladders[h][i] == 1:
                    i += 1
                elif self.ladders[h][i] == 2:
                    i -= 1
            if i != n:
                return False
        return True


def main():
    game = Game()
    answer = game.modify(0, 0)
    print(answer if answer != sys.maxsize else -1)


if __name__ == '__main__':
    input = sys.stdin.readline
    sys.setrecursionlimit(10**5)
    main()
