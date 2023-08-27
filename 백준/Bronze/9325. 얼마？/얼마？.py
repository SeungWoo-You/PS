import sys


def main():
    T = int(input())
    for _ in range(T):
        s = int(input())
        n = int(input())
        for _ in range(n):
            p, q = map(int, input().split())
            s += p * q
        print(s)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
