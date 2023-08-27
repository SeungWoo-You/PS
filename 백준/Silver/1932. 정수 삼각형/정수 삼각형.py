import sys


def main():
    n = int(input())
    R = [[0] * n for _ in range(n)]
    items = list(map(int, input().split()))
    R[0][0] = items[0]

    for i in range(1, n):
        items = list(map(int, input().split()))
        prev = i - 1
        for j, x in enumerate(items):
            if j == 0:
                R[i][j] = max(R[i][j], R[prev][j] + x)
            elif j == i + 1:
                R[i][j] = max(R[i][j], R[prev][j - 1] + x)
            else:
                R[i][j] = max(R[i][j], R[prev][j] + x, R[prev][j - 1] + x)
    print(max(R[-1]))


if __name__ == "__main__":
    input = sys.stdin.readline
    main()
