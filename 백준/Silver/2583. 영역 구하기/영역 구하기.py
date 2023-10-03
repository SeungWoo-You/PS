import sys
from collections import deque


class Paper:
    def __init__(self) -> None:
        self.M: int
        self.N: int
        self.K: int
        self.area: list[list[int]]
        self.get_info()

    def get_info(self) -> None:
        self.M, self.N, self.K = map(int, input().split())
        self.area = [[0] * self.N for _ in range(self.M)]
        for _ in range(self.K):
            y1, x1, y2, x2 = map(int, input().split())
            for x in range(x1, x2):
                for y in range(y1, y2):
                    self.area[x][y] = 1

    def find_empty(self) -> set[tuple[int, int]]:
        empty: set[tuple[int, int]] = set()
        for i in range(self.M):
            for j in range(self.N):
                if self.area[i][j] == 0:
                    empty.add((i, j))
        return empty

    def divide(self) -> list[int]:
        E = self.find_empty()
        result: list[int] = []
        Dx = [0, 0, -1, 1]
        Dy = [-1, 1, 0, 0]
        while E:
            T = E.pop()
            Q: deque[tuple[int, int]] = deque([T])
            checked: set[tuple[int, int]] = set()
            while Q:
                i, j = Q.popleft()
                if (i, j) in checked:
                    continue
                checked.add((i, j))
                for dx, dy in zip(Dx, Dy):
                    x, y = i + dx, j + dy
                    if 0 <= x < self.M and 0 <= y < self.N and (x, y) in E:
                        Q.append((x, y))
            E.difference_update(checked)
            result.append(len(checked))
        result.sort()
        return result


def main():
    paper = Paper()
    answer = paper.divide()
    print(len(answer))
    print(*answer)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
