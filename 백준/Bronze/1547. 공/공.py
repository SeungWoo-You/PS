import sys


def main():
    M = int(input())
    ball = 1
    for _ in range(M):
        X, Y = map(int, input().split())
        if X == ball:
            ball = Y
        elif Y == ball:
            ball = X
    print(ball)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
