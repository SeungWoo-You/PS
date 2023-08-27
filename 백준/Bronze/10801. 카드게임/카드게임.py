import sys


def main():
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    res = {'A': 0, 'B': 0}
    for a, b in zip(A, B):
        if a > b:
            res['A'] += 1
        elif a < b:
            res['B'] += 1
    if res['A'] > res['B']:
        print('A')
    elif res['A'] < res['B']:
        print('B')
    else:
        print('D')


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
