import sys


class DragonCurve:
    def __init__(self) -> None:
        self.x: int
        self.y: int
        self.d: int
        self.g: int
        self.pts: set[tuple[int, int]] = set()
        self.start_pt: tuple[int, int]
        self.end_pt: tuple[int, int]
        self.get_info()

    def get_info(self) -> None:
        self.x, self.y, self.d, self.g = map(int, input().split())
        self.start_pt = (self.x, self.y)
        self.pts.add(self.start_pt)
        self.end_pt = tuple(map(sum, zip(self.start_pt, self.direction())))
        self.pts.add(self.end_pt)

    def direction(self) -> tuple[int, int]:
        if self.d == 0:
            dx, dy = (1, 0)
        elif self.d == 1:
            dx, dy = (0, -1)
        elif self.d == 2:
            dx, dy = (-1, 0)
        elif self.d == 3:
            dx, dy = (0, 1)
        return (dx, dy)

    def rotation(self, tx: int, ty: int) -> tuple[int, int]:
        ex, ey = self.end_pt
        x = ex + ey - ty
        y = ey - ex + tx
        return (x, y)

    def generate(self) -> None:
        for _ in range(self.g):
            pts: set[tuple[int, int]] = set()
            for p in self.pts:
                rotated = self.rotation(*p)
                pts.add(rotated)
                if p == self.start_pt:
                    end_pt = rotated
            try:
                self.end_pt = end_pt
            except:
                pass
            self.pts = self.pts | pts


def count(pts: set[tuple[int, int]]) -> int:
    ls = sorted(pts)
    res = 0
    i = 0
    checked_x: set[int] = set()
    prev_y: set[int] = set()
    now_y: set[int] = set()
    for x, y in ls:
        if x != i:
            i = x
            prev_y = now_y.copy()
            now_y = {y}
        else:
            if x - 1 in checked_x and y - 1 in prev_y:
                if y in prev_y:
                    if y - 1 in now_y:
                        res += 1
        checked_x.add(x)
        now_y.add(y)
    return res


def main():
    N = int(input())
    pts: set[int, int] = set()
    for _ in range(N):
        dragon = DragonCurve()
        dragon.generate()
        pts = pts | dragon.pts
    print(count(pts))


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
