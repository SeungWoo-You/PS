import sys


def main():
    N, L = map(int, input().split())
    holes = [tuple(map(int, input().split())) for _ in range(N)]
    holes.sort(key=lambda p: (p[0], -p[1]))

    end = 0
    count = 0
    for x, y in holes:
        if y + 1 > end:
            end = end if x < end else x
            board, rem = divmod(y - end, L)
            plus = 1 if rem > 0 else 0
            board = board + plus
            end += board * L
            count += board
    print(count)


if __name__ == "__main__":
    input = sys.stdin.readline
    main()
