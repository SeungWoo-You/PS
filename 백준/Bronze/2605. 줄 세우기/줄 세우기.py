import sys
from collections import deque


def main():
    N = int(input())
    nums = list(map(int, input().split()))
    Q: deque[int] = deque()
    right: deque[int] = deque()
    for i, x in enumerate(nums, start=1):
        for _ in range(x):
            right.appendleft(Q.pop())
        Q.append(i)
        Q.extend(right)
        right.clear()
    print(*Q)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
