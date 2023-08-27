import sys
from collections import deque


def main():
    T = int(input())
    for _ in range(T):
        L = input().rstrip('\n')
        left: list[str] = []
        right: deque[str] = deque([])

        for s in L:
            try:
                if s == '<':
                    right.appendleft(left.pop())
                elif s == '>':
                    left.append(right.popleft())
                elif s == '-':
                    left.pop()
                else:
                    left.append(s)
            except:
                continue
        print(''.join(left + list(right)))


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
