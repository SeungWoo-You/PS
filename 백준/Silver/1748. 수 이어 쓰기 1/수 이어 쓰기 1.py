import sys
import math


def main():
    N = int(input())
    k = math.floor(math.log10(N))
    ans = 0
    for i in range(k):
        ans += 9 * 10**(i) * (i + 1)
    try:
        rem = N - 9 * int('1' * k)
    except:
        rem = N
    ans += rem * (k + 1)
    print(ans)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
