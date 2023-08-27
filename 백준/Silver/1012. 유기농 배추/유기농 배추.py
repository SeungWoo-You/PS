import sys


def main():
    T = int(input())
    for _ in range(T):
        M, N, K = map(int, input().split(" "))
        cabbages = [list(map(int, input().split(" "))) for _ in range(K)]
        grid = [[0] * (N + 1) for _ in range(M + 1)]

        for x, y in cabbages:
            grid[x][y] = 1

        bugs = 0
        for x in range(M):
            for y in range(N):
                if grid[x][y] == 1:
                    search(grid, x, y)
                    bugs += 1
        print(bugs)


def search(grid: list[list[int]], x: int, y: int) -> None:
    grid[x][y] = 0
    if grid[x][y + 1] == 1:
        search(grid, x, y + 1)
    if y >= 1 and grid[x][y - 1] == 1:
        search(grid, x, y - 1)
    if grid[x + 1][y] == 1:
        search(grid, x + 1, y)
    if x >= 1 and grid[x - 1][y] == 1:
        search(grid, x - 1, y)


if __name__ == '__main__':
    sys.setrecursionlimit(10**6)
    main()
