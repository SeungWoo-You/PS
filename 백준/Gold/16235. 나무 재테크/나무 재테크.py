import sys
from collections import deque


class Land:
    def __init__(self) -> None:
        self.N: int
        self.M: int
        self.K: int
        self.A: list[list[int]]
        self.trees: list[list[deque[int]]]
        self.nourishment: list[list[int]]
        self.get_info()

    def get_info(self) -> None:
        self.N, self.M, self.K = map(int, input().split())
        self.A = [list(map(int, input().split())) for _ in range(self.N)]
        self.trees = [[deque([]) for _ in range(self.N)]
                      for _ in range(self.N)]
        self.nourishment = [[5] * self.N for _ in range(self.N)]
        for _ in range(self.M):
            x, y, t = map(int, input().split())
            self.trees[x - 1][y - 1].append(t)

    def invest(self) -> None:
        for _ in range(self.K):
            self.spring_summer_winter()
            self.autumn()

    def spring_summer_winter(self) -> None:
        for i, row in enumerate(self.trees):
            for j, T in enumerate(row):
                Q: deque[int] = deque([])
                dead = 0
                for t in T:
                    if t > self.nourishment[i][j]:
                        dead += t // 2
                    else:
                        self.nourishment[i][j] -= t
                        Q.append(t + 1)
                self.trees[i][j] = Q
                self.nourishment[i][j] += dead + self.A[i][j]

    def autumn(self) -> None:
        after: list[list[deque[int]]] = [
            [deque([]) for _ in range(self.N)] for _ in range(self.N)]
        Dx = [0, 0, -1, 1, -1, -1, 1, 1]
        Dy = [-1, 1, 0, 0, -1, 1, -1, 1]
        for i, row in enumerate(self.trees):
            for j, T in enumerate(row):
                for t in T:
                    if t % 5 == 0:
                        for dx, dy in zip(Dx, Dy):
                            x, y = i + dx, j + dy
                            if 0 <= x < self.N and 0 <= y < self.N:
                                after[x][y].appendleft(1)
                    after[i][j].append(t)
        self.trees = after

    def count_tree(self) -> int:
        lives = 0
        for row in self.trees:
            lives += sum([len(T) for T in row])
        return lives


def main():
    land = Land()
    land.invest()
    print(land.count_tree())


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
