import sys


def main():
    A = sum(map(int, input().split()))
    B = sum(map(int, input().split()))
    print(max(A, B))


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
