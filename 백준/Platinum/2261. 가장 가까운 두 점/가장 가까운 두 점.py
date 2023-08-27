import sys
from itertools import combinations


def main():
    n = int(input())
    pts = [tuple(map(int, input().split())) for _ in range(n)]
    pts.sort()
    print(find_closest(pts))


def dist(p1: tuple[int, int], p2: tuple[int, int]) -> int:
    dx = abs(p1[0] - p2[0])
    dy = abs(p1[1] - p2[1])
    return dx**2 + dy**2


def find_closest(pts: list[tuple[int, int]]) -> int:
    N = len(pts)
    if N <= 3:
        res = [dist(p1, p2) for p1, p2 in combinations(pts, 2)]
        return min(res)

    m = N // 2
    left = find_closest(pts[:m])
    right = find_closest(pts[m:])
    res = min(left, right)

    cx = pts[m][0]
    between = [p for p in pts if abs(p[0] - cx)**2 <= res]
    between.sort(key=lambda p: p[1])
    M = len(between)

    for i in range(M):
        for j in range(i + 1, M):
            if abs(between[i][1] - between[j][1]) < res:
                res = min(res, dist(between[i], between[j]))
            else:
                break
    return res


if __name__ == "__main__":
    input = sys.stdin.readline
    main()
