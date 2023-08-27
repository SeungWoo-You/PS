import math


def main():
    T = int(input())
    for _ in range(T):
        a, b, c = map(int, input().split())
        if c > max(a, b):
            print('NO')
            continue
        get = math.gcd(a, b)
        if c % get == 0:
            print('YES')
        else:
            print('NO')


if __name__ == '__main__':
    main()
