import sys

class Solve:
    def __init__(self, alp: int, cop: int, problems: list) -> None:
        self.alp: int = alp
        self.cop: int = cop
        self.problems: list[list[int]] = problems
        self.A: int = max(problems, key=lambda p: p[0])[0]
        self.C: int = max(problems, key=lambda p: p[1])[1]
        
    def time(self) -> int:
        A, C = self.A, self.C
        a, c = min(self.alp, A), min(self.cop, C)
        T: list[list[int]] = [[sys.maxsize] * (C + 1) for _ in range(A + 1)]
        T[a][c] = 0
        for i in range(a, A + 1):
            for j in range(c, C + 1):
                if i < A:
                    T[i + 1][j] = min(T[i + 1][j], T[i][j] + 1)
                if j < C:
                    T[i][j + 1] = min(T[i][j + 1], T[i][j] + 1)
                for P in self.problems:
                    if i >= P[0] and j >= P[1]:
                        dx, dy, t = P[2], P[3], P[4]
                        x, y = min(i + dx, A), min(j + dy, C)
                        T[x][y] = min(T[x][y], T[i][j] + t)
        return T[A][C]
        

def solution(alp, cop, problems):
    solve = Solve(alp, cop, problems)
    return solve.time()