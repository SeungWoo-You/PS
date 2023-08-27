import sys


def main():
    total = int(input())
    recipe = [int(input()) for _ in range(9)]
    print(total - sum(recipe))


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
