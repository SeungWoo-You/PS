import sys


def main():
    N = int(input())
    ls = list(map(int, input().split()))
    res = [0] * N
    for i, x in enumerate(ls, start=1):
        for j, k in enumerate(res):
            if x == 0:
                if k == 0:
                    break
                else:
                    continue
            if k == 0:
                x -= 1
        res[j] = i
    print(*res)


if __name__ == "__main__":
    input = sys.stdin.readline
    main()
