import sys


def main():
    N, K = map(int, input().split())
    meas: set[int] = set()
    for x in range(1, N + 1):
        quot, rem = divmod(N, x)
        if rem == 0:
            meas.add(x)
    R = sorted(meas)
    print(R[K - 1] if len(R) >= K else 0)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
