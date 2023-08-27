import math


def main():
    N, K = map(int, input().split())
    print(math.comb(N, K))


if __name__ == '__main__':
    main()
