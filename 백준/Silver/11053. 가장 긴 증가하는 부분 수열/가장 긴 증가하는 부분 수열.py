import sys


def main():
    N = int(input())
    A = list(map(int, input().split()))

    res = [0] * N
    res[0] = 1
    idx = 0

    for i in range(1, N):
        for j in range(i):
            if A[j] < A[i] and res[i] < res[j] + 1:
                res[i] = res[j] + 1
        if res[idx] < res[i]:
            idx = i
        if res[i] == 0:
            res[i] = 1
    print(res[idx])


if __name__ == "__main__":
    input = sys.stdin.readline
    main()
