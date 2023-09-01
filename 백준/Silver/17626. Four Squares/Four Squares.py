import sys


def main():
    N = int(input())
    res = [0, 1]
    for x in range(2, N + 1):
        count = sys.maxsize
        for j in range(1, x + 1):
            if j**2 == x:
                count = min(count, 1)
                break
            elif j**2 < x:
                count = min(count, res[x - j**2] + 1)
            else:
                break
        res.append(count)
    print(res[N])


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
