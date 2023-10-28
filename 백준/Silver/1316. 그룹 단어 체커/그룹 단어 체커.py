import sys


def main():
    N = int(input())
    total = 0
    for _ in range(N):
        S = input().strip()
        checked: set[str] = set()
        prev = ''
        for x in S:
            if x in checked and x != prev:
                break
            prev = x
            checked.add(x)
        else:
            total += 1
    print(total)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
