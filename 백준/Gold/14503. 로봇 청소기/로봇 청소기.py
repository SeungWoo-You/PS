import sys


class Robot_Vacuum:
    def __init__(self) -> None:
        self.N: int
        self.M: int
        self.r: int
        self.c: int
        self.d: int
        self.room: list[list[int]]
        self.get_info()

    def get_info(self) -> None:
        self.N, self.M = map(int, input().split())
        self.r, self.c, self.d = map(int, input().split())
        self.room = [list(map(int, input().split())) for _ in range(self.N)]

    def clean(self) -> int:
        room = self.room
        Dx = [0, 0, -1, 1]
        Dy = [-1, 1, 0, 0]
        count = 0

        while True:
            keep = False
            if room[self.r][self.c] == 0:
                room[self.r][self.c] = -1
                count += 1
            for dx, dy in zip(Dx, Dy):
                x, y = self.r + dx, self.c + dy
                if 0 <= x < self.N and 0 <= y < self.M and room[x][y] == 0:
                    keep = True

            if keep == False:
                dx, dy = self.moving_direction(reverse=True)
                x, y = self.r + dx, self.c + dy
                if 0 <= x < self.N and 0 <= y < self.M and room[x][y] != 1:
                    self.r, self.c = x, y
                else:
                    break

            elif keep == True:
                self.d = (self.d - 1) % 4
                dx, dy = self.moving_direction()
                x, y = self.r + dx, self.c + dy
                if 0 <= x < self.N and 0 <= y < self.M and room[x][y] == 0:
                    self.r, self.c = x, y
        return count

    def moving_direction(self, reverse: bool = False) -> tuple[int, int]:
        if self.d == 0:
            dx, dy = -1, 0
        elif self.d == 1:
            dx, dy = 0, 1
        elif self.d == 2:
            dx, dy = 1, 0
        elif self.d == 3:
            dx, dy = 0, -1
        return (dx, dy) if reverse == False else (-dx, -dy)


def main():
    robot = Robot_Vacuum()
    print(robot.clean())


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
