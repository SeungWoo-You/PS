import sys


def main():
    T = int(input())
    for _ in range(T):
        A = list(map(int, input().split()))
        A.sort()
        print(A[-3])


if __name__ == "__main__":
    input = sys.stdin.readline
    main()
