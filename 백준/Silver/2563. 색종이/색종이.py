import sys


def main():
    N = int(input())
    background = [[0] * 100 for _ in range(100)]
    for _ in range(N):
        dy, dx = map(int, input().split())
        for x in range(90 - dx, 100 - dx):
            for y in range(dy, 10 + dy):
                background[x][y] = 1
    area = sum(map(sum, background))
    print(area)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
