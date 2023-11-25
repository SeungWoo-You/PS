import sys


def main():
    N = int(input())
    count = 0
    for n in range(1, N + 1):
        X = str(n)
        if len(X) == 1:
            count += 1
            continue
        prev, now = int(X[0]), int(X[1])
        diff = now - prev
        for i in range(1, len(X)):
            if int(X[i]) - int(X[i - 1]) != diff:
                break
        else:
            count += 1
    print(count)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
