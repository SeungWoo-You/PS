from itertools import permutations


def main():
    N, M = map(int, input().split())
    res = []
    tmp = []
    for ls in permutations(range(1, N + 1), M):
        if len(set(ls)) != len(ls):
            continue
        print(*ls)


if __name__ == '__main__':
    main()
