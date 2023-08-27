import sys
from itertools import product


def main():
    N = int(input())
    paper = [list(map(int, input().split())) for _ in range(N)]
    check, color = is_counting(paper)
    if check == True:
        ans = (0, 1) if color == 1 else (1, 0)
    else:
        ans = count_paper(paper, N)
    print(*ans, sep='\n')


def count_paper(paper: list[list[int]], N: int) -> tuple[int, int]:
    if N == 1:
        if paper[0][0] == 1:
            return (0, 1)
        return (1, 0)
    half = N // 2
    white = 0
    blue = 0

    X = [(0, half), (half, None)]
    Y = [(0, half), (half, None)]

    for tx, ty in product(X, Y):
        x1, x2 = tx
        y1, y2 = ty
        sliced_paper = slicing(paper, x1, y1, x2, y2)
        check, color = is_counting(sliced_paper)
        if check == True:
            if color == 1:
                blue += 1
            else:
                white += 1
        else:
            w, b = count_paper(sliced_paper, half)
            white += w
            blue += b
    return (white, blue)


def is_counting(paper: list[list[int]]) -> tuple[bool, int]:
    S: set[int] = set()
    for row in paper:
        S = S.union(set(row))
    if S == {1}:
        return (True, 1)
    elif S == {0}:
        return (True, 0)
    return (False, -1)


def slicing(paper: list[list[int]], x1: int, y1: int, x2: int | None = None, y2: int | None = None) -> list[list[int]]:
    res: list[list[int]] = []
    temp = paper[x1:x2] if x2 != None else paper[x1:]
    for row in temp:
        R = row[y1:y2] if y2 != None else row[y1:]
        res.append(R)
    return res


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
