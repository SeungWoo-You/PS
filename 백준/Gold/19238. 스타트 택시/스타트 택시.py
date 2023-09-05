import sys
from collections import deque


class Taxi:
    def __init__(self) -> None:
        self.N: int
        self.M: int
        self.fuel: int
        self.area: list[list[int]]
        self.pos: tuple[int, int]
        self.customers: dict[int, list[tuple[int, int]]] = {}
        self.get_info()

    def get_info(self) -> None:
        self.N, self.M, self.fuel = map(int, input().split())
        self.area = [[1] * (self.N + 1)]
        for _ in range(self.N):
            info = deque(map(int, input().split()))
            info.appendleft(1)
            self.area.append(list(info))
        self.pos = list(map(int, input().split()))
        for i in range(2, self.M + 2):
            info = list(map(int, input().split()))
            self.customers[i] = [tuple(info[0:2]), tuple(info[2:])]
            self.area[info[0]][info[1]] = i

    def find_customer(self) -> tuple[int, int]:
        if self.area[self.pos[0]][self.pos[1]] not in {0, 1}:
            cust = self.area[self.pos[0]][self.pos[1]]
            return (cust, 0)
        Q = deque([(*self.pos, 0)])
        visited: set[tuple[int, int]] = set()
        candidates: list[tuple[int, ...]] = []
        Dx = [0, 0, -1, 1]
        Dy = [-1, 1, 0, 0]
        while Q:
            i, j, d = Q.popleft()
            if (i, j) in visited:
                continue
            if candidates and d > candidates[0][0]:
                break
            visited.add((i, j))
            for dx, dy in zip(Dx, Dy):
                x, y = i + dx, j + dy
                if 0 < x <= self.N and 0 < y <= self.N and self.area[x][y] != 1:
                    place = self.area[x][y]
                    if place != 0:
                        candidates.append(
                            (d + 1, *self.customers[place][0], place))
                    Q.append((x, y, d + 1))
        candidates.sort()
        return (candidates[0][-1], candidates[0][0]) if candidates else (-1, -1)

    def drive(self, cust: int) -> int:
        src = self.pos
        dst = self.customers[cust][1]
        Q = deque([(*src, 0)])
        visited: set[tuple[int, int]] = set()
        Dx = [0, 0, -1, 1]
        Dy = [-1, 1, 0, 0]
        while Q:
            i, j, d = Q.popleft()
            if (i, j) in visited:
                continue
            if (i, j) == dst:
                return d
            visited.add((i, j))
            for dx, dy in zip(Dx, Dy):
                x, y = i + dx, j + dy
                if 0 < x <= self.N and 0 < y <= self.N and self.area[x][y] != 1:
                    Q.append((x, y, d + 1))
        return -1

    def work(self) -> None:
        while self.customers:
            cust, d = self.find_customer()
            if cust == -1 or self.check_fuel(d) == False:
                print(-1)
                return
            i, j = self.customers[cust][0]
            self.pos = (i, j)
            d = self.drive(cust)
            if d == -1 or self.check_fuel(d) == False:
                print(-1)
                return
            self.fuel += d * 2
            self.area[i][j] = 0
            self.pos = self.customers[cust][1]
            self.customers.pop(cust)
        print(self.fuel)

    def check_fuel(self, d: int) -> bool:
        self.fuel -= d
        return False if self.fuel < 0 else True


def main():
    taxi = Taxi()
    taxi.work()


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
