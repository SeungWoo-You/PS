import sys


def main():
    dice = list(map(int, input().split()))
    S = set(dice)
    if len(S) == 1:
        price = 10000 + dice[0] * 1000
    elif len(S) == 2:
        price = 1000 + dice[0] * \
            100 if dice[0] in dice[1:] else 1000 + dice[1] * 100
    else:
        price = max(dice) * 100
    print(price)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
