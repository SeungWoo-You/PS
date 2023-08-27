import sys
import math


def main():
    N = int(input())
    points = [list(map(int, input().split())) + [i] for i in range(1, N + 1)]
    pts = sorted(points)

    l = -1
    res = [0, 0]
    for i in range(1, N):
        r = abs((pts[i][1] - pts[i - 1][1]) / (pts[i][0] - pts[i - 1][0]))
        if r > l:
            res = sorted([pts[i - 1][2], pts[i][2]])
            l = r

    A = res[0]
    for i in range(A):
        r = abs((points[A][1] - points[i][1]) /
                (points[A][0] - points[i][0]))
        if math.isclose(r, l) == True:
            res[0] = points[i][2]
            break

    A, B = res
    for i in range(A, N):
        if i > B:
            break
        r = abs((points[i][1] - points[A - 1][1]) /
                (points[i][0] - points[A - 1][0]))
        if math.isclose(r, l) == True:
            res[1] = points[i][2]
            break
    print(*res)


if __name__ == "__main__":
    input = sys.stdin.readline
    main()
