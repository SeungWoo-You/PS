import sys
import math


def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    idx_ls = [i for i in range(N)]
    idx_ls.sort(key=lambda i: B[i])
    A.sort(reverse=True)
    res = sum(map(math.prod, zip(A, [B[i] for i in idx_ls])))
    print(res)


if __name__ == "__main__":
    input = sys.stdin.readline
    main()
