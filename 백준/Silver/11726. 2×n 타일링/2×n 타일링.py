import sys


def main():
    n = int(input())
    count = [0, 1, 2]
    while len(count) < n + 1:
        count.append((count[-1] % MOD + count[-2] % MOD) % MOD)
    print(count[n])


if __name__ == '__main__':
    input = sys.stdin.readline
    MOD = 10007
    main()
