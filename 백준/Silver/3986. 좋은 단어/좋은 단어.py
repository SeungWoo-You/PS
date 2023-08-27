import sys


def main():
    N = int(input())
    words = [input().strip() for _ in range(N)]

    count = 0
    for wd in words:
        stack: list[str] = []
        for c in wd:
            if not stack:
                stack.append(c)
                continue
            elif stack[-1] == c:
                stack.pop()
                continue
            stack.append(c)
        if not stack:
            count += 1
    print(count)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
