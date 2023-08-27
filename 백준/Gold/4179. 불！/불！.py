import sys
from collections import deque


def main():
    global R, C
    R, C = map(int, input().split())
    maze = [list(input().rstrip('\n')) for _ in range(R)]
    print(find_route(maze))


def find_route(maze: list[list[str]]) -> int:
    res: list[list[list[int]]] = []
    JH: deque[list[int]] = deque([])
    fire: deque[list[int]] = deque([])
    for i, row in enumerate(maze):
        line: list[list[int]] = []
        for j, x in enumerate(row):
            if x == '#':
                line.append([-1, -1])
            elif x == 'F':
                fire.append([i, j])
                line.append([0, 0])
            elif x == 'J':
                JH.append([i, j])
                line.append([0, -1])
            else:
                line.append([0, -1])
        res.append(line)

    Dx = [1, -1, 0, 0]
    Dy = [0, 0, 1, -1]
    while fire:
        i, j = fire.popleft()
        dist = res[i][j][1]
        for dx, dy in zip(Dx, Dy):
            x = i + dx
            y = j + dy
            if 0 <= x < R and 0 <= y < C and res[x][y] == [0, -1]:
                res[x][y][1] = dist + 1
                fire.append([x, y])

    while JH:
        i, j = JH.popleft()
        dist = res[i][j][0]
        if i in (0, R - 1) or j in (0, C - 1):
            return dist + 1
        for dx, dy in zip(Dx, Dy):
            x = i + dx
            y = j + dy
            if 0 <= x < R and 0 <= y < C and res[x][y][0] == 0 and (res[x][y][1] == -1 or res[x][y][1] > dist + 1):
                res[x][y][0] = dist + 1
                JH.append([x, y])
    return 'IMPOSSIBLE'


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
