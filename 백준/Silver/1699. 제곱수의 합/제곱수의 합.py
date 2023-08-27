import sys
import math


def main():
    N = int(input())
    res = [0, 1, 2]
    while len(res) <= N:
        k = int(math.sqrt(len(res)))
        res.append(min([res[-x**2] for x in range(1, k + 1)]) + 1)
    print(res[N])


if __name__ == "__main__":
    input = sys.stdin.readline
    main()
