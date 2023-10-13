import sys
from collections import deque


class Conveyor:
    def __init__(self) -> None:
        self.N: int
        self.K: int
        self.A: deque[int]
        self.robots: deque[int] = deque()
        self.get_info()

    def get_info(self) -> None:
        self.N, self.K = map(int, input().split())
        self.A = deque(map(int, input().split()))

    def rotate(self) -> int:
        broken = 0
        turn = 0
        while broken < self.K:
            self.A.appendleft(self.A.pop())
            self.robots = deque([x + 1 for x in self.robots])
            if self.robots and self.robots[-1] == self.N - 1:
                self.robots.pop()
            broken += self.move()
            if self.A[0] > 0:
                self.robots.appendleft(0)
                self.A[0] -= 1
                if self.A[0] == 0:
                    broken += 1
            turn += 1
        return turn

    def move(self) -> int:
        robots: deque[int] = deque([])
        broken = 0
        while self.robots:
            x = self.robots.pop()
            npos = x + 1
            if self.A[npos] == 0 or (robots and robots[0] == npos):
                robots.appendleft(x)
                continue
            self.A[npos] -= 1
            if self.A[npos] == 0:
                broken += 1
            if npos != self.N - 1:
                robots.appendleft(npos)
        self.robots = robots
        return broken


def main():
    conv = Conveyor()
    print(conv.rotate())


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
