import sys
from collections import defaultdict, deque


class HyperTube:
    def __init__(self) -> None:
        self.N: int
        self.M: int
        self.K: int
        self.station: defaultdict[int, set[int]] = defaultdict(set)
        self.get_info()

    def get_info(self) -> None:
        self.N, self.K, self.M = map(int, input().split())
        for i in range(1, self.M + 1):
            sta = set(map(int, input().split()))
            self.station[self.N + i].update(sta)
            for s in sta:
                self.station[s].add(i + self.N)

    def transport(self) -> int:
        Q = deque([(1, 1)])
        vistied: set[int] = set()
        while Q:
            u, count = Q.popleft()
            if u == self.N:
                return count
            for v in self.station[u]:
                if v not in vistied:
                    vistied.add(v)
                    if v > self.N:
                        Q.append((v, count))
                    else:
                        Q.append((v, count + 1))
        return -1


def main():
    tube = HyperTube()
    print(tube.transport())


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
