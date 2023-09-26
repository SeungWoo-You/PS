import sys


def main():
    N = int(input())
    info: list[list[int]] = []
    answer = sys.maxsize
    total = 0
    for _ in range(N):
        i, j = map(int, input().split())
        info.append([i, j])
        if len(info) >= 2:
            total += dist(info[-1], info[-2])
    for i in range(1, N - 1):
        T = total - dist(info[i], info[i - 1]) - dist(info[i + 1],
                                                      info[i]) + dist(info[i + 1], info[i - 1])
        answer = min(answer, T)
    print(answer)


def dist(A: list[int], B: list[int]) -> int:
    a1, a2 = A
    b1, b2 = B
    return abs(a1 - b1) + abs(a2 - b2)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
