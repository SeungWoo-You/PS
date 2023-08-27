import sys


def main():
    N, M = map(int, input().split())
    pack, single = sys.maxsize, sys.maxsize
    for _ in range(M):
        p, s = map(int, input().split())
        pack = min(pack, p)
        single = min(single, s)

    if single * 6 < pack:
        print(single * N)
    else:
        quot, rem = divmod(N, 6)
        if rem * single < pack:
            print(quot * pack + rem * single)
        else:
            print((quot + 1) * pack)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
