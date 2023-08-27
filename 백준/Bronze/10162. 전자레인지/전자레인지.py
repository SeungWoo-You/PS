import sys


def main():
    A, B, C = 5 * 60, 60, 10
    T = int(input())
    quot_a, rem_a = divmod(T, A)
    quot_b, rem_b = divmod(rem_a, B)
    quot_c, rem_c = divmod(rem_b, C)
    if rem_c != 0:
        print(-1)
    else:
        print(quot_a, quot_b, quot_c)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
