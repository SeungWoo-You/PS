import sys


def main():
    K = int(input())
    for i in range(1, K + 1):
        score = list(map(int, input().split()))
        score = score[1:]
        score.sort(reverse=True)

        diff = 0
        prev = score[0]
        for x in score:
            diff = max(diff, abs(prev - x))
            prev = x
        print(f'Class {i}')
        print(f'Max {score[0]}, Min {score[-1]}, Largest gap {diff}')


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
