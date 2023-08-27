import sys
from collections import defaultdict, deque


def main():
    N, M = map(int, input().split())
    lights: dict[int, defaultdict[int, set[tuple[int, int]]]] = {
        v: defaultdict(set) for v in range(1, N + 1)}
    for _ in range(M):
        x, y, a, b = map(int, input().split())
        lights[x][y].add((a, b))
    print(on_light(lights, N))


def on_light(lights: dict[int, defaultdict[int, set[tuple[int, int]]]], N: int) -> int:
    rooms = set([(1, 1)])
    checked = set([(1, 1)])
    accessible: deque[tuple[int, int]] = deque([(1, 1)])
    Dx = [0, 0, -1, 1]
    Dy = [-1, 1, 0, 0]

    while accessible:
        x, y = accessible.popleft()
        checked.add((x, y))
        for a, b in lights[x][y] - rooms:
            rooms.add((a, b))
            for dx, dy in zip(Dx, Dy):
                i, j = a + dx, b + dy
                if 0 < i <= N and 0 < j <= N and (i, j) in checked:
                    accessible.append((a, b))
                    break
        for dx, dy in zip(Dx, Dy):
            i, j = x + dx, y + dy
            if 0 < i <= N and 0 < j <= N and (i, j) not in checked and (i, j) in rooms:
                accessible.append((i, j))
    return len(rooms)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
