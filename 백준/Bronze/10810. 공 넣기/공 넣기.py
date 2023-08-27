import sys


def main():
    N, M = map(int, input().split())
    basket = {v: 0 for v in range(1, N + 1)}
    for _ in range(M):
        s, e, v = map(int, input().split())
        for i in range(s, e + 1):
            basket[i] = v
    print(*basket.values())


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
