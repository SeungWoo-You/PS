import sys


def main():
    ls = list(map(int, input().split()))
    while ls[0] != 0:
        ls.sort()
        k = len(set(ls))
        if ls[-1] >= ls[0] + ls[1]:
            print("Invalid")
        elif k == 1:
            print("Equilateral")
        elif k == 2:
            print("Isosceles")
        else:
            print("Scalene")
        ls = list(map(int, input().split()))


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
