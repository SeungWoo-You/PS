import sys

def main():
    N, M = map(int, input().split())
    A = set(map(int, input().split()))
    B = set(map(int, input().split()))
    C = A - B
    print(len(C))
    if len(C) != 0:
        print(*sorted(C))


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
