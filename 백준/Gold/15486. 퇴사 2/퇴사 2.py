import sys


def main():
    N = int(input())
    income = [0] * (N + 1)
    table = [list(map(int, input().split())) for _ in range(N)]
    total = 0

    for day in range(N):
        T, P = table[day]
        total = max(total, income[day])
        if day + T <= N:
            income[day + T] = max(income[day + T], total + P)
    print(max(income))


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
