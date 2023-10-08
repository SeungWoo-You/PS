import sys
from collections import deque


class Room:
    def __init__(self) -> None:
        self.N: int
        self.M: int
        self.board: list[list[int]]
        self.get_info()

    def get_info(self) -> None:
        self.N, self.M = map(int, input().split())
        self.board = [list(map(int, input().split())) for _ in range(self.N)]

    def escape(self) -> int:
        possible: set[tuple[int, int]] = set()
        for i, row in enumerate(self.board):
            for j, x in enumerate(row):
                if x != 0:
                    possible.add((i, j))
        Dx = [0, 0, -1, 1]
        Dy = [-1, 1, 0, 0]
        dist = 0
        password = 0
        while possible:
            i, j = possible.pop()
            Q: deque[tuple[int, int, int]] = deque([(0, i, j)])
            visited: set[tuple[int, int]] = set()
            start = self.board[i][j]
            end = start
            temp = 0
            while Q:
                d, i, j = Q.popleft()
                if (i, j) in visited:
                    continue
                if d >= temp:
                    end = self.board[i][j] if d > temp else max(
                        end, self.board[i][j])
                    temp = d
                visited.add((i, j))
                for dx, dy in zip(Dx, Dy):
                    x, y = i + dx, j + dy
                    if 0 <= x < self.N and 0 <= y < self.M and self.board[x][y] != 0:
                        Q.append((d + 1, x, y))
            if temp >= dist:
                password = start + \
                    end if temp > dist else max(password, start + end)
                dist = temp
        return password


def main():
    room = Room()
    print(room.escape())


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
