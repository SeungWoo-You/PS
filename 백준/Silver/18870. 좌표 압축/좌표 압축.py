import sys


def main():
    N = int(input())
    pts = list(map(int, input().split()))
    res = [0] * N

    D = [(pts[i], i) for i in range(N)]
    D.sort()

    prev = D[0][0]
    count = 0
    for x, i in D:
        if x != prev:
            count += 1
        res[i] = count
        prev = x
    print(*res)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
