import sys
from collections import defaultdict


class City:
    def __init__(self) -> None:
        self.N: int
        self.M: int
        self.bus: defaultdict[int, dict[int, int]] = defaultdict(dict)
        self.get_info()

    def get_info(self) -> None:
        self.N, self.M = map(int, input().split())
        checked: set[tuple[int, int]] = set()
        for _ in range(self.M):
            u, v, t = map(int, input().split())
            self.bus[u][v] = min(self.bus[u][v], t) if (u, v) in checked else t
            checked.add((u, v))

    def find_route(self) -> tuple[bool, dict[int, int]]:
        route = {v: sys.maxsize for v in range(1, self.N + 1)}
        loop = False
        route[1] = 0
        for i in range(self.N):
            for u, sub in self.bus.items():
                for v, t in sub.items():
                    if route[u] != sys.maxsize and route[u] + t < route[v]:
                        route[v] = route[u] + t
                        if i == self.N - 1:
                            loop = True
        return loop, route


def main():
    city = City()
    loop, route = city.find_route()
    if loop == True:
        print(-1)
    else:
        for v in range(2, city.N + 1):
            print(route[v] if route[v] != sys.maxsize else -1)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
