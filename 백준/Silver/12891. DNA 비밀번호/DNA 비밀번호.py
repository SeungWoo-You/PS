import sys
from collections import Counter


def main():
    M, N = map(int, input().split())
    S = input().strip()
    C = Counter(S[:N])
    target = {c: i for c, i in zip('ACGT', map(int, input().strip().split()))}
    total = 1 if is_possible(C, target) else 0
    for i in range(N, M):
        s, e = S[i - N], S[i]
        C[s] -= 1
        C[e] += 1
        if is_possible(C, target):
            total += 1
    print(total)


def is_possible(C: Counter[str], target: dict[str, int]) -> bool:
    for c in 'ACGT':
        if target[c] > C[c]:
            return False
    return True


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
