import sys


def main():
    T = int(input())
    ls: list[str] = [input().strip() for _ in range(T)]
    for S in ls:
        X = S
        rS = ''.join(reversed(S))
        for i in range(len(X)):
            if X[i:] + ''.join(reversed(X[:i])) == rS:
                X = X + ''.join(reversed(X[:i]))
                break
        print(X)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
