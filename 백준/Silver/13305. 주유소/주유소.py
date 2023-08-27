import sys


def main():
    N = int(input())
    roads = list(map(int, input().split()))
    cities = list(map(int, input().split()))

    prev = sys.maxsize
    total = 0
    for i in range(N - 1):
        cost = cities[i]
        if prev > cost:
            prev = cost
        total += prev * roads[i]
    print(total)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
