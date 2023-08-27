import sys


def main():
    A = len(input().strip())
    B = len(input().strip())
    print('go' if A >= B else 'no')
    


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
