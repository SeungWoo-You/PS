import sys
from statistics import mean, median


def main():
    ls = [int(input()) for _ in range(5)]
    print(mean(ls), median(ls), sep='\n')


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
