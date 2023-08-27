import sys


def main():
    N = int(input())
    ropes = [int(input()) for _ in range(N)]
    ropes.sort(key=lambda x: -x)

    W = 0
    for i, r in enumerate(ropes, start=1):
        W = max(W, i * r)
    print(W)


if __name__ == "__main__":
    input = sys.stdin.readline
    main()
