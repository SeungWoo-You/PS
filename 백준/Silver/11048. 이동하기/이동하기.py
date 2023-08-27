import sys


def main():
    N, M = map(int, input().split())
    maze = [list(map(int, input().split())) for _ in range(N)]
    count = [[0] * (M + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            candy = maze[i - 1][j - 1]
            count[i][j] = max(count[i][j], count[i][j - 1],
                              count[i - 1][j], count[i - 1][j - 1]) + candy
    print(count[N][M])


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
