import sys
from copy import deepcopy


class combinations:
    def __init__(self, ls: list, r: int) -> None:
        self.ls = ls
        self.r = r
        self.result: list = []

    def nCr(self, n: int = 0, temp: list = []) -> None:
        if n == len(self.ls):
            if len(temp) == self.r:
                T = deepcopy(temp)
                self.result.append(T)
            return
        temp.append(self.ls[n])
        self.nCr(n + 1, temp)
        temp.pop()
        self.nCr(n + 1, temp)
        return


class Election:
    def __init__(self) -> None:
        self.N: int
        self.population: list[int] = [0]
        self.regions: list[list[int]]
        self.total: int
        self.get_info()

    def get_info(self) -> None:
        self.N = int(input())
        self.population.extend(map(int, input().split()))
        self.regions = [[]]
        for _ in range(self.N):
            info = list(map(int, input().split()))
            self.regions.append(info[1:])
        self.total = sum(self.population)

    def divide(self, R: list[int]) -> tuple[bool, tuple[int, int]]:
        S: list[int] = [R[0]]
        V1: set[int] = set()
        while S:
            i = S.pop()
            if i in V1:
                continue
            V1.add(i)
            for x in self.regions[i]:
                if x in R:
                    S.append(x)
        T = set(range(1, self.N + 1))
        S = [(T - V1).pop()]
        V2: set[int] = set()

        while S:
            i = S.pop()
            if i in V2:
                continue
            V2.add(i)
            for x in self.regions[i]:
                if x not in V1:
                    S.append(x)
        possible = True if V1 | V2 - {0} == T else False
        c1 = sum([self.population[i] for i in V1]) if possible else -1
        c2 = self.total - c1 if possible else -1
        return (possible, (c1, c2))


def main():
    elect = Election()
    pops = list(range(1, elect.N + 1))
    diff = sys.maxsize
    for r in range(1, elect.N // 2 + 1):
        comb = combinations(pops, r)
        comb.nCr()
        for T in comb.result:
            T: list[int]
            possible, C = elect.divide(T)
            if possible:
                diff = min(diff, abs(C[0] - C[1]))
    print(diff if diff != sys.maxsize else -1)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
