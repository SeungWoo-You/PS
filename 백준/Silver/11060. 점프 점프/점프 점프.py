import sys


def main():
    N = int(input())
    maze = list(map(int, input().split()))
    ans = [sys.maxsize] * N
    ans[0] = 0
    for i, jump in enumerate(maze):
        for j in range(1, jump + 1):
            if i + j < N:
                ans[i + j] = min(ans[i] + 1, ans[i + j])
    print(ans[N - 1] if ans[N - 1] != sys.maxsize else -1)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
