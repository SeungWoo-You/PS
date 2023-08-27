import sys
from collections import deque


def main():
    P = int(input())
    for _ in range(P):
        info = list(map(int, input().split()))
        T, line = info[0], info[1:]
        left: deque[int] = deque([])
        right: deque[int] = deque([])
        step = 0
        for std in line:
            while left:
                if left[-1] > std:
                    right.appendleft(left.pop())
                else:
                    left.append(std)
                    break
            if not left:
                left.append(std)
            step += len(right)
            left.extend(right)
            right.clear()
        print(T, step)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
