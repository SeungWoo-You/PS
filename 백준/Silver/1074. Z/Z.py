import sys


def main():
    N, r, c = map(int, input().split())
    print(visit_Z(N, r, c))


def visit_Z(N: int, r: int, c: int) -> int:
    if N == 1:
        square = [[0, 1], [2, 3]]
        return square[r][c]
    coord = 2**(N - 1)
    square_size = coord**2
    if r < coord and c < coord:
        start = 0
        res = start + visit_Z(N - 1, r, c)
    elif r < coord and c >= coord:
        start = square_size
        res = start + visit_Z(N - 1, r, c - coord)
    elif r >= coord and c < coord:
        start = square_size * 2
        res = start + visit_Z(N - 1, r - coord, c)
    elif r >= coord and c >= coord:
        start = square_size * 3
        res = start + visit_Z(N - 1, r - coord, c - coord)
    return res


if __name__ == '__main__':
    sys.setrecursionlimit(10**5)
    main()
