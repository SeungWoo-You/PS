import sys


def main():
    N = int(input())
    ls = list(map(int, input().split()))
    M = sys.maxsize
    num = -1
    for n in range(1, max(ls) + 1):
        temp = sum(abs(x - n) for x in ls)
        if temp < M:
            num = n
            M = temp
    print(num)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
