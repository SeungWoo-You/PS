from collections import deque
import sys


def main():
    N = int(input())
    queue: deque[str] = deque()
    for _ in range(N):
        line = input().strip().split()
        if len(line) == 2:
            cmd, x = line
            if cmd == 'push_front':
                queue.appendleft(x)
            elif cmd == 'push_back':
                queue.append(x)
            continue
        cmd = line[0]
        if cmd == 'pop_front':
            print(queue.popleft() if queue else -1)
        elif cmd == 'pop_back':
            print(queue.pop() if queue else -1)
        elif cmd == 'size':
            print(len(queue))
        elif cmd == 'empty':
            print(1 if not queue else 0)
        elif cmd == 'front':
            print(queue[0] if queue else -1)
        elif cmd == 'back':
            print(queue[-1] if queue else -1)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
