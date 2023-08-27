import sys


def main():
    T = int(input())
    for _ in range(T):
        N = 9
        count = {'Y': 0, 'K': 0}
        for _ in range(N):
            Y, K = map(int, input().split())
            count['Y'] += Y
            count['K'] += K
        if count['Y'] > count['K']:
            print("Yonsei")
        elif count['Y'] < count['K']:
            print("Korea")
        else:
            print('Draw')


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
