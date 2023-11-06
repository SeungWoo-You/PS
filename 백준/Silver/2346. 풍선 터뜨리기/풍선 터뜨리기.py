import sys
from collections import deque


def main():
    N = int(input())
    B = map(int, input().split())
    balloon = deque([(i, m) for i, m in zip(range(1, N + 1), B)])
    idx, move = balloon.popleft()
    print(idx, end=' ')
    while balloon:
        if move > 0:
            for _ in range(move - 1):
                balloon.append(balloon.popleft())
        else:
            for _ in range(-move):
                balloon.appendleft(balloon.pop())
        idx, move = balloon.popleft()
        print(idx, end=' ')


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
