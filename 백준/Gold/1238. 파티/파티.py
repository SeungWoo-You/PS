import sys
from collections import defaultdict
import heapq


class Party:
    def __init__(self) -> None:
        self.N: int
        self.M: int
        self.X: int
        self.road: defaultdict[int, dict[int, int]] = defaultdict(dict)
        self.reverse_road: defaultdict[int, dict[int, int]] = defaultdict(dict)
        self.get_info()

    def get_info(self) -> None:
        self.N, self.M, self.X = map(int, input().split())
        for _ in range(self.M):
            u, v, w = map(int, input().split())
            self.road[u][v] = w
            self.reverse_road[v][u] = w

    def find_cost(self, src: int, road: defaultdict[int, dict[int, int]]) -> dict[int, int]:
        costs = {v: sys.maxsize for v in range(1, self.N + 1)}
        costs[src] = 0
        H = [(costs[src], src)]
        while H:
            c, u = heapq.heappop(H)
            if costs[u] < c:
                continue
            for v, w in road[u].items():
                if c + w < costs[v]:
                    costs[v] = c + w
                    heapq.heappush(H, (costs[v], v))
        return costs

    def find_max(self) -> int:
        costs_to_X = self.find_cost(self.X, self.reverse_road)
        costs_from_X = self.find_cost(self.X, self.road)
        return max(map(sum, zip(costs_from_X.values(), costs_to_X.values())))


def main():
    graph = Party()
    print(graph.find_max())


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
