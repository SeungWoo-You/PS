import sys


def main():
    N = input().strip()
    if int(N) < 10:
        N = '0' + N
    X = N
    Y = ''
    cycle = 0
    while Y != N:
        temp = str(sum(map(int, list(X))))
        Y = X[-1] + temp[-1]
        X = Y
        cycle += 1
    print(cycle)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
