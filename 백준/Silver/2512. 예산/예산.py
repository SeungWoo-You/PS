import sys


def main():
    N = int(input())
    gps = list(map(int, input().split()))
    gps.sort()
    budget = int(input())
    print(set_budget(gps, budget))


def set_budget(gps: list[int], bud: int) -> int:
    start = 0
    end = gps[-1]
    while start <= end:
        mid = (start + end) // 2
        S = calc_set(gps, mid)
        if S > bud:
            end = mid - 1
        else:
            start = mid + 1
    mid = (start + end) // 2
    return mid


def calc_set(gps: list[int], bud: int) -> int:
    total = 0
    for x in gps:
        if x > bud:
            total += bud
        else:
            total += x
    return total


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
