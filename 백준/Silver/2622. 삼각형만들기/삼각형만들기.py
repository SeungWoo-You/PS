import sys


def main():
    N = int(input())
    total = 0
    for c1 in range(1, N // 3 + 1):
        for c2 in range(c1, (N - c1) // 2 + 1):
            c3 = N - c2 - c1
            if c3 < c1 + c2:
                total += 1
    print(total)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
