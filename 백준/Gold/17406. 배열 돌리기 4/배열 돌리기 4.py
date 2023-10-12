import sys
from copy import deepcopy
from collections import deque


class permutations:
    def __init__(self, ls: list, r: int) -> None:
        self.ls = ls
        self.n = len(ls)
        self.r = r
        self.answer = []

    def nPr(self, contain: list[list[int]], visited: set[int]) -> None:
        if len(visited) == self.r:
            self.answer.append(deepcopy(contain))
            return
        for j in range(self.n):
            if j in visited:
                continue
            visited.add(j)
            contain.append(self.ls[j])
            self.nPr(contain, visited)
            visited.discard(j)
            contain.pop()
        return


class Array:
    def __init__(self) -> None:
        self.N: int
        self.M: int
        self.K: int
        self.A: list[list[int]]
        self.info: list[list[int]]
        self.get_info()

    def get_info(self) -> None:
        self.N, self.M, self.K = map(int, input().split())
        self.A = [list(map(int, input().split())) for _ in range(self.N)]
        self.info = []
        for _ in range(self.K):
            r, c, s = map(int, input().split())
            self.info.append([r - 1, c - 1, s])

    def rotate(self, A: list[list[int]], info: list[int]) -> list[list[int]]:
        i, j, S = info
        for ds in range(S, 0, -1):
            si, sj = i - ds, j - ds
            ei, ej = i + ds, j + ds
            Q: deque[int] = deque()
            Q.extend([A[si][k] for k in range(sj + 1, ej + 1)])
            Q.extend([A[k][ej] for k in range(si + 1, ei + 1)])
            Q.extend([A[ei][k] for k in range(ej - 1, sj - 1, -1)])
            Q.extend([A[k][sj] for k in range(ei - 1, si - 1, -1)])
            Q.appendleft(Q.pop())
            for k in range(sj + 1, ej + 1):
                A[si][k] = Q.popleft()
            for k in range(si + 1, ei + 1):
                A[k][ej] = Q.popleft()
            for k in range(ej - 1, sj - 1, -1):
                A[ei][k] = Q.popleft()
            for k in range(ei - 1, si - 1, -1):
                A[k][sj] = Q.popleft()
        return A

    def find_min(self) -> int:
        P = permutations(self.info, self.K)
        P.nPr([], set())
        value = sys.maxsize
        for order in P.answer:
            order: list[list[int]]
            A = deepcopy(self.A)
            for info in order:
                A = self.rotate(A, info)
            value = min(value, min([sum(row) for row in A]))
        return value


def main():
    arr = Array()
    print(arr.find_min())


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
