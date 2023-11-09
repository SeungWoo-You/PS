import sys


def main():
    N = int(input())
    D: dict[str, tuple[int]] = {}
    for _ in range(N):
        name, s1, s2, s3 = input().strip().split()
        D[name] = tuple(map(int, [s1, s2, s3]))
    res = sorted(
        D.items(), key=lambda p: (-p[1][0], p[1][1], -p[1][2], p[0]))
    for T in res:
        print(T[0])


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
