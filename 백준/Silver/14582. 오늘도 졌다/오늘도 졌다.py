import sys


def main():
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    score = [0, 0]
    check = 0
    for i in range(9):
        score[0] += A[i]
        if check == 0:
            if score[0] > score[1]:
                check = 1
        score[1] += B[i]
        if check == 1:
            if score[0] < score[1]:
                check = 2
    print('Yes' if check == 2 else 'No')


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
