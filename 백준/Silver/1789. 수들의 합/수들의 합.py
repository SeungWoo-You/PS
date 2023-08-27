import sys


def main():
    S = int(input())
    res = 1
    for n in range(1, S):
        k = nat_sum(n)
        if k > S:
            res = n - 1
            break
        elif k == S:
            res = n
    print(res)


def nat_sum(n: int) -> int:
    return n * (n + 1) // 2


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
