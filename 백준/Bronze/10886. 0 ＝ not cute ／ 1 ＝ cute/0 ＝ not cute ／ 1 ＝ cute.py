import sys
from collections import Counter


def main():
    N = int(input())
    survey = [int(input()) for _ in range(N)]
    survey = Counter(survey)
    if survey[0] > survey[1]:
        print('Junhee is not cute!')
    else:
        print('Junhee is cute!')


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
