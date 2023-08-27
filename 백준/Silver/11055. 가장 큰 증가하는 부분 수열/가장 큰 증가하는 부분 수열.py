import sys


def main():
    N = int(input())
    A = list(map(int, input().split()))
    idx = 0
    total = A.copy()

    for i in range(N):
        for j in range(i):
            if A[j] < A[i]:
                total[i] = max(total[i], total[j] + A[i])
            if total[idx] < total[i]:
                idx = i
    print(total[idx])


if __name__ == "__main__":
    input = sys.stdin.readline
    main()
