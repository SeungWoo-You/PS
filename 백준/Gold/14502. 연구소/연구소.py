import sys
from itertools import combinations


class Lab:
    def __init__(self) -> None:
        self.N: int
        self.M: int
        self.virus: set[tuple[int, int]] = set()
        self.empty: set[tuple[int, int]] = set()
        self.wall: set[tuple[int, int]] = set()
        self.get_info()

    def get_info(self) -> None:
        self.N, self.M = map(int, input().split())
        for i in range(self.N):
            row = map(int, input().split())
            for j, elem in enumerate(row):
                if elem == 2:
                    self.virus.add((i, j))
                elif elem == 1:
                    self.wall.add((i, j))
                else:
                    self.empty.add((i, j))

    def spread(self, empty: set[tuple[int, int]]) -> set[tuple[int, int]]:
        virus = self.virus.copy()
        Dx = [0, 0, -1, 1]
        Dy = [-1, 1, 0, 0]
        while virus:
            i, j = virus.pop()
            for dx, dy in zip(Dx, Dy):
                x, y = i + dx, j + dy
                if (x, y) in empty:
                    empty.remove((x, y))
                    virus.add((x, y))
        return empty

    def find_zone(self) -> int:
        size = 0
        for sel in combinations(self.empty, 3):
            empty = self.empty.copy()
            empty.difference_update(sel)
            empty = self.spread(empty)
            size = max(size, len(empty))
        return size


def main():
    lab = Lab()
    print(lab.find_zone())


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
