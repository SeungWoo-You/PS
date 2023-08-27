import sys


def main():
    K = int(input())
    S: list[int] = []
    for _ in range(K):
        x = int(input())
        if x != 0:
            S.append(x)
        else:
            S.pop()
    print(sum(S))


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
