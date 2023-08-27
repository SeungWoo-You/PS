import sys
from collections import deque


def main():
    L = deque(input().rstrip('\n'))
    R: deque[str] = deque()
    M = int(input())
    for _ in range(M):
        line = input().split()
        cmd = line[0]
        try:
            if cmd == 'L':
                R.appendleft(L.pop())
            elif cmd == 'D':
                L.append(R.popleft())
            elif cmd == 'B':
                L.pop()
            elif cmd == 'P':
                L.append(line[1])
        except:
            pass
    print(''.join(L + R))


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
