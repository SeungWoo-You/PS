import sys


class Floyd:
    def __init__(self) -> None:
        self.N: int
        self.M: int
        self.graph: list[list[int]]
        self.get_info()

    def get_info(self) -> None:
        self.N = int(input())
        self.M = int(input())
        self.graph = [[sys.maxsize] * self.N for _ in range(self.N)]
        for i in range(self.N):
            self.graph[i][i] = 0
        for _ in range(self.M):
            i, j, w = map(int, input().split())
            self.graph[i - 1][j - 1] = min(self.graph[i - 1][j - 1], w)

    def find(self) -> None:
        for mid in range(self.N):
            for i in range(self.N):
                for j in range(self.N):
                    self.graph[i][j] = min(
                        self.graph[i][j], self.graph[i][mid] + self.graph[mid][j])


def main():
    F = Floyd()
    F.find()
    for row in F.graph:
        for x in row:
            print(x if x != sys.maxsize else 0, end=' ')
        print()


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
