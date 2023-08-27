import sys


def main():
    N = int(input())
    M = int(input())
    S = input().strip()
    P = 'I' + 'OI' * N

    i = 0
    count = 0
    while i < M:
        if S[i] == 'I':
            if S.find(P, i, i + 2 * N + 1) != -1:
                count += 1
                i += 2
            else:
                i += 1
        else:
            i += 1
    print(count)


if __name__ == "__main__":
    input = sys.stdin.readline
    main()
