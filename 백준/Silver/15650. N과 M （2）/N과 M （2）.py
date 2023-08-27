from itertools import combinations


def main():
    N, M = map(int, input().split())
    for ls in combinations(range(1, N + 1), M):
        print(*ls)


if __name__ == '__main__':
    main()
