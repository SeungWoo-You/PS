import sys


class Cheese:
    def __init__(self) -> None:
        self.N: int
        self.M: int
        self.cheese: set[tuple[int, int]] = set()
        self.outside: set[tuple[int, int]] = set()
        self.get_info()

    def get_info(self) -> None:
        self.N, self.M = map(int, input().split())
        for i in range(self.N):
            for j, x in enumerate(map(int, input().split())):
                if x == 1:
                    self.cheese.add((i, j))
                else:
                    self.outside.add((i, j))

    def melt(self) -> int:
        Dx = [0, 0, -1, 1]
        Dy = [-1, 1, 0, 0]
        count = 0

        while self.cheese:
            checked = [[False] * self.M for _ in range(self.N)]
            air = [(0, 0)]
            while air:
                i, j = air.pop()
                checked[i][j] = True
                for dx, dy in zip(Dx, Dy):
                    x, y = i + dx, j + dy
                    if 0 <= x < self.N and 0 <= y < self.M and (x, y) in self.outside and checked[x][y] == False:
                        air.append((x, y))

            melted: set[tuple[int, int]] = set()
            for chz in self.cheese:
                k = 0
                i, j = chz
                for dx, dy in zip(Dx, Dy):
                    x, y = i + dx, j + dy
                    if 0 <= x < self.N and 0 <= y < self.M and checked[x][y] == True:
                        k += 1
                if k >= 2:
                    melted.add(chz)
            self.cheese.difference_update(melted)
            self.outside = self.outside.union(melted)
            count += 1
        return count


def main():
    chz = Cheese()
    print(chz.melt())


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
