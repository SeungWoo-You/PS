import sys
from collections import deque

class Apartment:
    def __init__(self) -> None:
        self.N: int
        self.land: list[list[int]] = []
        self.house: set[tuple[int, int]] = set()
        self.get_info()
        

    def get_info(self) -> None:
        self.N = int(input())
        for i in range(self.N):
            row = map(int, list(input().strip()))
            self.land.append([])
            for j, x in enumerate(row):
                if x == 1:
                    self.house.add((i, j))
                self.land[i].append(x)
    
    def grouping(self) -> list[int]:
        Dx = [0, 0, -1, 1]
        Dy = [-1, 1, 0, 0]
        group: list[int] = []
        while self.house:
            src = self.house.pop()
            self.house.add(src)
            Q = deque([src])
            checked: set[tuple[int, int]] = set()
            while Q:
                i, j = Q.popleft()
                if (i, j) in checked:
                    continue
                self.house.discard((i, j))
                checked.add((i, j))
                for dx, dy in zip(Dx, Dy):
                    x, y = i + dx, j + dy
                    if 0 <= x < self.N and 0 <= y < self.N and self.land[x][y] == 1:
                        Q.append((x, y))
            group.append(len(checked))
        return group

def main():
    apart = Apartment()
    G = apart.grouping()
    print(len(G))
    G.sort()
    print(*G, sep='\n')


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
