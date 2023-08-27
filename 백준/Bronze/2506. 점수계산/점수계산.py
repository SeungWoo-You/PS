import sys


def main():
    N = int(input())
    scores = list(map(int, input().split()))
    total = 0
    bonus = 0
    for x in scores:
        if x == 1:
            total += bonus + x
            bonus += 1
        elif x == 0:
            bonus = 0
    print(total)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
