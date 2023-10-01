import sys
from collections import deque


class Treasure_Island:
    def __init__(self) -> None:
        self.M: int
        self.N: int
        self.guide_map: list[str]
        self.lands: set[tuple[int, int]] = set()
        self.get_info()

    def get_info(self) -> None:
        self.M, self.N = map(int, input().split())
        self.guide_map = [''] * self.M
        for i in range(self.M):
            line = list(input())
            for j, x in enumerate(line):
                if x == 'L':
                    self.lands.add((i, j))
                self.guide_map[i] += x

    def find(self) -> int:
        answer = 0
        Dx = [0, 0, -1, 1]
        Dy = [-1, 1, 0, 0]
        for i, j in self.lands:
            Q = deque([(i, j, 0)])
            checked: set[tuple[int, int]] = set()
            dist = 0
            while Q:
                i, j, d = Q.popleft()
                if (i, j) in checked:
                    continue
                dist = max(dist, d)
                checked.add((i, j))
                for dx, dy in zip(Dx, Dy):
                    x, y = i + dx, j + dy
                    if 0 <= x < self.M and 0 <= y < self.N and self.guide_map[x][y] == 'L':
                        Q.append((x, y, d + 1))
            answer = max(answer, dist)
        return answer


def main():
    treasure = Treasure_Island()
    print(treasure.find())


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
