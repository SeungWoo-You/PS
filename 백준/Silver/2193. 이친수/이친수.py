import sys


def main():
    N = int(input())
    count = [0, 1, 1]
    while len(count) - 1 < N:
        count.append(count[-2] + count[-1])
    print(count[N])


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
