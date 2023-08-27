import sys


def main():
    n = int(input())
    res = [100, 100]
    for _ in range(n):
        x, y = map(int, input().split())
        if x > y:
            res[1] -= x
        elif x < y:
            res[0] -= y
    print(*res, sep='\n')


if __name__ == "__main__":
    input = sys.stdin.readline
    main()
