import sys


def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        stickers = [list(map(int, input().split())) for _ in range(2)]
        selects = [[0, stickers[0][0]], [0, stickers[1][0]]]

        for i in range(1, n):
            a0 = max(selects[0][-2], selects[1][-2],
                     selects[1][-1]) + stickers[0][i]
            a1 = max(selects[0][-2], selects[1][-2],
                     selects[0][-1]) + stickers[1][i]
            selects[0].append(a0)
            selects[1].append(a1)
        print(max(selects[0][-1], selects[1][-1]))


if __name__ == "__main__":
    input = sys.stdin.readline
    main()
