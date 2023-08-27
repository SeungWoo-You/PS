import sys


def main():
    N = int(input())
    schedule = [list(map(int, input().split())) for _ in range(N)]
    schedule.sort(key=lambda p: (p[1], p[0]))
    res = 0
    ing = -1
    for p in schedule:
        start, end = p
        if start >= ing:
            res += 1
            ing = end
    print(res)


if __name__ == "__main__":
    input = sys.stdin.readline
    main()
