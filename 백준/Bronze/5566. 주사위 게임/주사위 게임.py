import sys


def main():
    N, M = map(int, input().split())
    board = [int(input()) for _ in range(N)]
    dice = [int(input()) for _ in range(M)]
    pos = 1
    for count, d in enumerate(dice, start=1):
        pos += d
        if pos >= N:
            break
        pos += board[pos - 1]
        if pos >= N:
            break
    print(count)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
