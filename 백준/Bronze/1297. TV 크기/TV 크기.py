import sys
import math


def main():
    D, H, W = map(int, input().split())
    k = math.sqrt(D**2 / (H**2 + W**2))
    print(math.floor(H * k), math.floor(W * k))


if __name__ == "__main__":
    input = sys.stdin.readline
    main()
