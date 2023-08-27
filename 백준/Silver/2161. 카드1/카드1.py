import sys
from collections import deque


def main():
    N = int(input())
    cards = deque(range(1, N + 1))
    ans: list[int] = []
    while len(cards) != 1:
        ans.append(cards.popleft())
        cards.append(cards.popleft())
    ans.append(cards.popleft())
    print(*ans)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
