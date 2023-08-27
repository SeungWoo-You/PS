import sys


def main():
    N = int(input())
    if N == 1:
        print('*')
    else:
        print(' ' * (N - 1) + '*')
        for i in range(2, N):
            front = ' ' * (N - i)
            mid = ' ' * (2 * i - 3)
            print(front + '*' + mid + '*')
        print('*' * (2 * N - 1))


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
