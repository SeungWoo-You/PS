from collections import defaultdict
import heapq
import sys

class Army:
    def __init__(self, N: int, roads: list) -> None:
        self.N: int = N
        self.roads: defaultdict[int, set[int]] = defaultdict(set)
        for u, v in roads:
            self.roads[u].add(v)
            self.roads[v].add(u)
    
    def comeback(self, home: int) -> list:
        nodes: list[int] = [sys.maxsize] * (self.N + 1)
        nodes[home] = 0
        H: list[tuple[int, int]] = [(0, home)]
        while H:
            d, u = heapq.heappop(H)
            for v in self.roads[u]:
                if d + 1 < nodes[v]:
                    nodes[v] = d + 1
                    heapq.heappush(H, (d + 1, v))
        return nodes
    
def solution(n, roads, sources, destination):
    answer = []
    army = Army(n, roads)
    res = army.comeback(destination)
    for src in sources:
        answer.append(res[src] if res[src] != sys.maxsize else -1)
    return answer