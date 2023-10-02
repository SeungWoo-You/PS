import sys


class QueenBee:
    def __init__(self) -> None:
        self.M: int
        self.N: int
        self.larva: list[int]
        self.get_info()

    def get_info(self) -> None:
        self.M, self.N = map(int, input().split())
        self.larva = [1] * (2 * self.M - 1)
        for _ in range(self.N):
            zero, one, two = map(int, input().split())
            mid = zero + one
            end = mid + two
            for i in range(zero, mid):
                self.larva[i] += 1
            for i in range(mid, end):
                self.larva[i] += 2

    def grow(self) -> list[list[int]]:
        board = [[1] * self.M for _ in range(self.M)]
        for i in range(self.M):
            board[self.M - i - 1][0] = self.larva[i]
        for j in range(1, self.M):
            board[0][j] = self.larva[j + self.M - 1]
        for i in range(1, self.M):
            for j in range(1, self.M):
                board[i][j] = max(board[i - 1][j], board[i]
                                  [j - 1], board[i - 1][j - 1])
        return board


def main():
    bee = QueenBee()
    for row in bee.grow():
        print(*row)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
