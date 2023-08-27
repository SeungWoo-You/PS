import sys


def main():
    H, W, N, M = map(int, input().split())
    q1, r1 = divmod(H, N + 1)
    q2, r2 = divmod(W, M + 1)
    if r1 > 0:
        q1 += 1
    if r2 > 0:
        q2 += 1
    print(q1 * q2)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
