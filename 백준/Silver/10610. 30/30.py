import sys


def main():
    S = list(input().strip())
    if '0' in S:
        if sum(map(int, S)) % 3 == 0:
            N = list(map(int, S))
            N.sort(reverse=True)
            print(*N, sep='')
            exit()
    print(-1)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
