import sys


def main():
    T = int(input())
    A = [0, 500, 300, 200, 50, 30, 10]
    B = [0, 512, 256, 128, 64, 32]
    for _ in range(T):
        a, b = map(int, input().split())
        a_prize, b_prize = 0, 0
        for n in range(7):
            last = n * (n + 1) // 2
            if a <= last:
                a_prize = A[n]
                break
        for n in range(6):
            last = 2**n - 1
            if b <= last:
                b_prize = B[n]
                break
        print((a_prize + b_prize) * 10000)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
