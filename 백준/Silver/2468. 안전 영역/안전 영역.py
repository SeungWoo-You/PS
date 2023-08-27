import sys


def main():
    N = int(input())
    zone = [list(map(int, input().split())) for _ in range(N)]
    count = 0
    for rain in range(101):
        count = max(count, count_safe(N, *mk_grid(N, zone, rain)))
    print(count)


def count_safe(N: int, zone: list[list[int]], safe: set[int]) -> int:
    count = 0
    if not safe:
        return count
    stack = [safe.pop()]
    Dx = [0, 0, -1, 1]
    Dy = [-1, 1, 0, 0]
    while stack:
        i, j = stack.pop()
        for dx, dy in zip(Dx, Dy):
            x, y = i + dx, j + dy
            if 0 <= x < N and 0 <= y < N and zone[x][y] != -1 and (x, y) in safe:
                stack.append((x, y))
                safe.remove((x, y))
        if not stack:
            count += 1
            if not safe:
                return count
            stack.append(safe.pop())


def mk_grid(N: int, zone: list[list[int]], rain: int) -> tuple[list[list[int]], set[int]]:
    grid = [[0] * N for _ in range(N)]
    safe: set[int] = set()
    for i, row in enumerate(zone):
        for j, x in enumerate(row):
            if x <= rain:
                grid[i][j] = -1
            else:
                grid[i][j] = x
                safe.add((i, j))
    return grid, safe


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
