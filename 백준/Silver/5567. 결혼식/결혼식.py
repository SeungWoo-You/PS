import sys


def main():
    n = int(input())
    m = int(input())
    friend: dict[int, list[int]] = {v: [] for v in range(1, n + 1)}
    for _ in range(m):
        u, v = map(int, input().split())
        friend[u].append(v)
        friend[v].append(u)
    print(find_relation(friend))


def find_relation(friend: dict[int, list[int]]) -> int:
    checked: set[int] = {1}
    checked.update(friend[1])
    Q = friend[1]
    for u in Q:
        checked.update(friend[u])
    return len(checked) - 1


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
