import sys


def main():
    N, M = map(int, input().split())
    passwords: dict[str, str] = dict()
    for _ in range(N):
        site, pw = input().strip().split()
        passwords[site] = pw

    for _ in range(M):
        where = input().strip()
        print(passwords[where])


if __name__ == "__main__":
    input = sys.stdin.readline
    main()
