import sys


def main():
    S = input().strip()
    N = len(S)
    count: set[str] = set()
    for i in range(N):
        for j in range(i, N):
            count.add(S[i:j + 1])
    print(len(count))


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
