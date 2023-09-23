import sys
from itertools import combinations


class Team:
    def __init__(self) -> None:
        self.N: int
        self.stat: list[list[int]]
        self.get_info()

    def get_info(self) -> None:
        self.N = int(input())
        self.stat = [list(map(int, input().split())) for _ in range(self.N)]

    def divide(self) -> int:
        total = set(range(self.N))
        m = sys.maxsize
        for T in combinations(range(self.N), self.N // 2):
            opponent = total - set(T)
            s1 = sum(self.stat[i][j] + self.stat[j][i]
                     for i, j in combinations(T, 2))
            s2 = sum(self.stat[i][j] + self.stat[j][i]
                     for i, j in combinations(opponent, 2))
            m = min(m, abs(s1 - s2))
        return m


def main():
    team = Team()
    print(team.divide())


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
