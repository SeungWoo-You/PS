import sys

def main():
    L, P = map(int, input().split())
    A = list(map(int, input().split()))
    total = L * P
    for x in A:
        print(x - total, end=' ')


if __name__ == '__main__':
    input = sys.stdin.readline
    main()