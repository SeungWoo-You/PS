import sys


def main():
    N = 10000
    S = set(range(1, N + 1))
    for i in range(1, N + 1):
        X = i + sum(map(int, list(str(i))))
        S.discard(X)
    print(*sorted(S), sep='\n')


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
