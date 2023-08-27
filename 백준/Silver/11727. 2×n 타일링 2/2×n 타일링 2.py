import sys


def main():
    n = int(input())
    res = [0, 1, 3]

    while len(res) <= n:
        temp = res[-1] + res[-2] * 2 % MOD
        res.append(temp % MOD)
    print(res[n])

if __name__ == "__main__":
    input = sys.stdin.readline
    MOD = 10007
    main()
