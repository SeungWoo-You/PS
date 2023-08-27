import sys


def main():
    res = 0
    m = sys.maxsize
    for _ in range(7):
        x = int(input())
        if x % 2 == 1:
            res += x
            m = min(m, x)
    if m == sys.maxsize:
        print(-1)
        return
    print(res)
    print(m)


if __name__ == "__main__":
    input = sys.stdin.readline
    main()
