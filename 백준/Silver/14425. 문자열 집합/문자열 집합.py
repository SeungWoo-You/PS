import sys


def main():
    N, M = map(int, input().split())
    S = {input().strip() for _ in range(N)}
    count = 0
    for _ in range(M):
        C = input().strip()
        if C in S:
            count += 1
    print(count)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
