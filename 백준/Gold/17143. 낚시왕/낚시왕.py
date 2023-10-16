import sys


class Shark:
    def __init__(self, x: int, y: int, s: int, d: int, z: int) -> None:
        D = {
            1: (-1, 0),
            2: (1, 0),
            3: (0, 1),
            4: (0, -1)
        }
        self.D: tuple[int, int] = D[d]
        self.pos: tuple[int, int] = (x, y)
        self.size = z
        self.speed = s

    def move(self, R: int, C: int) -> None:
        i, j = self.pos
        dx, dy = self.D
        if dx != 0:
            s = self.speed % (2 * (R - 1))
        elif dy != 0:
            s = self.speed % (2 * (C - 1))
        move = 0
        x = i
        y = j
        while move < s:
            x, y = x + dx, y + dy
            if x < 0 or x >= R or y < 0 or y >= C:
                x, y = x - dx, y - dy
                dx, dy = -dx, -dy
                self.D = (dx, dy)
            else:
                move += 1
        self.pos = (x, y)


class Fishing:
    def __init__(self) -> None:
        self.R: int
        self.C: int
        self.M: int
        self.sharks: dict[int, Shark] = dict()
        self.get_info()

    def get_info(self) -> None:
        self.R, self.C, self.M = map(int, input().split())
        for i in range(self.M):
            x, y, s, d, z = map(int, input().split())
            self.sharks.update({i: Shark(x - 1, y - 1, s, d, z)})

    def play(self) -> int:
        person = 0
        total = 0
        while person < self.C:
            catch: Shark | None = None
            ck = -1
            for k, sh in self.sharks.items():
                if sh.pos[1] == person:
                    if catch == None or catch.pos[0] > sh.pos[0]:
                        catch = sh
                        ck = k
            if catch != None:
                self.sharks.pop(ck)
                total += catch.size
            person += 1
            for sh in self.sharks.values():
                sh.move(self.R, self.C)
            board: list[list[tuple[int, Shark] | None]] = [
                [None] * self.C for _ in range(self.R)]
            sub: dict[int, Shark] = dict()
            for k, sh in self.sharks.items():
                x, y = sh.pos
                if board[x][y] == None:
                    board[x][y] = (k, sh)
                    sub.update({k: sh})
                else:
                    pk, prev = board[x][y]
                    if prev.size < sh.size:
                        sub.pop(pk)
                        sub.update({k: sh})
                        board[x][y] = (k, sh)
            self.sharks = sub
        return total


def main():
    fishing = Fishing()
    print(fishing.play())


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
