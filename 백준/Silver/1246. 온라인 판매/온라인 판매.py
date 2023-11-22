import sys


def main():
    N, M = map(int, input().split())
    P = [int(input()) for _ in range(M)]
    P.sort(reverse=True)
    income = 0
    price = -1
    for i in range(min(M, N)):
        cost = P[i]
        if income <= cost * (i + 1):
            income = cost * (i + 1)
            price = cost
    print(price, income)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
