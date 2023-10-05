import sys
from collections import Counter


def main():
    S = list(map(int, list(input().strip())))
    C = Counter(S)
    count = [0, 0]
    answer = ''
    for x in S:
        count[x] += 1
        if x == 0:
            if count[x] > C[x] // 2:
                continue
        elif x == 1:
            if count[x] <= C[x] // 2:
                continue
        answer += str(x)
    print(answer)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
