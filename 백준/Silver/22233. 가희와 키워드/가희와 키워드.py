import sys


def main():
    N, M = map(int, input().split())
    memo = set(input().strip() for _ in range(N))
    for _ in range(M):
        keyword = input().strip().split(',')
        memo.difference_update(keyword)
        print(len(memo))


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
