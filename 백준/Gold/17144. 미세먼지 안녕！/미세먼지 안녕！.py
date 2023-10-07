import sys
from collections import deque
from copy import deepcopy


class Room:
    def __init__(self) -> None:
        self.R: int
        self.C: int
        self.T: int
        self.board: list[list[int]]
        self.purifier: list[int] = []
        self.get_info()

    def get_info(self) -> None:
        self.R, self.C, self.T = map(int, input().split())
        self.room: list[list[int]] = []
        for i in range(self.R):
            line = map(int, input().split())
            self.room.append([])
            for x in line:
                if x == -1:
                    self.purifier.append(i)
                self.room[i].append(x)

    def spread_dust(self) -> None:
        Dx = [0, 0, -1, 1]
        Dy = [-1, 1, 0, 0]
        room = deepcopy(self.room)
        for i, row in enumerate(self.room):
            for j, dust in enumerate(row):
                if dust > 4:
                    d = dust // 5
                    for dx, dy in zip(Dx, Dy):
                        x, y = i + dx, j + dy
                        if 0 <= x < self.R and 0 <= y < self.C and room[x][y] != -1:
                            room[x][y] += d
                            room[i][j] -= d
        self.room = room

    def clean(self) -> None:
        Q: deque[int] = deque()
        tx = self.purifier[0]
        Q.extend(self.room[tx][1:])
        for x in range(tx - 1, -1, -1):
            Q.append(self.room[x][-1])
        Q.extend(reversed(self.room[0][:-1]))
        for x in range(1, tx - 1):
            Q.append(self.room[x][0])
        Q.appendleft(0)
        x, y = tx, 1
        dx, dy = 0, 1
        for dust in Q:
            self.room[x][y] = dust
            if y + dy >= self.C:
                dx, dy = -1, 0
            elif x + dx < 0:
                dx, dy = 0, -1
            elif y + dy < 0:
                dx, dy = 1, 0
            x, y = x + dx, y + dy

        Q: deque[int] = deque()
        bx = self.purifier[1]
        Q.extend(self.room[bx][1:])
        for x in range(bx + 1, self.R):
            Q.append(self.room[x][-1])
        Q.extend(reversed(self.room[-1][:-1]))
        for x in range(self.R - 2, bx + 1, -1):
            Q.append(self.room[x][0])
        Q.appendleft(0)
        x, y = bx, 1
        dx, dy = 0, 1
        for dust in Q:
            self.room[x][y] = dust
            if y + dy >= self.C:
                dx, dy = 1, 0
            elif x + dx >= self.R:
                dx, dy = 0, -1
            elif y + dy < 0:
                dx, dy = -1, 0
            x, y = x + dx, y + dy


def main():
    home = Room()
    for _ in range(home.T):
        home.spread_dust()
        home.clean()
    count = 2
    for row in home.room:
        count += sum(row)
    print(count)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
