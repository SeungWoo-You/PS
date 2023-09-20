import sys


class City:
    def __init__(self) -> None:
        self.N: int
        self.L: int
        self.road: list[list[int]]
        self.get_info()

    def get_info(self) -> None:
        self.N, self.L = map(int, input().split())
        self.road = [list(map(int, input().split())) for _ in range(self.N)]

    def put_slope(self, line: list[int]) -> bool:
        placeable: list[int] = [True] * self.N
        prev_h = line[0]
        i = 1
        while i < self.N:
            h = line[i]
            if h == prev_h:
                i += 1
            elif prev_h - h == 1:
                for j in range(i, i + self.L):
                    if (j >= self.N) or (line[j] != h) or (placeable[j] == False):
                        return False
                    placeable[j] = False
                prev_h = line[j]
                i = j + 1
            elif h - prev_h == 1:
                for j in range(i - self.L, i):
                    if (j < 0) or (line[j] != prev_h) or (placeable[j] == False):
                        return False
                    placeable[j] = False
                prev_h = line[i]
                i += 1
            else:
                return False
        return True

    def find_way(self) -> int:
        count = 0
        for p in range(self.N):
            row = self.road[p]
            col = [self.road[i][p] for i in range(self.N)]
            if self.put_slope(row):
                count += 1
            if self.put_slope(col):
                count += 1
        return count


def main():
    city = City()
    print(city.find_way())


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
