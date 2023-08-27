import sys
from collections import deque


def main():
    N = int(input())
    A = deque(sorted(map(int, input().split())))

    T = sum(A)
    cost = 0
    while A:
        s, e = A[0], A[-1]
        rm = A.popleft() if s >= T - e else A.pop()
        T -= rm
        cost += T * rm
    print(cost)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
