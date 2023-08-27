import sys
from collections import deque


def main():
    A, B = map(int, input().split())
    Q = deque([(A, 1)])
    while Q:
        x, count = Q.popleft()
        if x == B:
            print(count)
            return
        if 2 * x <= B:
            Q.append((2 * x, count + 1))
        if 10 * x + 1 <= B:
            Q.append((10 * x + 1, count + 1))
    print(-1)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
