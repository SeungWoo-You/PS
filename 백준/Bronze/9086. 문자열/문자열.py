import sys


def main():
    T = int(input())
    for _ in range(T):
        S = input().strip()
        print(S[0] + S[-1])


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
