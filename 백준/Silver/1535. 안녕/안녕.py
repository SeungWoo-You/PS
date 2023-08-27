import sys


def main():
    N = int(input())
    health = list(map(int, input().split()))
    happy = list(map(int, input().split()))
    pleasent = [[0] * (N + 1) for _ in range(101)]
    for i in range(1, 101):
        for j in range(1, N + 1):
            h, p = health[j - 1], happy[j - 1]
            if i - h > 0:
                pleasent[i][j] = max(pleasent[i][j - 1],
                                     pleasent[i - h][j - 1] + p)
            else:
                pleasent[i][j] = pleasent[i][j - 1]
    print(pleasent[100][N])


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
