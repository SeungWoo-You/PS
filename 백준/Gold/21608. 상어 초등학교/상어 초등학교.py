import sys


class School:
    def __init__(self) -> None:
        self.N: int
        self.pref: list[list[int | set[int]]] = []
        self.empty: set[tuple[int, int]] = set()
        self.board: list[list[int]]
        self.get_info()

    def get_info(self) -> None:
        self.N = int(input())
        for _ in range(self.N**2):
            info = list(map(int, input().split()))
            self.pref.append([info[0], set(info[1:])])
        for i in range(self.N):
            for j in range(self.N):
                self.empty.add((i, j))
        self.board: list[list[int]] = [[0] * self.N for _ in range(self.N)]

    def place(self) -> dict[int, int]:
        Dx = [0, 0, -1, 1]
        Dy = [-1, 1, 0, 0]
        pos: dict[int, int] = dict()
        for q, (std, P) in enumerate(self.pref):
            count: dict[tuple[int, int], tuple[int, int]] = dict()
            std: int
            P: set[int]
            for i, j in self.empty:
                temp = 0
                em = 0
                for dx, dy in zip(Dx, Dy):
                    x, y = i + dx, j + dy
                    if 0 <= x < self.N and 0 <= y < self.N:
                        if self.board[x][y] in P:
                            temp += 1
                        elif self.board[x][y] == 0:
                            em += 1
                count[(i, j)] = (temp, em)
            possible = sorted(
                count.items(), key=lambda p: (-p[1][0], -p[1][1], p[0][0], p[0][1]))
            (pi, pj), _ = possible[0]
            self.board[pi][pj] = std
            self.empty.discard((pi, pj))
            pos[std] = q
        return pos

    def calc_score(self, pos: dict[int, int]) -> int:
        Dx = [0, 0, -1, 1]
        Dy = [-1, 1, 0, 0]
        total = 0
        for i in range(self.N):
            for j in range(self.N):
                count = 0
                std = pos[self.board[i][j]]
                for dx, dy in zip(Dx, Dy):
                    x, y = i + dx, j + dy
                    if 0 <= x < self.N and 0 <= y < self.N and self.board[x][y] in self.pref[std][1]:
                        count += 1
                total += 10**(count - 1) if count >= 1 else 0
        return total


def main():
    school = School()
    pos = school.place()
    print(school.calc_score(pos))


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
