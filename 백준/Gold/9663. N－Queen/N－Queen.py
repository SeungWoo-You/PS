import sys
sys.setrecursionlimit(10**4)


class Queen:
    def __init__(self, N: int) -> None:
        self.N = N
        self.cols: set[int] = set()
        self.diags_rightdown: set[int] = set()
        self.diags_rightup: set[int] = set()

    def count(self, row_idx: int = 0) -> int:
        if row_idx == self.N:
            return 1
        ans = 0
        for j in range(self.N):
            d_down = row_idx - j
            d_up = row_idx + j
            if j in self.cols or d_down in self.diags_rightdown or d_up in self.diags_rightup:
                continue
            self.cols.add(j)
            self.diags_rightdown.add(d_down)
            self.diags_rightup.add(d_up)
            ans += self.count(row_idx + 1)
            self.cols.discard(j)
            self.diags_rightdown.discard(d_down)
            self.diags_rightup.discard(d_up)
        return ans


def main():
    N = int(input())
    Q = Queen(N)
    print(Q.count())


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
