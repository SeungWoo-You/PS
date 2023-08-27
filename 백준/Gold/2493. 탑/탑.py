import sys


def main():
    N = int(input())
    tower = list(map(int, input().split()))
    stack: list[tuple[int, int]] = []
    receive = {v: 0 for v in range(1, N + 1)}
    for i, t in enumerate(tower, start=1):
        while stack:
            j, prev = stack[-1]
            if prev < t:
                stack.pop()
            else:
                break
        if stack:
            receive[i] = j
        stack.append((i, t))
    print(*receive.values())


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
