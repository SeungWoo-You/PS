import sys
import heapq


class Building:
    def __init__(self) -> None:
        self.L: int
        self.R: int
        self.C: int
        self.rooms: list[list[str]] = []
        self.get_info()

    def get_info(self) -> None:
        self.L, self.R, self.C = map(int, input().split())
        for _ in range(self.L):
            self.rooms.append([input().strip() for _ in range(self.R)])
            input()

    def escape(self) -> int:
        dists = [
            [[sys.maxsize] * self.C for _ in range(self.R)] for _ in range(self.L)]
        for i, F in enumerate(self.rooms):
            for j, row in enumerate(F):
                for k, c in enumerate(row):
                    if c == 'S':
                        src = (i, j, k)
                        dists[i][j][k] = 0
                        break
        H: list[tuple[int, int, int, int]] = [(0, *src)]
        Dx = [0, 0, 0, 0, -1, 1]
        Dy = [0, 0, -1, 1, 0, 0]
        Dz = [-1, 1, 0, 0, 0, 0]
        while H:
            d, i, j, k = heapq.heappop(H)
            if self.rooms[i][j][k] == 'E':
                return d
            for dz, dx, dy in zip(Dz, Dx, Dy):
                z, x, y = i + dz, j + dx, k + dy
                if 0 <= z < self.L and 0 <= x < self.R and 0 <= y < self.C and self.rooms[z][x][y] != '#':
                    if d + 1 < dists[z][x][y]:
                        dists[z][x][y] = d + 1
                        heapq.heappush(H, (d + 1, z, x, y))
        return -1


def main():
    while True:
        B = Building()
        if not B.rooms:
            break
        t = B.escape()
        print(f'Escaped in {t} minute(s).' if t != -1 else 'Trapped!')


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
