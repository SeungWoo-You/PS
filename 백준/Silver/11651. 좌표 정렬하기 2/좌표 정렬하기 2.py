import sys


def main():
    N = int(input())
    ls: list[tuple[int]] = []
    for _ in range(N):
        pt = tuple(map(int, input().split()))
        ls.append(pt)
    ls.sort(key=lambda p: (p[1], p[0]))
    for p in ls:
        print(*p)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
