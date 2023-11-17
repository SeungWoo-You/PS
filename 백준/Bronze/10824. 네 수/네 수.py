import sys


def main():
    A, B, C, D = input().strip().split()
    print(int(A + B) + int(C + D))


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
