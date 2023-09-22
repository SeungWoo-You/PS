import sys
from collections import deque


class Gear:
    def __init__(self) -> None:
        self.tooth = deque(map(int, list(input().strip())))

    @property
    def left(self) -> int:
        return self.tooth[-2]

    @property
    def right(self) -> int:
        return self.tooth[2]

    def rotate(self, way: str) -> None:
        if way == 'CCW':
            self.tooth.append(self.tooth.popleft())
        elif way == 'CW':
            self.tooth.appendleft(self.tooth.pop())


class Machine:
    def __init__(self) -> None:
        self.gears: dict[int, Gear]
        self.K: int
        self.cmd: list[list[int]]
        self.get_info()

    def get_info(self) -> None:
        self.gears = {i: Gear() for i in range(1, 5)}
        self.K = int(input())
        self.cmd = [list(map(int, input().split())) for _ in range(self.K)]

    @property
    def direction(self) -> dict[int, str]:
        return {
            1: 'CW',
            -1: 'CCW'
        }

    def run(self) -> int:
        for g, d in self.cmd:
            checked: set[tuple[int, int]] = set()
            S = [(g, d)]
            while S:
                i, w = S.pop()
                if (i, w) in checked:
                    continue
                checked.add((i, w))
                x = i - 1
                if x in self.gears and self.gears[x].right != self.gears[i].left:
                    S.append((x, -w))
                x = i + 1
                if x in self.gears and self.gears[x].left != self.gears[i].right:
                    S.append((x, -w))
            for i, w in checked:
                way = self.direction[w]
                self.gears[i].rotate(way)
        return self.calc_score()

    def calc_score(self) -> int:
        return sum([self.gears[i].tooth[0] * 2**(i - 1) for i in range(1, 5)])


def main():
    machine = Machine()
    print(machine.run())


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
