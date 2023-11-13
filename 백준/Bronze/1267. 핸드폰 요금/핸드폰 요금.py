import sys


def main():
    N = int(input())
    C = list(map(int, input().split()))
    Y, M = 0, 0
    for cost in C:
        quot, rem = divmod(cost, 30)
        quot += 1
        Y += quot * 10
        quot, rem = divmod(cost, 60)
        quot += 1
        M += quot * 15
    if Y == M:
        print(f'Y M {Y}')
    elif Y < M:
        print(f'Y {Y}')
    else:
        print(f'M {M}')


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
