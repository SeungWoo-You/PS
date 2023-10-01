import sys
from collections import defaultdict
import heapq


class Highway:
    def __init__(self) -> None:
        self.N: int
        self.D: int
        self.road: defaultdict[int, dict[int, int]] = defaultdict(dict)
        self.get_info()

    def get_info(self) -> None:
        self.N, self.D = map(int, input().split())
        self.end = self.D
        checked: set[tuple[int, int]] = set()
        self.road[0][self.D] = self.D
        node: set[int] = set([0, self.D])
        checked.add((0, self.D))
        for _ in range(self.N):
            u, v, d = map(int, input().split())
            self.road[u][v] = min(self.road[u][v], d) if (
                u, v) in checked else d
            checked.add((u, v))
            node.update([u, v])
        for u in node:
            for v in node:
                if u < v:
                    self.road[u][v] = min(
                        self.road[u][v], v - u) if (u, v) in checked else v - u

    def drive(self) -> int:
        dist = {v: sys.maxsize for v in self.road.keys()}
        for X in self.road.values():
            for k in X.keys():
                dist[k] = sys.maxsize
        dist[0] = 0
        H: list[tuple[int, int]] = [(0, 0)]
        while H:
            d, u = heapq.heappop(H)
            for v, w in self.road[u].items():
                if dist[v] > d + w:
                    dist[v] = d + w
                    heapq.heappush(H, (dist[v], v))
        return dist[self.D]


def main():
    highway = Highway()
    print(highway.drive())


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
