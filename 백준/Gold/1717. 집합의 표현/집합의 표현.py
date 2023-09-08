import sys


def main():
    n, m = map(int, input().split())
    ids = list(range(n + 1))
    for _ in range(m):
        cmd, a, b = map(int, input().split())
        if cmd == 0:
            union(a, b, ids)
        else:
            if find(a, ids) == find(b, ids):
                print('YES')
            else:
                print('NO')


def union(x: int, y: int, ids: list[int]) -> None:
    a, b = find(x, ids), find(y, ids)
    if a > b:
        ids[a] = b
    else:
        ids[b] = a


def find(x: int, ids: list[int]) -> int:
    if x != ids[x]:
        ids[x] = find(ids[x], ids)
    return ids[x]


if __name__ == '__main__':
    input = sys.stdin.readline
    sys.setrecursionlimit(10**5)
    main()
