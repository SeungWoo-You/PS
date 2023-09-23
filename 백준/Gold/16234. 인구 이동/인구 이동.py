import sys
from itertools import product


class Population:
    def __init__(self) -> None:
        self.N: int
        self.L: int
        self.R: int
        self.land: list[list[int]]
        self.get_info()

    def get_info(self) -> None:
        self.N, self.L, self.R = map(int, input().split())
        self.land = [list(map(int, input().split())) for _ in range(self.N)]

    def move(self) -> int:
        loop = -1
        gp = 0
        Dx = [0, 0, -1, 1]
        Dy = [-1, 1, 0, 0]
        while gp != self.N**2:
            possible = set([T for T in product(range(self.N), repeat=2)])
            full: list[set[tuple[int, int]]] = []
            while possible:
                S: list[tuple[int, int]] = [possible.pop()]
                checked: set[tuple[int, int]] = set()
                while S:
                    i, j = S.pop()
                    if (i, j) in checked:
                        continue
                    checked.add((i, j))
                    possible.discard((i, j))
                    for dx, dy in zip(Dx, Dy):
                        x, y = i + dx, j + dy
                        if 0 <= x < self.N and 0 <= y < self.N:
                            if self.L <= abs(self.land[x][y] - self.land[i][j]) <= self.R:
                                S.append((x, y))
                full.append(checked)
            for F in full:
                human = sum([self.land[i][j] for i, j in F])
                count = len(F)
                balanced = human // count
                for i, j in F:
                    self.land[i][j] = balanced
            gp = len(full)
            loop += 1
        return loop


def main():
    pops = Population()
    print(pops.move())


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
