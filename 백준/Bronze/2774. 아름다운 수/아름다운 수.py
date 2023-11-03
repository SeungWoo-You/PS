import sys


def main():
    T = int(input())
    for _ in range(T):
        L = list(input().strip())
        print(len(set(L)))


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
