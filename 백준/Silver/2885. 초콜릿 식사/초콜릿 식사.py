import sys
import math


def main():
    K = int(input())
    s = math.log2(K)
    choco = 2**int(s) if s.is_integer() else 2**math.ceil(s)
    print(choco, divide(choco, K))


def divide(choco: int, K: int) -> int:
    if K == choco:
        return 0
    count = 0
    while K > 0:
        choco //= 2
        if choco <= K:
            K -= choco
        count += 1
    return count


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
