import sys


def main():
    input = sys.stdin.readline
    N = int(input())
    stack: list[str] = []
    for _ in range(N):
        line = input().strip().split()
        if len(line) == 2:
            stack.append(line[1])
            continue
        cmd = line[0]
        if cmd == 'pop':
            print(stack.pop() if stack else -1)
        elif cmd == 'size':
            print(len(stack))
        elif cmd == 'empty':
            print(1 if not stack else 0)
        elif cmd == 'top':
            print(stack[-1] if stack else -1)


if __name__ == '__main__':
    main()
