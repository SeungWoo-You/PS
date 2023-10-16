import sys


def main():
    scores = [sum(map(int, input().split())) for _ in range(5)]
    best = max(scores)
    print(scores.index(best) + 1, best)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
