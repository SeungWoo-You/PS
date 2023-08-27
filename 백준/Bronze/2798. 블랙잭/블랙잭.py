from itertools import combinations


def main():
    N, M = map(int, input().split())
    cards = map(int, input().split())
    res = -1
    for c in combinations(cards, 3):
        temp = sum(c)
        if temp > M:
            continue
        elif temp == M:
            res = temp
            break
        elif temp > res:
            res = temp
    print(res)


if __name__ == '__main__':
    main()
