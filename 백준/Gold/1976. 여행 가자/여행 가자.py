import sys
from collections import defaultdict, deque


class Trip:
    def __init__(self) -> None:
        self.N: int
        self.M: int
        self.road: defaultdict[int, list[int]] = defaultdict(list)
        self.seq: list[int]
        self.get_info()

    def get_info(self) -> None:
        self.N = int(input())
        self.M = int(input())
        for i in range(1, self.N + 1):
            line = map(int, input().split())
            for j, x in enumerate(line, start=1):
                if x == 1:
                    self.road[i].append(j)
        self.seq = list(map(int, input().split()))

    def is_possible(self) -> bool:
        Q: deque[int] = deque([self.seq[0]])
        checked: set[int] = set()
        while Q:
            u = Q.popleft()
            if u in checked:
                continue
            checked.add(u)
            Q.extend(self.road[u])
        return checked.issuperset(set(self.seq))


def main():
    trip = Trip()
    print('YES' if trip.is_possible() else 'NO')


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
