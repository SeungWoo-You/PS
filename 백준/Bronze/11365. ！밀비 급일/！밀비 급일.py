import sys


def main():
    t = input().rstrip('\n')
    while t != 'END':
        print(*reversed(t), sep='')
        t = input().rstrip('\n')


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
