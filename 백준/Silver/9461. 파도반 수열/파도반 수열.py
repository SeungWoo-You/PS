import sys


def main():
    T = int(input())
    res = [0, 1, 1, 1, 2]
    for _ in range(T):
        N = int(input())
        if len(res) > N:
            print(res[N])
            continue
        while len(res) <= N:
            res.append(res[-1] + res[-5])
        print(res[N])


if __name__ == "__main__":
    input = sys.stdin.readline
    main()
