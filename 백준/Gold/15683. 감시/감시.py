import sys
from itertools import product
from copy import deepcopy


class Watch:
    def __init__(self) -> None:
        self.N: int
        self.M: int
        self.office: list[list[int]] = []
        self.cctv: list[int] = []
        self.get_info()

    @property
    def way(self) -> dict[int, list[str]]:
        return {
            1: ['R', 'B', 'L', 'T'],
            2: ['LR', 'BT'],
            3: ['RB', 'BL', 'LT', 'TR'],
            4: ['RBL', 'BLT', 'LTR', 'TRB'],
            5: ['RBLT']
        }

    @property
    def DxDy(self) -> dict[str, tuple[int, int]]:
        return {
            'R': (0, 1),
            'B': (1, 0),
            'L': (0, -1),
            'T': (-1, 0)
        }

    def get_info(self) -> None:
        self.N, self.M = map(int, input().split())
        for i in range(self.N):
            cell = map(int, input().split())
            self.office.append([])
            for x in cell:
                if x in range(1, 6):
                    self.cctv.append(x)
                self.office[i].append(x)

    def run(self) -> int:
        directions = product(*[self.way[x] for x in self.cctv])
        unreachable = sys.maxsize
        for TVs in directions:
            TVs: tuple[str, ...]
            gen = (tv for tv in TVs)
            office = deepcopy(self.office)
            for i, row in enumerate(office):
                for j, cell in enumerate(row):
                    if cell in range(1, 6):
                        for w in next(gen):
                            x, y = i, j
                            dx, dy = self.DxDy[w]
                            while True:
                                x, y = x + dx, y + dy
                                if 0 <= x < self.N and 0 <= y < self.M:
                                    if office[x][y] == 0:
                                        office[x][y] = -1
                                    elif office[x][y] == 6:
                                        break
                                else:
                                    break
            unreachable = min(unreachable, self.count_unreach(office))
        return unreachable

    def count_unreach(self, office: list[list[int]]) -> int:
        count = 0
        for row in office:
            for x in row:
                if x == 0:
                    count += 1
        return count


def main():
    watching = Watch()
    print(watching.run())


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
