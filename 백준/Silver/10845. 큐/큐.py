from collections import deque
import sys


def main():
    input = sys.stdin.readline
    N = int(input())
    q: deque[str] = deque()
    for _ in range(N):
        line = input().strip().split()
        if len(line) == 2:
            q.append(line[-1])
            continue
        cmd = line[0]
        if cmd == 'pop':
            try:
                print(q.popleft())
            except:
                print(-1)
        elif cmd == 'size':
            print(len(q))
        elif cmd == 'empty':
            print(1 if not q else 0)
        elif cmd == 'front':
            try:
                print(q[0])
            except:
                print(-1)
        elif cmd == 'back':
            try:
                print(q[-1])
            except:
                print(-1)


if __name__ == '__main__':
    main()
