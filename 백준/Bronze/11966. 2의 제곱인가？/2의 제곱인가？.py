import sys
import math


def main():
    N = int(input())
    if math.log2(N).is_integer() == True:
        print(1)
    else:
        print(0)


if __name__ == "__main__":
    input = sys.stdin.readline
    main()
