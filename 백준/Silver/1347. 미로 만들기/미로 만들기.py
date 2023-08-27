import sys
from collections import deque


def main():
    N = int(input())
    S = input().strip()
    maze: deque[deque[str]] = deque()
    maze.append(deque(['.']))
    x, y = 0, 0
    d = (1, 0)
    for cmd in S:
        if cmd == 'R':
            d = (d[1], -d[0])
        elif cmd == 'L':
            d = (-d[1], d[0])
        else:
            x, y = map(sum, zip((x, y), d))
            M, N = len(maze), len(maze[0])
            if x < 0:
                row = '#' * N
                maze.appendleft(deque(row))
                x = 0
            elif x >= M:
                row = '#' * N
                maze.append(deque(row))
                x = M
            if y < 0:
                for row in maze:
                    row.appendleft('#')
                y = 0
            elif y >= N:
                for row in maze:
                    row.append('#')
                y = N
        maze[x][y] = '.'
    for row in maze:
        print(*row, sep='')


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
