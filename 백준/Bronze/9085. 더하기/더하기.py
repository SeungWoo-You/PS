import sys


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        print(sum(map(int, input().split())))


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
