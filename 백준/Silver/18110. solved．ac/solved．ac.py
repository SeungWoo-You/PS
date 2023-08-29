import sys


def main():
    N = int(input())
    if N == 0:
        print(0)
        return
    rm = round(0.15 * N)
    rate = [int(input()) for _ in range(N)]
    rate.sort()
    calc = rate[rm:-rm] if rm != 0 else rate
    print(round(sum(calc) / len(calc)))


def round(v: float) -> int:
    return int(v) + 1 if v - int(v) >= 0.5 else int(v)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
