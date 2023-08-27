import sys


def main():
    K, L = map(int, input().split())
    std_ids = [input().strip() for _ in range(L)]
    S: dict[str, int] = {}
    checked: set[str] = set()
    for x in std_ids:
        if x in checked:
            S.pop(x)
        S[x] = 0
        checked.add(x)
    i = 0
    for k in S.keys():
        print(k)
        i += 1
        if i >= K:
            break


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
