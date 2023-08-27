import sys


def main():
    N, K = map(int, input().split())
    items = [tuple(map(int, input().split())) for _ in range(N)]
    sack = [[0] * (K + 1) for _ in range(N + 1)]
    for k in range(1, K + 1):
        for j in range(1, N + 1):
            w, v = items[j - 1]
            if k - w < 0:
                sack[j][k] = sack[j - 1][k]
            else:
                sack[j][k] = max(sack[j - 1][k], sack[j - 1][k - w] + v)
    print(sack[N][K])


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
