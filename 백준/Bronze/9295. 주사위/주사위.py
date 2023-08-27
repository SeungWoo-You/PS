import sys


def main():
    T = int(input())
    for t in range(1, T + 1):
        print(f'Case {t}: {sum(map(int, input().split()))}')


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
