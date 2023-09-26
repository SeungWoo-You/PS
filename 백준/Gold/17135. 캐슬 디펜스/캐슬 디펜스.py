import sys
from itertools import combinations
from collections import deque
from copy import deepcopy


class Game:
    def __init__(self) -> None:
        self.N: int
        self.M: int
        self.D: int
        self.board: list[list[int]]
        self.get_info()

    def get_info(self) -> None:
        self.N, self.M, self.D = map(int, input().split())
        self.board = [list(map(int, input().split())) for _ in range(self.N)]

    def iskeep(self, board: list[list[int]]) -> bool:
        for row in board:
            for x in row:
                if x == 1:
                    return True
        return False

    def place_archer(self) -> int:
        answer = 0
        for T in combinations(range(self.M), 3):
            board = deque(deepcopy(self.board))
            kill = 0
            while self.iskeep(board) == True:
                attacked = self.play(board, T)
                for i, j in attacked:
                    board[i][j] = 0
                    kill += 1
                board.pop()
                board.appendleft([0] * self.M)
            answer = max(answer, kill)
        return answer

    def play(self, board: deque[list[int]], archer: tuple[int, int, int]) -> set[tuple[int, int]]:
        attacked: set[tuple[int, int]] = set()
        Dx = [0, -1, 0]
        Dy = [-1, 0, 1]
        for j in archer:
            Q = deque([(self.N - 1, j, 1)])
            checked: set[tuple[int, int]] = set()
            while Q:
                i, j, d = Q.popleft()
                if d <= self.D:
                    if board[i][j] == 1:
                        attacked.add((i, j))
                        break
                else:
                    continue
                if (i, j) in checked:
                    continue
                checked.add((i, j))
                for dx, dy in zip(Dx, Dy):
                    x, y = i + dx, j + dy
                    if 0 <= x < self.N and 0 <= y < self.M:
                        Q.append((x, y, d + 1))
        return attacked


def main():
    game = Game()
    print(game.place_archer())


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
