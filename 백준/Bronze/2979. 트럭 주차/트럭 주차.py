import sys


def main():
    cost = [0] + list(map(int, input().split()))
    parking = [list(map(int, input().split())) for _ in range(3)]
    parking.sort()
    activated = 0
    total = 0
    for i in range(1, 100):
        for s, e in parking:
            if i == s:
                activated += 1
            elif i == e:
                activated -= 1
        total += cost[activated] * activated
    print(total)


if __name__ == "__main__":
    input = sys.stdin.readline
    main()
