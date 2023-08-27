from itertools import combinations


def main():
    ls = [int(input()) for _ in range(9)]
    total = sum(ls)

    for x, y in combinations(ls, 2):
        if total - (x + y) == 100:
            break
    ls.remove(x)
    ls.remove(y)
    ls.sort()
    print(*ls, sep='\n')


if __name__ == '__main__':
    main()
