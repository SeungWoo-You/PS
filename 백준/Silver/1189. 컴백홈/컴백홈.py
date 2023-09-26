import sys


class Route:
    def __init__(self) -> None:
        self.R: int
        self.C: int
        self.K: int
        self.road: list[str]
        self.get_info()

    @property
    def src(self) -> tuple[int, int]:
        return (self.R - 1, 0)

    @property
    def home(self) -> tuple[int, int]:
        return (0, self.C - 1)

    def get_info(self) -> None:
        self.R, self.C, self.K = map(int, input().split())
        self.road = [input().strip() for _ in range(self.R)]

    def find(self, way: list[tuple[int, int]]) -> int:
        count = 0
        if len(way) == self.K:
            if way[-1] == self.home:
                return 1
            else:
                return 0
        Dx = [0, 0, -1, 1]
        Dy = [-1, 1, 0, 0]
        i, j = way[-1]
        for dx, dy in zip(Dx, Dy):
            x, y = i + dx, j + dy
            if 0 <= x < self.R and 0 <= y < self.C and self.road[x][y] == '.':
                if (x, y) not in way:
                    L = way.copy()
                    L.append((x, y))
                    count += self.find(L)
        return count


def main():
    route = Route()
    print(route.find([(route.src)]))


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
