import sys


def main():
    A = input().strip()
    N = int(input())
    count = 0
    for _ in range(N):
        S = 2 * input().strip()
        if A in S:
            count += 1
    print(count)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
