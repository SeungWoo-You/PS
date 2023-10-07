from collections import defaultdict
import heapq
import sys


class Delivery:
    def __init__(self, N, road, K) -> None:
        self.N: int = N
        self.road: defaultdict[int, dict[int, int]] = defaultdict(dict)
        for u, v, w in road:
            self.road[u][v] = min(self.road[u][v], w) if v in self.road[u] else w
            self.road[v][u] = min(self.road[v][u], w) if u in self.road[v] else w
        self.K: int = K
    
    def find(self) -> list:
        res = [sys.maxsize] * (self.N + 1)
        src = 1
        res[src] = 0
        H: list[tuple[int, int]] = [(res[src], src)]
        while H:
            d, u = heapq.heappop(H)
            for v, w in self.road[u].items():
                if res[v] > d + w:
                    res[v] = d + w
                    heapq.heappush(H, (res[v], v))
        return res


def solution(N, road, K):
    deliv = Delivery(N, road, K)
    res: list[int] = deliv.find()
    answer = 0
    for x in res:
        if x <= K:
            answer += 1
    return answer