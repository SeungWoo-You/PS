import sys


class Robot:
    def __init__(self, pos: list[int, int, str]) -> None:
        self.pos: list[int, int, str] = pos

    def turn(self, direction: int) -> dict[str, str]:
        return {
            'W': 'N',
            'N': 'E',
            'E': 'S',
            'S': 'W'
        } if direction == 'R' else {
            'W': 'S',
            'S': 'E',
            'E': 'N',
            'N': 'W'
        }

    def forward(self) -> None:
        x, y, way = self.pos
        if way == 'W':
            dx, dy = (-1, 0)
        elif way == 'S':
            dx, dy = (0, -1)
        elif way == 'E':
            dx, dy = (1, 0)
        else:
            dx, dy = (0, 1)
        self.pos[0], self.pos[1] = x + dx, y + dy

    def move(self, cmd: str) -> None:
        if cmd == 'L' or cmd == 'R':
            self.pos[2] = self.turn(cmd)[self.pos[2]]
        else:
            self.forward()


class Simulation:
    def __init__(self) -> None:
        self.A: int
        self.B: int
        self.N: int
        self.M: int
        self.robots: dict[int, Robot] = {}
        self.cmd_input: list[tuple[int, str, int]] = []
        self.get_info()

    def get_info(self) -> None:
        self.A, self.B = map(int, input().split())
        self.N, self.M = map(int, input().split())
        for i in range(1, self.N + 1):
            info = list(input().strip().split())
            self.robots[i] = Robot([int(info[0]), int(info[1]), info[2]])
        for _ in range(self.M):
            info = list(input().strip().split())
            self.cmd_input.append([int(info[0]), info[1], int(info[2])])

    def run(self) -> None:
        for cmd_in in self.cmd_input:
            r, cmd, iteration = cmd_in
            robot = self.robots[r]
            for _ in range(iteration):
                robot.move(cmd)
                if not (0 < robot.pos[0] <= self.A and 0 < robot.pos[1] <= self.B):
                    print(f'Robot {r} crashes into the wall')
                    return
                for k, another in self.robots.items():
                    if another == robot:
                        continue
                    if another.pos[0] == robot.pos[0] and another.pos[1] == robot.pos[1]:
                        print(f'Robot {r} crashes into robot {k}')
                        return
        print('OK')


def main():
    sim = Simulation()
    sim.run()


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
