from itertools import combinations


def main():
    while True:
        ls = list(map(int, input().split()))
        if ls[0] == 0:
            break
        k, S = ls[0], ls[1:]
        for c in combinations(S, 6):
            print(*c)
        print()


if __name__ == '__main__':
    main()
