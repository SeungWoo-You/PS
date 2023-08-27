import sys


def main():
    K, N, M = map(int, input().split())
    res = K * N - M
    print(res if res > 0 else 0)


if __name__ == "__main__":
    input = sys.stdin.readline
    main()
