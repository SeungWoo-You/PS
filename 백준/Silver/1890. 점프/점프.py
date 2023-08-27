import sys


def main():
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    count = [[0] * N for _ in range(N)]
    count[0][0] = 1
    for i, row in enumerate(board):
        for j, jump in enumerate(row):
            if jump == 0:
                continue
            x = i + jump
            if 0 <= x < N:
                count[x][j] += count[i][j]
            y = j + jump
            if 0 <= y < N:
                count[i][y] += count[i][j]
    print(count[-1][-1])


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
