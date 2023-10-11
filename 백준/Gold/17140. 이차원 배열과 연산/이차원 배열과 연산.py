import sys
from copy import deepcopy
from collections import Counter


class Array:
    def __init__(self) -> None:
        self.r: int
        self.c: int
        self.k: int
        self.A: list[list[int]]
        self.get_info()

    def get_info(self) -> None:
        self.r, self.c, self.k = map(int, input().split())
        self.r -= 1
        self.c -= 1
        self.A = [list(map(int, input().split())) for _ in range(3)]

    def R(self) -> None:
        A = self.A
        new_A: list[list[int]] = []
        M = 0
        for row in A:
            count = Counter(row)
            if 0 in count:
                count.pop(0)
            S = sorted(count.items(), key=lambda p: (p[1], p[0]))
            new_row: list[int] = []
            for T in S:
                if len(new_row) >= 100:
                    break
                new_row.extend(T)
            M = max(M, len(new_row))
            new_A.append(new_row)
        for row in new_A:
            while len(row) < M:
                row.append(0)
        self.A = new_A
        return

    def C(self) -> None:
        A = self.A
        N, M = len(A), len(A[0])
        new_A: list[list[int]] = []
        for j in range(M):
            count = Counter([A[i][j] for i in range(N)])
            if 0 in count:
                count.pop(0)
            S = sorted(count.items(), key=lambda p: (p[1], p[0]))
            for c, T in enumerate(S):
                if c >= 50:
                    break
                if len(new_A) <= 2 * c:
                    line = [0] * j
                    line.append(T[0])
                    new_A.append(line)
                    line = [0] * j
                    line.append(T[1])
                    new_A.append(line)
                else:
                    new_A[2 * c].append(T[0])
                    new_A[2 * c + 1].append(T[1])
            for row in new_A:
                while len(row) < j + 1:
                    row.append(0)
        self.A = new_A
        return

    def calc(self) -> int:
        try:
            if self.A[self.r][self.c] == self.k:
                return 0
        except:
            pass
        for t in range(1, 101):
            N, M = len(self.A), len(self.A[0])
            if N >= M:
                self.R()
            else:
                self.C()
            try:
                if self.A[self.r][self.c] == self.k:
                    return t
            except:
                pass
        return -1


def main():
    arr = Array()
    print(arr.calc())


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
