import sys
from collections import deque


def main():
    N = int(input())
    img = [list(input().strip()) for _ in range(N)]
    week: list[list[str]] = []
    for row in img:
        line = []
        for c in row:
            line.append(c if c != 'G' else 'R')
        week.append(line)
    print(find_area(img, N), find_area(week, N))


def find_area(graph: list[list[str]], N: int) -> int:
    visited = [[False] * N for _ in range(N)]
    group = deque([(0, 0, graph[0][0])])
    visited[0][0] = True
    sect = 1

    Dx = [-1, 1, 0, 0]
    Dy = [0, 0, -1, 1]
    remains: set[tuple[int, int, str]] = set()

    while True:
        if not group:
            if remains:
                R = (0, 0, graph[0][0])
                while visited[R[0]][R[1]] == True:
                    try:
                        R = remains.pop()
                    except:
                        break
                if visited[R[0]][R[1]] == True:
                    break
                group.append(R)
                visited[R[0]][R[1]] = True
                sect += 1
            else:
                break
        x, y, c = group.popleft()
        for d in zip(Dx, Dy):
            dx, dy = d
            i, j = x + dx, y + dy
            if 0 <= i < N and 0 <= j < N and visited[i][j] == False:
                if graph[i][j] == c:
                    visited[i][j] = True
                    group.append((i, j, graph[i][j]))
                elif graph[i][j] != c and (i, j, graph[i][j]) not in remains:
                    remains.add((i, j, graph[i][j]))
    return sect


def isin(graph: list[list], target) -> tuple[int, int]:
    for i, row in enumerate(graph):
        for j, x in enumerate(row):
            if x == target:
                return (i, j)
    return (-1, -1)


if __name__ == "__main__":
    input = sys.stdin.readline
    main()
