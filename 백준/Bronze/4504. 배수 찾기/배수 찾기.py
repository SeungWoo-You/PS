import sys


def main():
    n = int(input())
    x = int(input())
    while x != 0:
        k = x / n
        if k.is_integer() == True:
            print(f"{x} is a multiple of {n}.")
        if k.is_integer() == False:
            print(f"{x} is NOT a multiple of {n}.")
        x = int(input())


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
