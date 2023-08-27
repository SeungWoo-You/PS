import sys
from itertools import combinations


class Delivery:
    def __init__(self) -> None:
        self.N: int
        self.M: int
        self.city: list[list[int]]
        self.house: set[tuple[int, int]] = set()
        self.chicken: set[tuple[int, int]] = set()
        self.get_info()

    def get_info(self) -> None:
        self.N, self.M = map(int, input().split())
        self.city = [list(map(int, input().split())) for _ in range(self.N)]
        for i, row in enumerate(self.city):
            for j, building in enumerate(row):
                if building == 1:
                    self.house.add((i, j))
                elif building == 2:
                    self.chicken.add((i, j))

    def dist(self, chicken: tuple[tuple[int, int], ...]) -> int:
        result = 0
        for home in self.house:
            d = sys.maxsize
            for chick in chicken:
                d = min(d, manhattan(chick, home))
            result += d
        return result

    def choose(self) -> int:
        result = sys.maxsize
        for C in combinations(self.chicken, self.M):
            result = min(result, self.dist(C))
        return result


def main():
    deliv = Delivery()
    print(deliv.choose())


def manhattan(A: tuple[int, int], B: tuple[int, int]) -> int:
    return abs(A[0] - B[0]) + abs(A[1] - B[1])


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
