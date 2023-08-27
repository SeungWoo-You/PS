import sys


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        stores = list(map(int, input().split()))
        print((max(stores) - min(stores)) * 2)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
