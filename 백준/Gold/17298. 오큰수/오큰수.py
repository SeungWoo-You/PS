import sys


def main():
    N = int(input())
    A = list(map(int, input().split()))
    S: list[tuple[int, int]] = []
    answer = [-1] * N
    for i, a in enumerate(A):
        while S:
            if a > S[-1][1]:
                j, _ = S.pop()
                answer[j] = a
            else:
                break
        S.append((i, a))
    for i, _ in S:
        answer[i] = -1
    print(*answer)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
