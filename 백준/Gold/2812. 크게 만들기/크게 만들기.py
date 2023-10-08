import sys


def main():
    N, K = map(int, input().split())
    A = input().strip()
    S: list[str] = []
    rm = 0
    for a in A:
        while S:
            if rm == K:
                break
            if int(a) > int(S[-1]):
                S.pop()
                rm += 1
            else:
                break
        S.append(a)
    for _ in range(rm, K):
        S.pop()
    print(''.join(S))


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
