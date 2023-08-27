import sys


def main():
    L, P, V = map(int, input().split())
    t = 1
    while (L, P, V) != (0, 0, 0):
        quot, rem = divmod(V, P)
        usable = quot * L
        usable = usable + rem if L > rem else usable + L
        print(f'Case {t}: {usable}')
        t += 1
        L, P, V = map(int, input().split())


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
