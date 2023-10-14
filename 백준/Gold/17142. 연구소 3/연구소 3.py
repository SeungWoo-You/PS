import sys
from copy import deepcopy
from collections import deque


class combinations:
    def __init__(self, ls: list, r: int) -> None:
        self.N = len(ls)
        self.r = r
        self.ls = ls
        self.answer: list = []

    def nCr(self, visited: list = [], i: int = 0) -> None:
        if len(visited) == self.r:
            self.answer.append(deepcopy(visited))
            return
        if i == self.N:
            return
        visited.append(self.ls[i])
        self.nCr(visited, i + 1)
        visited.pop()
        self.nCr(visited, i + 1)


class Lab:
    def __init__(self) -> None:
        self.N: int
        self.M: int
        self.board: list[list[int]]
        self.get_info()

    def get_info(self) -> None:
        self.N, self.M = map(int, input().split())
        self.board = [list(map(int, input().split())) for _ in range(self.N)]

    def spread(self) -> int:
        virus: list[tuple[int, int]] = []
        empty: set[tuple[int, int]] = set()
        for i, row in enumerate(self.board):
            for j, x in enumerate(row):
                if x == 0:
                    empty.add((i, j))
                elif x == 2:
                    virus.append((i, j))
        C = combinations(virus, self.M)
        C.nCr()
        Dx = [0, 0, -1, 1]
        Dy = [-1, 1, 0, 0]
        total = sys.maxsize
        for V in C.answer:
            V: list[tuple[int, int]]
            Q: deque[tuple[int, int, int]] = deque([(0, *T) for T in V])
            checked: set[tuple[int, int]] = set()
            while Q:
                d, i, j = Q.popleft()
                if (i, j) in checked:
                    continue
                checked.add((i, j))
                if checked.issuperset(empty):
                    total = min(total, d)
                    break
                for dx, dy in zip(Dx, Dy):
                    x, y = i + dx, j + dy
                    if 0 <= x < self.N and 0 <= y < self.N and self.board[x][y] != 1:
                        Q.append((d + 1, x, y))
        return total


def main():
    lab = Lab()
    result = lab.spread()
    print(result if result != sys.maxsize else -1)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
