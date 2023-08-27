import sys
from collections import deque


class Dice:
    def __init__(self) -> None:
        self.pip_hori = deque([0] * 4)
        self.pip_verti = deque([0] * 4)
        self.top, self.bot = 1, 3
        self.N: int
        self.M: int
        self.x: int
        self.y: int
        self.cmd: list[int]
        self.map: list[list[int]]
        self.get_info()

    def get_info(self) -> None:
        self.N, self.M, self.x, self.y, K = map(int, input().split())
        self.map = [list(map(int, input().split())) for _ in range(self.N)]
        self.cmd = list(map(int, input().split()))

    def roll(self, cmd: int) -> None:
        verti, hori = self.pip_verti, self.pip_hori
        top, bot = self.top, self.bot
        if cmd == 1:
            hori.appendleft(hori.pop())
            verti[top], verti[bot] = hori[top], hori[bot]
        elif cmd == 2:
            hori.append(hori.popleft())
            verti[top], verti[bot] = hori[top], hori[bot]
        elif cmd == 3:
            verti.append(verti.popleft())
            hori[top], hori[bot] = verti[top], verti[bot]
        elif cmd == 4:
            verti.appendleft(verti.pop())
            hori[top], hori[bot] = verti[top], verti[bot]

    def move(self) -> list[int]:
        Dx = {1: 0, 2: 0, 3: -1, 4: 1}
        Dy = {1: 1, 2: -1, 3: 0, 4: 0}
        res: list[int] = []
        for c in self.cmd:
            x, y = self.x + Dx[c], self.y + Dy[c]
            if 0 <= x < self.N and 0 <= y < self.M:
                self.x, self.y = x, y
                self.roll(c)
                if self.map[x][y] == 0:
                    self.map[x][y] = self.pip_hori[self.bot]
                else:
                    self.pip_hori[self.bot] = self.pip_verti[self.bot] = self.map[x][y]
                    self.map[x][y] = 0
                res.append(self.pip_hori[self.top])
        return res


def main():
    dice = Dice()
    print(*dice.move(), sep='\n')


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
