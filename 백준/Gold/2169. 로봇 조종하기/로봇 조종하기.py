import sys
from collections import deque


def main():
    global N, M
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    print(find_best(grid))


def find_best(grid: list[list[int]]) -> int:
    res = []

    for i in range(N):
        lr = grid[i][0] if i == 0 else res[i - 1][0] + grid[i][0]
        if i == 0 or i == N - 1:
            rl = -sys.maxsize
        else:
            rl = res[i - 1][M - 1] + grid[i][M - 1]
        line_LR = [lr]
        line_RL = deque([rl])
        for j in range(1, M):
            if i == 0:
                line_LR.append(line_LR[-1] + grid[i][j])
                line_RL.appendleft(-sys.maxsize)
            elif i == N - 1:
                line_LR.append(
                    max(line_LR[-1], res[i - 1][j]) + grid[i][j])
                line_RL.appendleft(-sys.maxsize)
            else:
                line_LR.append(
                    max(line_LR[-1], res[i - 1][j]) + grid[i][j])
                line_RL.appendleft(
                    max(line_RL[0], res[i - 1][M - 1 - j]) + grid[i][M - 1 - j])
        temp = [max(x) for x in zip(line_LR, line_RL)]
        res.append(temp)
    return res[-1][-1]


if __name__ == "__main__":
    input = sys.stdin.readline
    main()
