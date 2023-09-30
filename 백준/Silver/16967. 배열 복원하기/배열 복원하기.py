import sys


def main():
    H, W, X, Y = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(H + X)]
    A = [[0] * W for _ in range(H)]
    for i in range(H + X):
        for j in range(W + Y):
            if B[i][j] == 0:
                continue
            if 0 <= i < X and 0 <= j < W:
                A[i][j] = B[i][j]
            if X <= i < H:
                if 0 <= j < Y:
                    A[i][j] = B[i][j]
                elif Y <= j < W:
                    A[i][j] = B[i][j] - A[i - X][j - Y]
            if H <= i < H + X and Y <= j < W + Y:
                A[i - X][j - Y] = B[i][j]
    for row in A:
        print(*row)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
