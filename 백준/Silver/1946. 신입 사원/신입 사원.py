import sys


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        scores = [tuple(map(int, input().split())) for _ in range(N)]
        scores.sort()
        count = 1
        prev = scores[0][1]
        for i in range(1, N):
            if scores[i][1] < prev:
                count += 1
                prev = scores[i][1]
        print(count)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
